#Importation de module
from tkinter import *
import tkinter as tk
from tkinter import ttk

class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)

        #------------------------------------------------------------------------------------
        #           Création du menu
        #------------------------------------------------------------------------------------
         
        #Creation de la barre de menu
        self.barremenu = tk.Menu(self.master)

        #Creation du menu "Règles"
        self.regles = tk.Menu(self.barremenu, tearoff = 0)
        self.barremenu.add_cascade(label = "Règles", underline = 0, menu = self.regles)
        self.regles.add_command(label = "Lister les règles", underline = 0, command = self.lister)
        self.regles.add_command(label = "Créer une règle", underline = 0, command = self.creer)
        self.regles.add_command(label = "Quitter", underline = 0, command = self.quitter)

        #Creation du menu "?"
        self.aide = tk.Menu(self.barremenu, tearoff = 0)
        self.barremenu.add_cascade(label = "?", underline = 0, menu = self.aide)

        #Afficher le menu
        self.master.config(menu = self.barremenu)

    #---------------------------------------------------------------------------------------
    #           Fonction que le menu renvoi
    #---------------------------------------------------------------------------------------
         
    #Premier onglet du menu
    def lister(self):
        fenetreLister = tk.Tk()
        fenetreLister.title("Lister les règles")
        fenetreLister.geometry("%dx%d%+d%+d" %(1000,400,250,200))

    def creer(self):
        fenetreLister = tk.Tk()
        fenetreLister.title("Creation d'un règle")
        fenetreLister.geometry("%dx%d%+d%+d" %(1000,400,250,200))
        
    def quitter(self):
        self.master.destroy()

    #Deuxième onglet du menu
    def apropos(self):
        fenetreLister = tk.Tk()
        fenetreLister.title("A propos")
        fenetreLister.geometry("%dx%d%+d%+d" %(1000,400,250,200))

#------------------------------------------------------------------------------------------
#           Fonction qui renvoi les boutons du menu 
#------------------------------------------------------------------------------------------
         
