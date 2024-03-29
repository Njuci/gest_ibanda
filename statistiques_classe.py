"""se basant sur fichier fiche_descotes.py 
je fais un design de statistiques de classe
qui affiche les statistiques de la classe
les statistiques par anne scolaire sont les suivantes:
- le nombre d'eleves
fille et garçon
- le nombre de cours
- le nombre d'echecs par cours 
- le nombre de reussites par cours et par eleve
- la moyenne de la classe par cours
- le taux de reussite par cours
- le taux d'echec par cours
Toutes ces statistiques sont affichées dans des labels
"""
from tkinter import *
from tkinter.messagebox import showerror,showinfo
from login_back import Connexion
from user_back import User_back
import cours_backend
#import fiche_descotes
import fiche_cote_back
import inscription_backend
import eleve_back
class Statistiques_classe:
    def __init__(self,connexion):
        self.connexion=connexion
        self.fen=Tk()
        self.fen.title("Statistiques de la classe")
        self.fen.geometry("800x600+300+100")
        self.fen.resizable(False,False)
        self.fen.configure(background='#51a596')
        self.label_titre=Label(self.fen, borderwidth=3,relief=SUNKEN,text="Statistiques de la classe",font=("Sans Serif",16),fg='white',background='#091821')
        self.label_titre.place(x=0,y=0,width=800,height=80)
        self.label_eleves=Label(self.fen,text="Nombre d'élèves:",font=("Times",15),fg="black",background='#51a596')
        self.label_eleves.place(x=5,y=100,width=200)
        
        self.label_filles=Label(self.fen,text="Nombre de filles:",font=("Times",15),fg="black",background='#51a596')
        self.label_filles.place(x=5,y=150,width=200)
        self.label_garcons=Label(self.fen,text="Nombre de garçons:",font=("Times",15),fg="black",background='#51a596')
        self.label_garcons.place(x=5,y=200,width=200)
        self.label_cours=Label(self.fen,text="Nombre de cours:",font=("Times",15),fg="black",background='#51a596')
        self.label_cours.place(x=5,y=250,width=200)
        self.label_echecs=Label(self.fen,text="Nombre d'échecs:",font=("Times",15),fg="black",background='#51a596')
        self.label_echecs.place(x=5,y=300,width=200)
        self.label_reussites=Label(self.fen,text="Nombre de réussites:",font=("Times",15),fg="black",background='#51a596')
        self.label_reussites.place(x=5,y=350,width=200)
        self.label_moyenne=Label(self.fen,text="Moyenne de la classe:",font=("Times",15),fg="black",background='#51a596')
        self.label_moyenne.place(x=5,y=400,width=200)
        self.label_taux_reussite=Label(self.fen,text="Taux de réussite:",font=("Times",15),fg="black",background='#51a596')
        self.label_taux_reussite.place(x=5,y=450,width=200)
        self.label_taux_echec=Label(self.fen,text="Taux d'échec:",font=("Times",15),fg="black",background='#51a596')
        self.label_taux_echec.place(x=5,y=500,width=200)
        self.remplir_labels()
    def remplir_labels(self):
        eleve=eleve_back.eleve_back("","","","","")
        eleves=eleve.get_eleves(self.connexion.curseur,1,1)
        self.label_eleves.config(text="Nombre d'élèves: "+str(eleves))
        filles=eleve.get_eleves_fille(self.connexion.curseur,1,1)
        self.label_filles.config(text="Nombre de filles: "+str(len(filles)))
        garcons=eleve.get_eleves_garcon(self.connexion.curseur,1,1)
        self.label_garcons.config(text="Nombre de garçons: "+str(len(garcons)))
        cours=cours_backend.cours_back("","","","","")
        cours=cours.get_nombre_cours_by_classe(self.connexion.curseur,1)
        self.label_cours.config(text="Nombre de cours: "+str(cours[0]))
        """fiche=fiche_cote_back.Fiche_cote_back("","","","","","","","","")
        echecs=fiche.get_echecs(self.connexion.curseur)
        self.label_echecs.config(text="Nombre d'échecs: "+str(len(echecs)))
        reussites=fiche.get_reussites(self.connexion.curseur)
        self.label_reussites.config(text="Nombre de réussites: "+str(len(reussites)))
        moyenne=fiche.get_moyenne_classe(self.connexion.curseur)
        self.label_moyenne.config(text="Moyenne de la classe: "+str(moyenne))
        taux_reussite=fiche.get_taux_reussite(self.connexion.curseur)
        self.label_taux_reussite.config(text="Taux de réussite: "+str(taux_reussite))
        taux_echec=fiche.get_taux_echec(self.connexion.curseur)
        self.label_taux_echec.config(text="Taux d'échec: "+str(taux_echec))"""
if __name__=="__main__":
    con=Connexion()
    if con.login():
        stat=Statistiques_classe(con)
        stat.fen.mainloop()
    else:
        showerror("Erreur","Erreur de connexion à la base de données")
    
