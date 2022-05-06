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
        self.__carteMain = [0]
        self.__carteJeu = [0]
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
    def getMain(self):
        return self.__carteMain
    def modifTotalMana(self, amount):
        self.__totalMana += amount
    def modifValeurMana(self, amount):
        self.__valeurMana += amount

class Cristal(Carte):
    def __init__(self, coutMana, nom, descr):
        Carte.__init__(self, coutMana, nom, descr)
    def useCarte(self, mage):
        mage.modifTotalMana(2)
        mage.modifValeurMana(-self.coutMana)

class Creature(Carte):
    def __init__(self, coutMana, nom, descr, pointCoeur, attaque):
        Carte.__init__(self, coutMana, nom, descr)
        self.__pointCoeur = pointCoeur
        self.__attaque = attaque
    def getPointCoeur(self):
        return self.__pointCoeur
    def getAttaque(self):
        return self.__attaque
    def placeCreature(self, mage):
        mage.modifValeurMana(-self.coutMana)


J1 = Mage("Jean-Eudes", 20, 10, 10)
J2 = Mage("Billy", 20, 10, 10)

print(J1.getMain())