def boutons():

    #Police des labels
    titrePolice = tk.font.Font(size = 14, weight = "bold", underline = 1, slant = "italic")
    labelPolice = tk.font.Font(size = 11, slant = "italic")
    
    #Titre de la fenêtre
    frame = Frame(fenetre, borderwidth = 0, relief = GROOVE)
    frame.place(x = 450, y = 10)
    titre1 = Label(frame, text = "Renommer en lots", font = titrePolice)
    titre1.pack(side = "top")


    #Premiere ligne de la fenêtre
    frame2 = Frame(fenetre, borderwidth = 0, relief= GROOVE)
    frame2.place(x = 300, y = 70)
    label_nomRepe = Label(frame2, text = "Nom du répertoire", font = labelPolice)
    label_nomRepe.pack(side = "left")

    frame3 = Frame(frame2, borderwidth = 0, relief= GROOVE)
    frame3.place(x = 300, y = 10)
    var_text = StringVar()
    text_nomRepe = Entry(frame2, textvariable = var_text, width= 40)
    text_nomRepe.pack(padx = 10)

    frame4 = Frame(fenetre, borderwidth = 0, relief= GROOVE)
    frame4.place(x = 750, y = 65)
    bouton_imagePerso = Button(frame4, text= "Image personnalisée \n de votre logiciel", font = labelPolice, width = 25, height = 3)
    bouton_imagePerso.pack(side = "right")


    #deuxième ligne de la fenêtre    
    frame5 = Frame(fenetre, borderwidth = 0, relief= GROOVE)
    frame5.place(x = 40, y = 130)
    label_amorce = Label(frame5, text = "Amorce", font = labelPolice)
    label_amorce.pack(side = "left")

    frame6 = Frame(fenetre, borderwidth = 0, relief= GROOVE)
    label_preFixe = Label(frame5, text = "Préfixe", font = labelPolice)
    label_preFixe.pack(side = "left", padx = 32)

    frame7 = Frame(fenetre, borderwidth = 0, relief= GROOVE)
    label_nomFich = Label(frame5, text = "Nom du fichier", font = labelPolice)
    label_nomFich.pack(side = "left", padx = 30)

    frame8 = Frame(fenetre, borderwidth = 0, relief= GROOVE)
    label_postFixe = Label(frame5, text = "Postfixe", font = labelPolice)
    label_postFixe.pack(side = "left", padx = 30)
    
    frame9 = Frame(fenetre, borderwidth = 0, relief= GROOVE)
    label_extension = Label(frame5, text = "Extension concernée", font = labelPolice)
    label_extension.pack(side = "left", padx = 50)

    
    #Troisième ligne de la fenêtre
    var_case = IntVar()
    
    frame10 = Frame(fenetre, borderwidth = 0, relief = GROOVE)
    frame10.place(x = 20, y = 150)
    radio_aucune = Radiobutton(frame10, text = "Aucune", variable = var_case, value = 1)
    radio_aucune.pack(side = "left")

    frame11 = Frame(fenetre, borderwidth = 0, relief = GROOVE)
    frame11.place(x = 20, y = 175)
    radio_lettre = Radiobutton(frame11, text = "Lettre", variable = var_case, value = 2)
    radio_lettre.pack(side = "left")

    frame12 = Frame(fenetre, borderwidth = 0, relief = GROOVE)
    frame12.place(x = 20, y = 200)
    radio_chiffre = Radiobutton(frame12, text = "Chiffre", variable = var_case, value = 3)
    radio_chiffre.pack(side = "left")

    frame13 = Frame(fenetre, borderwidth = 0, relief = GROOVE)
    frame13.place(x = 120, y = 150)
    var_text2 = StringVar()
    text_preFixe = Entry(frame13, textvariable = var_text2, width= 10)
    text_preFixe.pack(side = "left")

    frame14 = Frame(fenetre, borderwidth = 0, relief = GROOVE)
    frame14.place(x = 200, y = 150)
    radio_nomOriginal = Radiobutton(frame14, text = "Nom original", variable = var_case, value = 4)
    radio_nomOriginal.pack(side = "left")

    frame15 = Frame(fenetre, borderwidth = 0, relief = GROOVE)
    frame15.place(x = 200, y = 175)
    radio_nomFichier = Radiobutton(frame15, variable = var_case, value = 5)
    radio_nomFichier.pack(side = "left")

    frame16 = Frame(fenetre, borderwidth = 0, relief = GROOVE)
    var_text3 = StringVar()
    text_nomFich = Entry(frame15, textvariable = var_text3, width= 20)
    text_nomFich.pack(side = "left")

    frame17 = Frame(fenetre, borderwidth = 0, relief = GROOVE)
    frame17.place(x = 380, y = 150)
    var_text4 = StringVar()
    text_postFixe = Entry(frame17, textvariable = var_text4, width= 20)
    text_postFixe.pack(side = "left")

    frame18 = Frame(fenetre, borderwidth = 0, relief= GROOVE)
    frame18.place(x = 547, y = 150)
    var_text5 = StringVar()
    text_extension = Entry(frame18, textvariable = var_text5, width= 20)
    text_extension.pack(side = "right")


    #Quatrième ligne de la fenêtre
    frame19 = Frame(fenetre, borderwidth = 0, relief= GROOVE)
    frame19.place(x = 20, y = 250)
    label_aPartir = Label(frame19, text = "A partir de", font = labelPolice)
    label_aPartir.pack(side = "bottom")

    frame20 = Frame(fenetre, borderwidth = 0, relief= GROOVE)
    frame20.place(x = 20, y = 270)
    var_text6 = StringVar()
    text_aPartir = Entry(frame20, textvariable = var_text6, width= 10)
    text_aPartir.pack(side = "bottom")

    frame21 = Frame(fenetre, borderwidth = 0, relief= GROOVE)
    frame21.place(x = 580, y = 270)
    bouton_renommer = Button(frame21, text= "Renommer", font = labelPolice, width = 10, height = 2)
    bouton_renommer.pack(side = "bottom")
    
#------------------------------------------------------------------------------------------
#           Création de la fenêtre principal
#------------------------------------------------------------------------------------------
 
#Creation de la fenêtre
fenetre = tk.Tk()

#Titre de la fenêtre
fenetre.title("Renommage de fichier")
app = Application(fenetre)

#Taille de la fenêtre et sa position quand on lance l'appli
fenetre.geometry("%dx%d%+d%+d" %(1000,330,200,200))

#Appelle de la fonction bouton
boutons()

#Démarage de la boucle Tkinter qui s'interompt quand on ferme
fenetre.mainloop()
