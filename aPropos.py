#Importation de module
from tkinter import *

class Apropos:
    """
       Classe qui affiche la fenetre a propos
    """
    def __init__(self):
        """
           Constructeur de la fenêtre permet de définir la fenetre et ce qu'il y a dedans  
        """
        #Creation de la fenetre fille
        self.fenetre = Toplevel()
        self.fenetre.title("A propos")
        self.fenetre.geometry("%dx%d%+d%+d" %(400,300,250,200))

        #----------------------------------------------------#
        #   Creation des champs qui serons dans la fenetre   #
        #----------------------------------------------------#

        #Police des labels
        labelPolice = font.Font(size = 11, slant = "italic", underline = 1)
        
        #Label de la fenêtre      
        self.creation = Label(self.fenetre, text = "\nCréation par :", font = labelPolice)
        self.creation.pack()

        self.creation2 = Label(self.fenetre, text = "DONATI Charlène")
        self.creation2.pack()
        
        self.date = Label(self.fenetre, text = "\nDate de création :", font = labelPolice)
        self.date.pack()

        self.date2 = Label(self.fenetre, text = "14/12/2017")
        self.date2.pack()
        
        self.version = Label(self.fenetre, text = "\nVersion 2.0", font = labelPolice)
        self.version.pack()

        self.label = Label(self.fenetre, text = "\n\nLogiciel qui permet de renommer un répertoire")
        self.label.pack()

        #Demarage de la boucle Tkinter qui s'interompt quand on ferme
        self.fenetre.mainloop()
