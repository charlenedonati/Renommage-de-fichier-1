#Importation de module
from tkinter import *
import os
from glob import glob
from os.path import join


class Action:
    def __init__(self, nomRep, regle):
        self.nomRepertoire = nomRep
        self.regle = regle

    def get_nomRepertoire(self):
        return self.nomRepertoire
    
    def set_nomRepertoire(self, n):
        self.nomRepertoire = n

    def get_regle(self):
        return self.regle

    def set_regle(self, r):
        self.regle = r

    def __str__(self):
        return "Certain fichier du dossier {0}, seron renomer\navec la règle suivante : {1}" .format(self.nomRepertoir, self.regle)

    def simule(self):
        """
           Fonction qui permet de simuler le renommage du fichier
        """
        originalNom = ""
        extension = ""
        changer = ""
        pre = ""
        post = ""
        nomF = ""
        stri = ""
        fichiers = []
        dictRetour = {} 
        try:
            if self.regle.extensions != [""]:
                for ext in self.regle.extensions:
                    fichiers.extend(glob(join(self.nomRepertoire, ext)))
                #Remise à zéro de la liste des extensions pour éviter les doublons
                self.regle.extensions[:] = []
            else:
                fichiers[:] = []
                fichiers = os.listdir(self.nomRepertoire)
            i = 1
            if fichiers != "":
                nextAmorce = ""
                for fichier in fichiers:
                    if os.path.isfile(fichier):
                        originalNom = os.path.basename(fichier).split(".")[0]
                        repertoire = os.path.dirname(fichier)
                        extension = os.path.splitext(fichier)[1]
                        stri += " - Nom du fichier original : " + originalNom + extension + " | Nouveau Nom : "
                        
                        if nextAmorce == "":
                            amorce = self.regle.apartirde
                            nextAmorce = amorce
                        else:
                            amorce = self.getAmorce(nextAmorce, self.regle.amorce)
                            nextAmorce = amorce
                        stri += amorce
                        if self.regle.prefixe != "":
                            stri += self.regle.prefixe
                            pre = self.regle.prefixe
                            
                        if self.regle.nomfichier != True:
                            stri += self.regle.nomfichier + "_" + str(i)
                            nomF = self.regle.nomfichier + "_" + str(i)
                            i += 1
                        else:
                            stri += originalNom
                            nomF = originalNom                    

                        if self.regle.postfixe != "":
                            stri += self.regle.postfixe + extension + "\n"
                            post = self.regle.postfixe
                        else:
                            stri += extension + "\n"
                        ancienNom = repertoire + "/" + originalNom + extension
                        nouveauNom = repertoire + "/" + amorce + pre + nomF + post + extension
                        dictRetour[ancienNom] = nouveauNom 

                if stri == "":
                    stri = "Erreur, une ou plusieurs extensions saisies ne sont pas dans le répertoire"
                return (stri, dictRetour)
            else:
                showinfo("Erreur""Erreur : Pas de fichiers dans ce répertoire")
        except IOError:
            return "Erreur : dossier non trouvable"

    def getAmorce(self, apartirde, typeA):
        """
           Fonction qui permet de creer une amorce de chiffre
        """
        apartirde = apartirde.upper()
        #If qui permet de changer des lettre en chiffre et inversement
        if apartirde == "A":
            typeA = "Lettre"
        if apartirde == "001":
            typeA = "Chiffre"
        if typeA == "Aucun":
            amorce= ""

        #If qui permet de calculer l'amorce pour  les chiffres
        if typeA == "Chiffre":
            if int(apartirde) == 999:
                amorce = "A"
            else:
                amorce = '{:03}'.format((int(apartirde) + 1))

        #If qui permet de calculer l'amorce pour les lettres
        if typeA == "Lettre":
            amorce = apartirde
                                
            for i in range(len(apartirde)):
                if i == 0:
                    lettre = amorce[-i-1]
                else:
                    lettre = amorce[-i]
                if amorce != "ZZZ":
                    if lettre != "Z":
                        lettre = chr(int(ord(lettre)) + 1)
                        amorceList = list(amorce)

                        if i == 0:
                            amorceList[-i-1] = lettre
                        else:
                            amorceList[-i] = lettre
                        amorce = ""
                        for a in amorceList:
                            amorce += a
                        break
                    
                    else:
                        if len(amorce) == 3:
                            if amorce[2] == "Z":
                                if amorce[1] == "Z":
                                    amorce = chr(int(ord(amorce[0])+1)) + "AA"
                                else:
                                    amorce = amorce[0] + chr(int(ord(amorce[1]) + 1)) + "A"
                            else:
                                amorce = amorce[0:1] + chr(int(ord(amorce[2]) + 1)) + "A"
                        elif len(amorce) == 2:
                            if amorce[1] == "Z":
                                if amorce == "ZZ":
                                    amorce = "AAA"
                                else:
                                    amorce = chr(int(ord(amorce[0]) + 1)) + "A"
                            else:
                                amorce = amorce[0] + chr(int(ord(amorce[1]) + 1))
                        else:
                            if amorce == "Z":
                                amorce = "AA"
                            else:
                                amorce = chr(int(ord(amorce) + 1))
                        break
                    
                else:
                    amorce = "001"
                    break

        return amorce
