import csv
class Data:
    def __init__(self,data):
        self.variables=data[0]
        self.donnee=data[1:len(data)]

    @staticmethod
    def charger_jeu_donnees(nom_data):
        #Faire un dico???
        data=[]
        if nom_data=='donnees hospitalieres par classe et age':
            nom_table='donnees-hospitalieres-classe-age-covid19-2021-03-03-17h03'
        elif nom_data=='donnees hospitalieres':
            nom_table='donnees-hospitalieres-covid19-2021-03-03-17h03'

        else:
            raise Exception('Pas de donnes de ce nom')
        with open(nom_table+'.csv', encoding='ISO-8859-1') as csvfile:
            covidreader = csv.reader(csvfile, delimiter=';')
            for row in covidreader:
                data.append(row)
        return Data(data)


    def __str__(self):
        model = '\n'.join([
            '{}',
            '  variables: {}',
            '  Premiere ligne: {}',
            '  nombre de lignes:{}'])
        return model.format(type(self).__name__,
                            '   ,  '.join(str(self.variables[i])for i in range(0,len(self.variables))),
                            self.donnee[0],
                            len(self.donnee)
                            )
