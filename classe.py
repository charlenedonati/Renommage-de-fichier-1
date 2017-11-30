import os

ext = ["txt","docx"]
alphabet= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

#-------------------------------------------------------------------------
#                               Classe REGLE
#-------------------------------------------------------------------------

class Regle:
    
    def __init__(self):#, a, ap, nF, pre, post, ext = []):
        self.amorce = ""
        self.apartirDe = ""
        self.nomFichier = False
        
        self.preFixe = "JKLMNOPQ"
        self.postFixe = "JKLMNOPQ"
        self.extension = ""
        
    #Fonction get qui permet de recuperer la valeur des self hors de la classe
    def get_amorce(self):
        return self.amorce

    def get_apartirDe(self):
        return self.apartirDe

    def get_nomFichier(self):
        return self.nomFichier

    def get_preFixe(self):
        return self.preFixe

    def get_postFixe(self):
        return self.postFixe

    def get_extension(self):
        return self.extension    

    #Fonction set 
    def set_amorce(self,value):
        #si les proprietes ne sont pas initialement remplies, ils le seront ici dans les setter qui attribue le type d amorce, rien, une lettre ou un chiffre
        if valeur == "" :
            self.amorce = ""
            print("tu n'as rien rentré")
        #test si c'est une lettre
        if value.isalpha(): 
            position = alphabet.find(valeur)
            for fichier in RecupererTousLesFichiersDuDossier():
                print(position)
                print(alphabet[position])
            
    #Fonction setter qui attribue pour un chiffre à partir de combien de chiffre
    def set_apartirDe(self, valeur):
        self.apartirDe = valeur

    #Fonction setter qui attibue le nom original ou modifier
    def set_nomFichier(self, valeur):
        #Si la valeur est vrai on saisi le nom personaliser sinon on prend le nom original 
        if valeur == True:
            saisi = str(input("saisissez le nom du fichier personnaliser : "))
        else:
            saisi = "fichier original"
        print("l utilisateur a choisi : " + saisi)
        self.nomFichier = saisi

    #Fonction setter qui attribue le postFixe
    def set_postFixe(self, valeur):
        '''for lettre in self.postfixe :
            print(lettre+suffixe)''' 
        
    #Fonction setter qui attribue le preFixe
    def set_preFixe(self, valeur):
        #à saisir dans l'interface      
        preFixe = "ack"
        
        for lettre in self.preFixe :
            print(preFixe+lettre)

    #Fonction setter qui selon les extension saisi dans l interface seperer par une virgule 
    def set_extension(self, valeur):
        self.extension= valeur
    
        
    def __str__(self):
        return "les règles a respecter : \nAmorce: {0},\nNom du fichier: {1},\nPostfixe: {2},\nPrefixe: {3},\nExtension: {4} " .format(self.amorce, self.nomFichier, self.postFixe, self.preFixe, self.extension)
    

#-------------------------------------------------------------------------
#                               Classe LISTEREGLE
#-------------------------------------------------------------------------
class ListeRegle:
    
    def __init__(self):
        self.regle = r

    def get_regles(self):
        return self.regle

    #Fonction qui recupere les règles
    def setListe(self, valeur):
        self.regle = liste 

    #Fonction qui permet d'afficher les règles contenu dans le fichier .ini 
    def charger(self):
        with open('ListRegle.ini', 'r') as f:
            maList = [line.strip() for line in f]
        print(maList)
    

    #Fonction qui permet de sauvegarder les règles dans un fichier .ini
    def sauvegarder(self):
        file = open("ListRegle.ini","a")
        for maRegle in self.regle:
            file.write(str(maRegle)+"\n")
        file.close()
        

    def _str__(self):
        return "Liste des règles a respecter: {0}" .format(self.regle)
        

#-------------------------------------------------------------------------
#                               Classe ACTION
#-------------------------------------------------------------------------

class Action:
    def __init__(self):
        self.nomDuRepertoire = ""
        self.regle = ""

    def get_nomDuRepertoire(self):
        return self.nomDuRepertoire

    def get_regle(self):
        return self.regle

    def set_nomDuRepertoire(self, valeur):
        self.nomDuRepertoire = valeur

    def set_regle(self, valeur):
        self.regle = valeur

    def __str__(self):
        return "Certain fichier du dossier {0}, seron renomer\navec la règle suivante : {1}" .format(self.nomDuRepertoir,self.regle)

#-------------------------------------------------------------------------
#                               Classe RENOMMAGE
#-------------------------------------------------------------------------
#Fonctionne pas encore
'''
#Classe renommage qui hérite de la classe action
class Renommage(Action):
    def __init__(self):
        Action.__init__(self,nomDuRepertoire,regle)
        self.mot = "gg"
        
    def __str__(self):
        return "{0}" .format(self.mot)

    #Fonction pas

    def RecupererTousLesFichiersDuDossierl(self):
    ## os.listdir("path") permet de récup la list des fichiers dans le dossier
        path="C:/Users/Donati/Documents/M2I/L3/Cours/Python/Exo"
        dirs = os.listdir( path )
        listeFichier = []

        nomComplet = os.path.join(path, "test.txt")
        nomComplet2 = os.path.join(path, "test2.txt")
        
        #Affiche tous les fichiers du dossier python
        for file in dirs:
           listeFichier.append(file)
        
        for fichier in listeFichier:
            #os.rename(nomComplet, nomComplet2)
            return (listeFichier)

    
def RecupererTousLesFichiersDuDossier():
        path="C:/Users/Donati/Documents/M2I/L3/Cours/Python/Exo"
        dirs = os.listdir( path )
        listeFichier = []

        nomComplet = os.path.join(path, "test.txt")
        nomComplet2 = os.path.join(path, "test2.txt")
        
        #Affiche tous les fichier du dossier python
        for file in dirs:
           listeFichier.append(file)
        
        for fichier in listeFichier:
            return (listeFichier)
'''


#-------------------------------------------------------------------------
#                               Objet
#-------------------------------------------------------------------------
     
r = Regle()   
lr = ListeRegle()
#re = Renommage()
a = Action()








    


