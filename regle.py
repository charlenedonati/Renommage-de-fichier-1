#Importation de module

class Regle:
    """
       Classe pour les règles
    """
    def __init__(self, amorce, apartirde, prefixe, nomfichier, postfixe, extensions = []):
        self.amorce = amorce
        self.apartirde = apartirde
        self.prefixe = prefixe
        self.nomfichier = nomfichier
        self.postfixe = postfixe
        self.extensions = extensions

    def __str__(self):
        return "Renomage du fichier en..."

    def get_amorce(self):
        return self.amorce
    
    def set_amorce(self, a):
        self.amorce = a
        
    def get_apartirde(self):
        return self.apartirde

    def set_apartirde(self, a):
        self.apartirde = a
        
    def get_prefix(self):
        return self.prefixe

    def set_prefix(self, p):
        self.prefixe = p
        
    def get_nomFichier(self):
        return self.nomfichier

    def set_nomFichier(self, n):
        self.nomfichier = n

    def get_postfixe(self):
        return self.postfixe
    
    def set_postfixe(self, p):
        self.postfixe = p

    def get_extensions(self):
        return self.extensions
    
    def set_extensions(self, e):
        self.extensions = e

    def ajoutExtension(self, ext):
        """
           Fonction qui permet d'ajouter des extensions
        """
        self.extensions.append(ext)
        return True
