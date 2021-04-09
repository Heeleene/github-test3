from Covid_pack.estimateurs import Estimateurs

class Variance(Estimateurs):
    def __init__(self,jeu,liste_var):
        super().__init__(jeu,liste_var)


    def calcul_variance(self):
        res=[]
        s=0

        from Covid_pack.moyenne import Moyenne
        moy=Moyenne(self.jeu,self.liste_var)
        moy.calcul_moyen()

        for i in range(0,len(self.liste_var)):
            index = None
            for j in range(0, len(self.jeu.variables)):
                if self.jeu.variables[j] == self.liste_var[i]:
                    index = j
            if index == None:
                raise Exception('Le jeu de donnée ne contient pas cette variable')
            for k in range(0, len(self.jeu.donnee)):
                s += (int(self.jeu.donnee[k][index]) - int(moy.res[i])) ** 2
            s = s / len(self.jeu.donnee)
            res.append(s)
        self.res=res




