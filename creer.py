#Importation de module
from tkinter import *
import tkinter.font
from listeRegle import *
from regle import *

class Creer:
    """
       Classe qui affiche la fenetre creer
    """
    def __init__(self):
        """
           Constructeur de la fenêtre permet de définir la fenetre et ce qu'il y a dedans  
        """
        #Creation de la fenetre fille
        self.fenetre = Tk()
        self.fenetre.title("Création de règle")
        self.fenetre.geometry("%dx%d%+d%+d" %(1000,400,250,200))

        #----------------------------------------------------#
        #   Creation des champs qui serons dans la fenetre   #
        #----------------------------------------------------#
        
        #Police des labels
        titrePolice = font.Font(size = 14, weight = "bold", underline = 1, slant = "italic")
        labelPolice = font.Font(size = 11, slant = "italic")

        #Titre de la fenêtre
        self.titre = Label(self.fenetre,text = "\nCréer une règle", font = titrePolice)
        self.titre.pack()

        #Amorce (avec une list)
        self.frame2 = Frame(self.fenetre, borderwidth = 0, relief = GROOVE)
        self.frame2.place(x = 50, y = 200)
        self.label2 = Label(self.frame2, text = "Amorce", font = labelPolice)
        self.label2.pack(side = "top", fill = "both")
        self.optionListe = ("Aucun", "Lettre", "Chiffre")
        self.string1 = StringVar()
        self.string1.set(self.optionListe[0])
        self.list1 = OptionMenu(self.frame2, self.string1, *self.optionListe)
        self.list1.pack(side = "bottom", fill = "both")

        #Préfixe
        self.frame3 = Frame(self.fenetre, borderwidth = 0,relief = GROOVE)
        self.frame3.place(x = 150, y = 200)
        self.label3 = Label(self.frame3, text = "Préfixe", font = labelPolice)
        self.label3.pack(side = "top", fill = "both")
        self.saisie2 = Entry(self.frame3, width = 20)
        self.saisie2.pack(side = "bottom", fill = "both")

        #Nom fichier (avec radio button)
        self.frame4 = Frame(self.fenetre, borderwidth = 0, relief = GROOVE)
        self.frame4.place(x = 280, y = 200)
        self.label4 = Label(self.frame4, text = "Nom du fichier", font = labelPolice)
        self.label4.pack(side = "top", fill = "both")
        self.valeur1 = StringVar()
        self.valeur2 = StringVar()
        self.choix1 = Radiobutton(self.frame4, text = "Nom Original", variable = self.valeur1, value = 1)
        self.choix1.pack()
        self.choix1.select()
        self.frame5= Frame(self.frame4, borderwidth = 0, relief = GROOVE)
        self.frame5.pack(side = LEFT, padx = 5, pady = 5)
        self.choix2 = Radiobutton(self.frame5, variable = self.valeur1, value = 2)
        self.entryChoix = Entry(self.frame5, textvariable = self.valeur2)
        self.choix2.pack(side = LEFT)
        self.entryChoix.pack(side = RIGHT)

        #PostFixe
        self.frame6 = Frame(self.fenetre, borderwidth = 0, relief = GROOVE)
        self.frame6.place(x = 480,y = 200)
        self.label5 = Label(self.frame6, text = "Postfixe", font = labelPolice)
        self.label5.pack(side = "top", fill = "both")
        self.saisie3 = Entry(self.frame6, width = 20)
        self.saisie3.pack(side = "bottom", fill = "both")

        #Extension concernée
        self.frame7 = Frame(self.fenetre, borderwidth = 0, relief = GROOVE)
        self.frame7.place(x = 630, y = 200)
        self.label6 = Label(self.frame7, text = "Extension concernée (.gif, .jpg)", font = labelPolice)
        self.label6.pack(side = "top", fill = "both")
        self.saisie4 = Entry(self.frame7, width = 20)
        self.saisie4.pack(side = "bottom", fill = "both")

        #A partir de
        self.frame8 = Frame(self.fenetre, borderwidth = 0, relief = GROOVE)
        self.frame8.place(x = 50, y = 300)
        self.label7 = Label(self.frame8, text = "A partir de")
        self.label7.pack(side = "top", fill = "both")
        self.saisie5 = Entry(self.frame8, width = 20)
        self.saisie5.pack(side = "bottom", fill = "both")

        #Renommer (button)
        self.bouton1 = Button(self.fenetre, text = "Créer", width = 20, command = self.creer)
        self.bouton1.place(x = 630, y = 310)
        
        #Demarage de la boucle Tkinter qui s'interompt quand on ferme
        self.fenetre.mainloop()

    #-----------------------------------------#
    #   Creation des fonction de la fenetre   #
    #-----------------------------------------#
    
    def creer(self):
        """
            Fonction qui permet de créer une règle et de la sauvegarder dans le fichier
        """
        amorce = self.string1.get()
        apartirde = self.saisie5.get()
        prefix = self.saisie2.get()
        if len(apartirde) <= 3 and ((amorce == "Chiffre" and (apartirde.isnumeric() or apartirde == "")) or (amorce == "Lettre" and (apartirde.isalpha() or apartirde == ""))) or amorce == "Aucun":
            if self.valeur1.get() == "1":
                nomFichier = True
            if self.valeur1.get() == "2":
                nomFichier = self.valeur2.get()
            postfixe = self.saisie3.get()
            extensions = self.saisie4.get()
            stri = "Amorce: " + amorce + "\nA partir de : " + apartirde + "\nPrefix: " + prefix + "\nNom Fichier : " + str(nomFichier) + "\nPostfixe: " + postfixe + "\nExtensions: " + extensions
            question = messagebox.askyesno("Création de la règle", "Etes-vous sur de vouloir créer la règle avec les attributs suivants : \n" + stri, icon = "question")
            if question == True:
                lr = ListeRegle()
                lr.regles[:] = []
                lr.charger()
                r = Regle(amorce, apartirde, prefix, nomFichier, postfixe)
                for ext in extensions.split(','):
                    r.ajoutExtension("*"+ext)
                lr.ajouteRegle(r)
                lr.sauvegarder()
                r.extensions[:] = []
                messagebox.showinfo("Création de la règle","Règle créée avec succès !")
                self.fenetre.destroy()
                inter.interface(amorce, apartirde, prefix, nomFichier, postfixe, extensions)
            else:
                return
        else:
            messagebox.showerror("Erreur", "L'amorce et A partir de ne sont pas cohérents.")
            return
