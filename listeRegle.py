#Importation de module
from tkinter import *
from regle import *
import json
import os

class ListeRegle:
    
    def __init__(self, regles = []):
        self.regles = regles

    def get_regles(self):
        return self.regles

    def set_regles(self, r):
        self.regles = r
 
    def charger(self):
        """
           Fonction qui permet d'afficher les règles contenu dans le fichier .ini 
        """
        file = open(os.path.dirname(os.path.abspath(__file__)) + "\..\config\elix.ini","r")
        file_r = file.read()
        datastore = json.loads(file_r)
        file.close()
        regles = datastore["regles"]
        listeRegleObj = ListeRegle()
        for i in regles:
            regle = regles[i]
            r = Regle(regle["amorce"], regle["apartirde"], regle["prefixe"], regle["nomfichier"], regle["postfixe"], regle["extensions"])
            listeRegleObj.ajouteRegle(r)
        return listeRegleObj
    
    def sauvegarder(self):
        """
           Fonction qui permet de sauvegarder les règles dans un fichier .ini
        """
        f_d = open(os.path.dirname(os.path.abspath(__file__))+"\..\config\elix.ini", "w")
        dic = {"regles":{}}
        dicRelge = {}
        i = 0
        for regle in self.regles:
            dicRelge = {"amorce": regle.amorce, "apartirde": regle.apartirde, "prefixe": regle.prefixe, "nomfichier": regle.nomfichier, "postfixe": regle.postfixe, "extensions": regle.extensions}
            dic["regles"][i] = dicRelge
            i = i + 1
        f_d.write(json.dumps(dic, indent = 4, separators = (',',':')))
        f_d.close()
        return True

    def ajouteRegle(self, r):
        self.regles.append(r)
        return True
        
    def _str__(self):
        return "Liste des règles a respecter: {0}" .format(self.regle)
        
