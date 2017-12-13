#Importation de module
from tkinter import *
import tkinter.font
from tkinter.filedialog import *
import tkinter.messagebox
from os.path import basename
from aPropos import *
from creer import *
from regle import *
from action import*
from renommage import *
from lister import *

class Interface:    
    """
       Classe qui affiche la fenetre principal
    """
    def __init__(self, am = "Aucun", ap = "", pr = "", nomf = True, pos = "", ext = "", nr = ""):
        """
           Constructeur de la fenêtre permet de définir la fenetre, le menu 
        """

        #Creation des attributs de la classe
        self.amorceTxt = am
        self.apartirdeTxt = ap
        self.prefixeTxt = pr
        self.nomFichierTxt = nomf
        self.postfixeTxt = pos
        self.extensionsTxt = ext
        self.nomRepertoire = nr
        
        #Creation de la fenetre principal
        self.fenetre = Tk()

        #Titre de la fenêtre
        self.fenetre.title("Renommage de fichier")

        #Taille de la fenêtre et sa position quand on lance l'appli
        self.fenetre.geometry("%dx%d%+d%+d" %(1000,400,250,200))

        #----------------------------------------#
        #            Creation du menu            #
        #----------------------------------------#
        
        #Creation de la barre de menu
        self.barremenu = Menu(self.fenetre)
        
        #Creation du menu "Règles"
        self.regles = Menu(self.barremenu, tearoff = 0)
        self.barremenu.add_cascade(label = "Règles", menu = self.regles)
        self.regles.add_command(label = "Lister les règles", command = self.lister)
        self.regles.add_command(label = "Crèer une règle", command = self.creer)
        self.regles.add_command(label = "Quitter", command = self.fenetre.destroy)
        
        #Creation du menu "?"
        self.aide = Menu(self.barremenu, tearoff = 0)
        self.barremenu.add_cascade(label = "?", menu = self.aide)
        self.aide.add_command(label = "A propos", command = self.aPropos)
        
        #Afficher le menu
        self.fenetre.config(menu = self.barremenu)
        
        #----------------------------------------------------#
        #   Creation des champs qui seront dans la fenetre   #
        #----------------------------------------------------#

        #Police des labels
        titrePolice = font.Font(size = 14, weight = "bold", underline = 1, slant = "italic")
        labelPolice = font.Font(size = 11, slant = "italic")
        
        #Titre de la fenêtre
        self.titre = Label(self.fenetre, text = "\nRenommer en lots", font = titrePolice)
        self.titre.pack()

        #Nom repertoire
        self.frame1 = Frame(self.fenetre,borderwidth = 0, relief = GROOVE)
        self.frame1.place(x = 200, y = 100)
        self.label1 = Label(self.frame1,text = "Nom du rèpertoire :", font = labelPolice)
        self.label1.pack(side = "left", fill = "both")
        self.string11 = StringVar()
        self.string11.set(self.nomRepertoire)
        self.saisie1 = Entry(self.frame1, width = 60, textvariable = self.string11)
        self.saisie1.pack(side = "right", fill = "both", padx = 3, pady = 3)

        #Image ne reconnait pas les png que les gif (dans version python que j'ai 
        self.image = PhotoImage(file = "../image/logo_python.gif")
        self.frame1bis = Frame(self.fenetre,borderwidth = 0, relief = GROOVE)
        self.frame1bis.place(x = 780, y = 5)
        self.canvas = Canvas(self.frame1bis, width = 200, height = 190)
        self.canvas.create_image(0, 0, anchor = NW, image = self.image)
        self.canvas.pack(side = "top", fill = "both", padx = 3, pady = 3)

        #Amorce (avec une list)
        self.frame2 = Frame(self.fenetre, borderwidth = 0, relief = GROOVE)
        self.frame2.place(x = 50, y = 200)
        self.label2 = Label(self.frame2, text = "Amorce", font = labelPolice)
        self.label2.pack(side = "top", fill = "both")
        self.optionListe = ("Aucun", "Lettre", "Chiffre")
        self.string1 = StringVar()
        self.string1.set(self.amorceTxt)
        self.list1 = OptionMenu(self.frame2, self.string1, *self.optionListe)
        self.list1.pack(side = "bottom", fill = "both")

        #Prefixe
        self.frame3 = Frame(self.fenetre, borderwidth = 0,relief = GROOVE)
        self.frame3.place(x = 150, y = 200)
        self.label3 = Label(self.frame3, text = "Préfixe", font = labelPolice)
        self.label3.pack(side = "top", fill = "both")
        self.string3 = StringVar()
        self.string3.set(self.prefixeTxt)
        self.saisie2 = Entry(self.frame3, width = 20, textvariable = self.string3)
        self.saisie2.pack(side = "bottom", fill = "both")

        #Nom fichier (avec radio button)
        self.frame4 = Frame(self.fenetre, borderwidth = 0, relief = GROOVE)
        self.frame4.place(x = 280, y = 200)
        self.label4 = Label(self.frame4, text = "Nom du fichier", font = labelPolice)
        self.label4.pack(side = "top", fill = "both")
        self.valeur1 = StringVar()
        self.valeur2 = StringVar()
        if(self.nomFichierTxt != True):
            self.valeur2.set(self.nomFichierTxt)
        self.choix1 = Radiobutton(self.frame4, text = "Nom Original", variable = self.valeur1, value = 1)
        self.choix1.pack()
        self.frame5= Frame(self.frame4, borderwidth = 0, relief = GROOVE)
        self.frame5.pack(side = LEFT)
        self.choix2 = Radiobutton(self.frame5, variable = self.valeur1, value = 2)
        self.entryChoix = Entry(self.frame5, textvariable = self.valeur2)
        self.choix2.pack(side = LEFT)
        if(self.nomFichierTxt == True):
            self.choix1.select()
        else:
            self.choix2.select()
        self.entryChoix.pack(side = RIGHT)

        #Postfix
        self.frame6 = Frame(self.fenetre, borderwidth = 0, relief = GROOVE)
        self.frame6.place(x = 480,y = 200)
        self.label5 = Label(self.frame6, text = "Postfix", font = labelPolice)
        self.label5.pack(side = "top", fill = "both")
        self.string6 = StringVar()
        self.string6.set(self.string6)
        self.saisie3 = Entry(self.frame6, width = 20, textvariable = self.string6)
        self.saisie3.pack(side = "bottom", fill = "both")

        #Extension concernee
        self.frame7 = Frame(self.fenetre, borderwidth = 0, relief = GROOVE)
        self.frame7.place(x = 630, y = 200)
        self.label6 = Label(self.frame7, text = "Extension concernée (.gif, .jpg, ...)", font = labelPolice)
        self.label6.pack(side = "top", fill = "both")
        self.string7 = StringVar()
        self.string7.set(self.string7)
        self.saisie4 = Entry(self.frame7, width = 20, textvariable = self.string7)
        self.saisie4.pack(side = "bottom", fill = "both")

        #A partir de
        self.frame8 = Frame(self.fenetre, borderwidth = 0, relief = GROOVE)
        self.frame8.place(x = 50, y = 300)
        self.label7 = Label(self.frame8, text = "A partir de", font = labelPolice)
        self.label7.pack(side = "top", fill = "both")
        self.string8 = StringVar()
        self.string8.set(self.apartirdeTxt)
        self.saisie5 = Entry(self.frame8, width = 20, textvariable = self.string8)
        self.saisie5.pack(side = "bottom", fill = "both")

        #Renommer (button)
        self.bouton2 = Button(self.fenetre, text = "Renommer", width = 20, command = self.rename)
        self.bouton2.place(x = 630, y = 310)

        #Demarage de la boucle Tkinter qui s'interompt quand on ferme
        self.fenetre.mainloop()  

    #-----------------------------------------#
    #   Creation des fonctions de la fenetre   #
    #-----------------------------------------# 
    
    def aPropos(self):
        """
            Fonction qui permet d'appeler l'interface a propos
        """
        Apropos()
        return True

    def creer(self):
        """
            Fonction qui permet d'appeler l'interface creer
        """
        self.fenetre.destroy()
        Creer()
        return True

    def lister(self):
        """
            Fonction qui permet d'appeler l'interface lister
        """
        self.fenetre.destroy()
        Lister()
        return True

    def set_nomFichier(self):
        """
           Pas encore totalement fini 
        """
        #Récupération de la valeur dans nom rèpertoire
        nomRepert = self.saisi1.get()
        
        #Récuperation d'un fichier SANS son extension  
        nomFichier = os.path.splitext(basename(nomRepert))[0]
 
        #Récuperation de l'extension d'un fichier 
        chemin, extension = os.path.splitext(nomRepert)

        #Récuperation de la valeur radiobouton
        choix = self.valeur1.get()

        #Récupération du champ nom fichier
        choixNomFicher = self.entryChoix.get()


        #Si le radio bouton est sur nom origne on fait le code du if sinon on fait le code du else
        if choix == "1":
            #Permet de désactiver le champ de l'autre radioButton et de le cleaner
            self.entryChoix.delete(0, END)
            self.entryChoix.config(state = "disabled")
            messagebox.showinfo("Mot changer ", set_preFix())
        else:
            self.entryChoix.config(state = "normal")
            print(choixNomFicher)

    def rename(self):       
        """
           Fonction qui permet de renommer un fichier quand a cliquer sur le bouton
        """
        repertoire = self.saisie1.get()
        prefixe = self.saisie2.get()
        postfixe = self.saisie3.get()
        amorce = self.string1.get()
        apartirde = self.saisie5.get()

        if len(apartirde) <= 3 and ((amorce == "Chiffre" and (apartirde.isnumeric() or apartirde == "")) or (amorce == "Lettre" and (apartirde.isalpha() or apartirde == ""))) or amorce == "Aucun":
            if amorce == "Chiffre" and apartirde =="":
                apartirde = 1
            if amorce == "Lettre" and apartirde =="":
                apartirde = "A"
            if self.valeur1.get() == "1":
                nomFichier = True
            if self.valeur1.get() == "2":
                nomFichier = self.valeur2.get()
            extensions = self.saisie4.get().split(",")

            #Instanciation d'une Regle
            regle = Regle(amorce, apartirde, prefixe, nomFichier, postfixe)
            for i in extensions:
                regle.ajoutExtension(i)
            
            #Instanciation d'une Action
            action = Action(repertoire, regle)
            
            #Appel de la mèthode Action::simule()
            simule = action.simule()
        
            #Affichage de la simulation dans un message Box
            if(repertoire != ""):
                showinfo("Simulation", simule())
                return True
        else:
            showinfo("Simulation", "Veuillez saisir un rèpertoire")
        return False

#Instanciation de la classe 
inter = Interface()
