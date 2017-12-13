#Importation de module
from tkinter import *
import tkinter.font
from tkinter import messagebox
from listeRegle import *
from regle import *
from interface import inter

class Lister:
    """
       Classe qui affiche la fenetre creer
    """
    def __init__(self):
        """
           Constructeur de la fenêtre permet de définir la fenetre et ce qu'il y a dedans  
        """
        #Initialisation des règles à afficher
        self.lr = ListeRegle()
        self.lr.regles[:] = []
        self.lr.charger()
        
        #Creation de la fenetre fille
        self.fenetre = Tk()
        self.fenetre.title("Lister les règles")
        self.fenetre.geometry("%dx%d%+d%+d" %(620,280,250,200))

        #----------------------------------------------------#
        #   Creation des champs qui serons dans la fenetre   #
        #----------------------------------------------------#
        
        #Police des labels
        titrePolice = font.Font(size = 14, weight = "bold", underline = 1, slant = "italic")
        labelPolice = font.Font(size = 11, slant = "italic")

        #Titre de la fenêtre
        self.titre = Label(self.fenetre,text = "\nLister les règles\n", font = titrePolice)
        self.titre.pack()

        #Règles (avec une listbox)
        self.frame1 = Frame(self.fenetre, borderwidth = 0, relief = GROOVE)
        self.frame1.place(x = 20, y = 50)
        self.scrollY = Scrollbar(self.frame1)
        self.scrollY.pack(side = RIGHT, fill = Y)
        self.listeBox = Listbox(self.frame1, width = 85)
        self.listeBox.pack()
        self.scrollY.config(command = self.listeBox.yview)
        self.listeBox.insert(0, "Amorce      |      A partir de      |      Préfixe      |      Nom Fichier      |      Postfixe      |      Extensions")

        #Bouton (pour pourvoir selectionner une ligne de la listbox
        self.bouton1 = Button(self.fenetre, width = 73, text = "Utiliser", command = self.utiliser)
        self.bouton1.place(x = 20, y = 250)

        #Ajout de règles
        self.ajouterRegles()
        
        #Demarage de la boucle Tkinter qui s'interompt quand on ferme
        self.fenetre.mainloop()

    #-----------------------------------------#
    #   Creation des fonctions de la fenetre   #
    #-----------------------------------------#
    def ajouterRegles(self):
        """
            Fonction qui permet d inserer des règles dans la listbox
        """
        i = 1
        for regle in self.lr.regles:
            self.listeBox.insert(i, regle.amorce + "             |     " + regle.apartirde + "     |     " + regle.prefixe + "     |     " + str(regle.nomfichier) + "     |     " + regle.postfixe + "     |     " + str(regle.extensions))
            i += 1
        return True

    def utiliser(self):
        """
            Fonction qui permet de changer d'interface
        """
        if self.listeBox.curselection():
            index = self.listeBox.curselection()[0]
            rstring = self.listeBox.get(index)
            rlist = rstring.split("|")
            amorce = rlist[0].strip()
            apartirde = rlist[1].strip()
            prefixe = rlist[2].strip()
            nomfichier = rlist[3].strip()
            if nomfichier == "True":
                nomfichier = True
            postfixe = rlist[4].strip()
            extensions = rlist[5].strip()[1:-1]
            striExten =""
            for extension in extensions.split(","):
                striExten += extension.strip()[2:-1]+","
            exts = striExten[:-1]
            if exts == "*":
                exts = ""
            self.fenetre.destroy()
            main = inter.Interface(amorce, apartirde, prefixe, nomfichier, postfixe, exts)
            return True
        else:
            messagebox.showerror("Erreur", "Veuillez sélectionner un élément")
            return False


