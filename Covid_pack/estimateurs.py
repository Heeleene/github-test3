from abc import ABC

class Estimateurs(ABC):
    def __init__(self,jeu,liste_var):
        self.jeu = jeu
        self.res=[]
        self.liste_var=liste_var

    def ajouter_selection_variable(self, list_var_supp):
        self.liste_var = list(self.liste_var)
        for i in range(0, len(list_var_supp)):
            self.liste_var.append(list_var_supp[i])

    def verif_var(self):
        list_index=[]

        for i in range(0,len(self.liste_var)):
            index = None
            for j in range(0, len(self.jeu.variables)):
                if self.jeu.variables[j] == self.liste_var[i]:
                    index = j
                    list_index.append(index)
            if index == None:
                raise Exception('Le jeu de donnée ne contient pas cette variable')
        return list_index


    def __str__(self):
        model = '\n'.join([
            '{}',
            '  variable(s): {}',
            '  Resultat: {}'])
        return model.format(type(self).__name__,self.liste_var,self.res)




