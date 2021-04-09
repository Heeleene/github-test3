#Il faut changer tout en int object:On pourr aussi rajouter la mediane
from Covid_pack.estimateurs import Estimateurs


class Mode(Estimateurs):
    def __init__(self,jeu,liste_var):
        super().__init__(jeu,liste_var)

    def calcul_mode(self):
        res=0
        cpt_max = 0
        for c in self.verif_var():
            for l in range(0, len(self.jeu.donnee)):
                cpt = 0
                for n in range(0, len(self.jeu.donnee)):
                    if self.jeu.donnee[l][c]==self.jeu.donnee[n][c]:
                        cpt += 1
                if cpt > cpt_max:
                    cpt_max = cpt
                    res = self.jeu.donnee[l][c]
        return (res,cpt_max)


    def calcul_mode_2(self):
        jeux=[]
        liste_jeux=[]
        mode_max=0
        for i in range(0,len(self.jeu.donnee)):
            if len(jeux)<=2000:
                jeux.append(self.jeu.donnee[i])
            else:
                liste_jeux.append(jeux)
                jeux=[]
        for j in range(0,len(liste_jeux)):
            m1=Mode(liste_jeux[j],self.liste_var)
            if m1.calcul_mode()[1]>=mode_max:
                mode_max=m1.calcul_mode()[1]
                res=m1.calcul_mode()[0]
        return res






























