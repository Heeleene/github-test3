
from Covid_pack.estimateurs import Estimateurs



class Moyenne(Estimateurs):
    def __init__(self, jeu, liste_var):
        super().__init__(jeu,liste_var)



    def calcul_moyen(self):
        res = []

        for i in range(0, len(self.liste_var)):
            m=0
            index=None
            for j in range(0, len(self.jeu.variables)):
                if self.jeu.variables[j] == self.liste_var[i]:
                    index = j
            if  index==None :
                raise Exception('Le jeu de donnée ne contient pas cette variable')
            for k in range(0,len(self.jeu.donnee)):
                m += int(self.jeu.donnee[k][index])
            m = m/len(self.jeu.donnee)
            res.append(m)
        self.res=res



