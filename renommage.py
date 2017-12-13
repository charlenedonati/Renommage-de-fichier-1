#Importation de module
from tkinter import *
import os
from action import *
from regle import *

#Classe renommage qui hérite de la classe action
class Renommage(Action):
    def __init__(self, n, r):
        Action.__init__(self, n, r)

    def renommer(self):
        """
           Fonction qui permet de renommer un fichier
        """
        simulation = self.simule()
        message = simulation[0]
        dict = simulation[1]
        if message != "Erreur, une ou plusieurs extensions saisies ne sont pas dans le répertoire":
            question = messagebox.askyesno("Simulation du renommage", "Etes-vous sur de vouloir renommer ces fichiers : \n\n" + message, icon = "question")
            if question == True:
                try:
                    for original, modif in dict.items():
                        os.rename(original, modif)
                    messagebox.showinfo("Validation", "Vos fichiers ont été renommés avec succès !")
                except OSError:
                    messagebox.showerror("Erreur", "Il y a eu une erreur lors du renommage !")
            return True
        else:
            messagebox.showerror("Erreur", message)       
            return False
        
    def __str__(self):
        return "Classe de renommage du fichier"
