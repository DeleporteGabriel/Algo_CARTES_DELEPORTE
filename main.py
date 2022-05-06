import random

class Carte():
    def __init__(self, coutMana, nom, descr):
        self.__coutMana = coutMana
        self.__nom = nom
        self.__descr = descr
    def getName(self):
        return self.__nom
    def getCoutMana(self):
        return self.__coutMana
    def getDescription(self):
        return self.__descr

class Mage():
    def __init__(self, nom, pointCoeur, totalMana, valeurMana):
        self.__nom = nom
        self.__pointCoeur = pointCoeur
        self.__totalMana = totalMana
        self.__valeurMana = valeurMana
        self.__carteMain = []
        self.__carteJeu = []
    def getName(self):
        return self.__nom
    def getPointCoeur(self):
        return self.__pointCoeur
    def getTotalMana(self):
        return self.__totalMana
    def getValeurMana(self):
        return self.__valeurMana
    def getJeu(self):
        return self.__carteJeu
    def placeCarte(self, carte):
        carte.useCarte(self)
        if (carte.getName() != "Couteu"):
            self.__carteJeu.append(carte)
        self.__carteMain.remove(carte)
    def getMain(self):
        return self.__carteMain
    def addCarteMain(self, carte):
        self.__carteMain.append(carte)
    def modifPC(self, amount):
        self.__pointCoeur += amount
    def modifTotalMana(self, amount):
        self.__totalMana += amount
    def modifValeurMana(self, amount):
        self.__valeurMana += amount

class Cristal(Carte):
    def __init__(self, coutMana, nom, descr):
        Carte.__init__(self, coutMana, nom, descr)
    def useCarte(self, mage):
        mage.modifTotalMana(2)
        mage.modifValeurMana(-self.getCoutMana())

class Creature(Carte):
    def __init__(self, coutMana, nom, descr, pointCoeur, attaque):
        Carte.__init__(self, coutMana, nom, descr)
        self.__pointCoeur = pointCoeur
        self.__attaque = attaque
    def getPointCoeur(self):
        return self.__pointCoeur
    def getAttaque(self):
        return self.__attaque
    def useCarte(self, mage):
        mage.modifValeurMana(-self.getCoutMana())
    def attaqueEnnemis(self, mageEnnemis):
        mageEnnemis.modifPC(-self.__attaque)
    def modifPC(self, amount):
        self.__pointCoeur += amount


class Blast(Carte):
    def __init__(self, coutMana, nom, descr, degat):
        Carte.__init__(self, coutMana, nom, descr)
        self.__degat = degat
    def getDegat(self):
        return self.__degat
    def useCarte(self, mage):
        mage.modifValeurMana(-self.getCoutMana())
    def explosion(self, cible):
        cible.modifPC(-self.getDegat())

def statJoueur(Joueur):
    print("------", Joueur.getName() ,"------")

    print("---Stats---")
    print("PC : ", Joueur.getPointCoeur())
    print("Mana : ", Joueur.getValeurMana(), "/", Joueur.getTotalMana())

    print("---Main---")
    Joueurmain = Joueur.getMain()
    i = 0
    for i in range(len(Joueurmain)):
        print(Joueurmain[i].getName())

    print("---Jeu---")
    Joueurjeu = Joueur.getJeu()
    i = 0
    for i in range(len(Joueurjeu)):
        print(Joueurjeu[i].getName())

def tourJoueur(Joueur, Adverse):

    Joueurjeu = Joueur.getJeu()
    i = 0
    for i in range(len(Joueurjeu)):
        if (Joueurjeu[i].getName() == "Bougross"):
            if (Joueurjeu[i].getPointCoeur() <= 0):
                Joueur.getJeu().remove(Joueurjeu[i])
    
    Joueur.modifValeurMana(2)
    if (Joueur.getValeurMana() > Joueur.getTotalMana()):
        Joueur.modifValeurMana(Joueur.getTotalMana() - Joueur.getValeurMana())

    print(Joueur.getName(), "pioche une carte")
    randomizePioche = random.randrange(0, 3)
    if (randomizePioche < 1):
        Joueur.addCarteMain(carteCreature)
    elif (randomizePioche < 2):
        Joueur.addCarteMain(carteCristal)
    else:
        Joueur.addCarteMain(carteBlast)

    statJoueur(Joueur)

    choixAction = 1
    while(choixAction == 1):
        choixAction = int(input("Que voulez-vous faire ? 1.Placer une carte 2.Terminer votre tour\n"))

        if (choixAction == 1):
            choixCarte = int(input("Quelle carte voulez-vous placer ? (0.Annuler l'action)\n"))
            while (choixCarte != 0 and Joueur.getMain()[choixCarte-1].getCoutMana() > Joueur.getValeurMana()):
                choixCarte = int(input("Quelle carte voulez-vous placer ? (0.Annuler l'action)\n"))

            if (choixCarte != 0):
                if (Joueur.getMain()[choixCarte-1].getName() == "Couteu"):
                    choixCible = int(input("Qui voulez-vous attaquer? 1.Joueur Adverse 2.Une de ses créatures"))
                    if (choixCible == 1):
                        Joueur.getMain()[choixCarte-1].explosion(Adverse)
                    if (choixCible == 2):
                        i = 0
                        for i in range(len(Adverse.getJeu())):
                            if (Adverse.getJeu()[i].getName() == "Bougross"):
                                Joueur.getMain()[choixCarte-1].explosion(Adverse.getJeu()[i])
                                i = 99999999
                Joueur.placeCarte(Joueur.getMain()[choixCarte-1])

                statJoueur(Joueur)
        else:
            break

    Joueurjeu = Joueur.getJeu()
    i = 0
    j = 0
    for i in range(len(Joueurjeu)):
        if (Joueurjeu[i].getName() == "Bougross"):
            print("Le Bougross de", Joueur.getName(), "attaque !")
            adversejeu = Adverse.getJeu()
            presenceBougross = 0
            for j in range(len(adversejeu)):
                if (adversejeu[j].getName() == "Bougross"):
                    Joueurjeu[i].attaqueEnnemis(adversejeu[j])
                    j = 999999
                    i = 999999
                    presenceBougross = 1
            if (presenceBougross == 0):
                Joueurjeu[i].attaqueEnnemis(J2)


J1 = Mage("Jean-Eudes", 20, 10, 10)
J2 = Mage("Billy", 20, 10, 10)

carteCreature = Creature(3, "Bougross", "C'est un Bougross", 5, 2)
carteCristal = Cristal(0, "Handspinners", "Ces handspinners sont magiques !")
carteBlast = Blast(2, "Couteu", "C'est un couteu vert", 4)

J1.addCarteMain(carteCreature)
J1.addCarteMain(carteCristal)
J1.addCarteMain(carteBlast)

J2.addCarteMain(carteCreature)
J2.addCarteMain(carteCristal)
J2.addCarteMain(carteBlast)

victoire = False
while (victoire == False):
    tourJoueur(J1, J2)
    if (J2.getPointCoeur() <= 0):
        victoire == True

    tourJoueur(J2, J1)
    if (J1.getPointCoeur() <= 0):
        victoire == True