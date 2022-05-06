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
        carte.useCarte(J1)
        self.__carteJeu.append(carte)
        self.__carteMain.remove(carte)
    def getMain(self):
        return self.__carteMain
    def addCarteMain(self, carte):
        self.__carteMain.append(carte)
    def modifTotalMana(self, amount):
        self.__totalMana += amount
    def modifValeurMana(self, amount):
        self.__valeurMana += amount

class Cristal(Carte):
    def __init__(self, coutMana, nom, descr):
        Carte.__init__(self, coutMana, nom, descr)
    def useCarte(self, mage):
        mage.modifTotalMana(2)
        mage.modifValeurMana(-self.__coutMana)

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


J1 = Mage("Jean-Eudes", 20, 10, 10)
J2 = Mage("Billy", 20, 10, 10)

carteCreature = Creature(3, "Bougross", "C'est un Bougross", 5, 2)
carteCristal = Cristal(0, "Handspinners", "Ces handspinners sont magiques !")

J1.addCarteMain(carteCreature)
J1.addCarteMain(carteCristal)


J1main = J1.getMain()
print("------", J1.getName() ,"------")

print("---Mana---")
print(J1.getValeurMana())

print("---Main---")
J1main = J1.getMain()
for i in range(len(J1main)):
    print(J1main[i].getName())

print("---Jeu---")
J1jeu = J1.getJeu()
for i in range(len(J1jeu)):
    print(J1jeu[i].getName())

choixCarte = int(input("Quelle carte voulez-vous placer ?"))

J1.placeCarte(J1main[choixCarte-1])

print("------", J1.getName() ,"------")

print("---Mana---")
print(J1.getValeurMana())

print("---Main---")
J1main = J1.getMain()
for i in range(len(J1main)):
    print(J1main[i].getName())

print("---Jeu---")
J1jeu = J1.getJeu()
for i in range(len(J1jeu)):
    print(J1jeu[i].getName())
