"""faisoms une interface graphique pour l'orientation des élèves semblable à palmares_tut 
mais juste on va ajouter une colonne pour l'orientation

"""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import side_bar_tutulaire as side_bar_tutulaire
#meme requete que palmares_tut
#from secretaire.orientation_backend import Orientation

from secretaire.eleve_back import eleve_back as Eleve
from fiche_cote_back import Fiche_cote_back as Fiche_cote

class orientation:
    
    def __init__(self,connexion):
        self.connexion=connexion['connexion']
        self.id_user=connexion['id_user']
        self.id_classe=connexion['id_classe']
        self.id_anne_scolaire=connexion['id_annee_scolaire']
        identifiant={'id_user':self.id_user,
                     'id_classe':self.id_classe,
                     'id_annee_scolaire':self.id_anne_scolaire,
                     'connexion':self.connexion}

        self.fen=Tk()
        self.fen.title("Orientation")
        self.fen.geometry("1080x600+150+0")
        self.fen.resizable(0,0)
        self.fen.configure(background='#51a596')
        self.side_bar=side_bar_tutulaire.SideBar_tutulaire(self.fen,identifiant)
        self.side_bar.place(x=0,y=0)
        self.label_titre=Label(self.fen, borderwidth=3,relief=SUNKEN,text="Orientation",font=("Sans Serif",16),fg='white',background='#091821')
        self.label_titre.place(x=300,y=0,width=500,height=80)
        self.label_classe=Label(self.fen,text="Classe",font=("Sans Serif",12),fg='white',background='#51a596')
        self.label_classe.place(x=300,y=100)
        self.label_classe1=Label(self.fen,text=self.id_classe,font=("Sans Serif",19),fg='white',background='#51a596')
        self.label_classe1.place(x=400,y=100)
        #treeview id_inscription, NOM_eleve,P1,P2,EX1,S1,P3,P4,EX2,S2,TOTAL,Orientation
        self.tree=ttk.Treeview(self.fen,columns=('Id Insc','Nom','P1','P2','EX1','S1','P3','P4','EX2','S2','TOTAL','Orientation'),show='headings')
        self.tree.heading('Id Insc',text='Id Inscription')
        self.tree.heading('Nom',text='Nom')
        self.tree.heading('P1',text='P1')
        self.tree.heading('P2',text='P2')
        self.tree.heading('EX1',text='EX1')
        self.tree.heading('S1',text='S1')
        self.tree.heading('P3',text='P3')
        self.tree.heading('P4',text='P4')
        self.tree.heading('EX2',text='EX2')
        self.tree.heading('S2',text='S2')
        self.tree.heading('TOTAL',text='TOTAL')
        self.tree.heading('Orientation',text='Orientation')
        self.tree.column('Id Insc',width=100)
        self.tree.column('Nom',width=100)
        #width=30
        self.tree.column('P1',width=30)
        self.tree.column('P2',width=30)
        self.tree.column('EX1',width=30)
        self.tree.column('S1',width=30)
        self.tree.column('P3',width=30)
        self.tree.column('P4',width=30)
        self.tree.column('EX2',width=30)
        self.tree.column('S2',width=30)
        self.tree.column('TOTAL',width=30)
        self.tree.column('Orientation',width=100)   
        self.afficher()
        
    def afficher(self):     
        
        self.tree.delete(*self.tree.get_children())
        fiche=Fiche_cote("","",0,0,0,0,0,0)
        palmares=fiche.palmares_clase_Orientation(self.connexion.get_curseur(),self.id_classe,self.id_anne_scolaire)
        for i in self.tree.get_children():
            self.tree.delete(i)
        for row in palmares:
            self.tree.insert("",'end',values=row)
        self.tree.place(x=300,y=200)