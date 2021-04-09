from Covid_pack.estimateurs import Estimateurs

class Etendue(Estimateurs):
    def __init__(self,jeu,liste_var):
        super().__init__(jeu,liste_var)

    def etendue(self):

        res = []
        for i in range(0, len(self.liste_var)):


            index = None
            for j in range(0, len(self.jeu.variables)):
                if self.jeu.variables[j] == self.liste_var[i]:
                    index = j
            if index == None:
                raise Exception('Le jeu de donnée ne contient pas cette variable')
            jeu_supp = []

            for l in range(0, len(self.jeu.donnee)):
                jeu_supp.append(int(self.jeu.donnee[l][index]))
            max = jeu_supp[0]
            min = max
            for n in range(1,len(jeu_supp)):
                if max <jeu_supp[n]:
                    max=jeu_supp[n]
                if min>jeu_supp[n]:
                    min=jeu_supp[n]
            res.append([min,max])
        self.res=res





