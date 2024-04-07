"""un combox qui contient les id_inscription des eleves inscrits dans une classe pour une annee scolaire donnee
et un tableau qui contient les cotes des eleves inscrits dans une classe pour une annee scolaire donnee
les cotes sont les cotes des eleves inscrits dans une classe pour une annee scolaire donnee et sont affiche`es dans un tableau en fonction de l'id_inscription de l'eleve
et en se basant sur les cours de la classe pour une annee scolaire donnee
sidebar tiutulaire


"""

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror,showinfo
from secretaire.eleve_back import eleve_back as Eleve
#from secretaire.inscription_backend import inscription_back as Inscription
from tkinter.ttk import Treeview
from tkinter import messagebox
import side_bar_tutulaire as side_bar_tutulaire
from cours_backend import cours_back as Cours
from fiche_cote_back import Fiche_cote_back as Fiche_cote
from secretaire.anne_scolaire_back import AnneScolaire
from cours_backend import cours_back as cours
class bulletin:
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
        self.fen.title("Bulletins")
        self.fen.geometry("900x900+150+0")
        self.fen.resizable(0,0)
        self.fen.configure(background='#51a596')
        self.side_bar=side_bar_tutulaire.SideBar_tutulaire(self.fen,identifiant)
        self.side_bar.place(x=0,y=0)
        self.label_titre=Label(self.fen, borderwidth=3,relief=SUNKEN,text="Bulletins",font=("Sans Serif",16),fg='white',background='#091821')
        self.label_titre.place(x=300,y=0,width=500,height=80)
        self.label_classe=Label(self.fen,text="Classe",font=("Sans Serif",12),fg='white',background='#51a596')
        self.label_classe.place(x=300,y=100)
        self.label_classe1=Label(self.fen,text=self.id_classe,font=("Sans Serif",19),fg='white',background='#51a596')
        self.label_classe1.place(x=400,y=100)
        self.label_eleve=Label(self.fen,text="Eleve",font=("Sans Serif",12),fg='white',background='#51a596')
        self.label_eleve.place(x=300,y=150)
        self.combo_eleve=ttk.Combobox(self.fen,font=("Sans Serif",12))
        self.combo_eleve.place(x=400,y=150)
        self.bouton_afficher=Button(self.fen,text='Afficher', background='#FF4500',font=("Times",16),fg='white',command=self.afficher)
        self.tree=ttk.Treeview(self.fen,columns=('Cours','Periode 1','Periode 2','Examen1','Semestre1','Periode 3','Periode 4','Examen2','Semestre2','Total'),show='headings')
        
        #heding of tree
        self.tree.heading('Cours', text='Cours')
        self.tree.heading('Periode 1', text='P1')
        self.tree.heading('Periode 2', text='P2')
        self.tree.heading('Examen1', text='Examen')
        self.tree.heading('Semestre1', text='Semestre')
        self.tree.heading('Periode 3', text='P3')
        self.tree.heading('Periode 4', text='P4')
        self.tree.heading('Examen2', text='Examen')
        self.tree.heading('Semestre2', text='Semestre')
        self.tree.heading('Total', text='Total')
        #column
        self.tree.column('Cours', width=100)
        self.tree.column('Periode 1', width=50)
        self.tree.column('Periode 2', width=50)
        self.tree.column('Examen1', width=50)
        self.tree.column('Semestre1', width=50)
              
        self.tree.column('Periode 3', width=50)
        self.tree.column('Periode 4', width=50)
        self.tree.column('Examen2', width=50)
        self.tree.column('Semestre2', width=50)
        self.tree.column('Total', width=50)
        #horizontal scrollbar
        self.tree.place(x=300,y=200)
        self.scrollbar=Scrollbar(self.fen,orient=HORIZONTAL,command=self.tree.xview)
        self.scrollbar.place(x=300,y=400)
        self.tree.configure(xscrollcommand=self.scrollbar.set)
        self.tree.tag_configure('oddrow',background='white')
        self.tree.tag_configure('evenrow',background='lightblue')
        
        self.remplir_combo()
        self.afficher(None)
        
    def remplir_combo(self):
        eleve=Eleve("", "", "", "", "")
        eleves=eleve.get_eleve_inscrit(self.connexion.get_curseur(),self.id_anne_scolaire,self.id_classe)
        self.combo_eleve['values']=[(eleve[5]+'|'+eleve[1]) for eleve in eleves]
        self.combo_eleve.bind('<<ComboboxSelected>>',self.afficher)
        
    def afficher(self,event):
        for i in self.tree.get_children():
            self.tree.delete(i)
        id_eleve=self.combo_eleve.get().split('|')[0]
        fiche_cote=Fiche_cote("", "",0,0,0,0,0,0)
        maximas=cours("","",0,0,"").get_maximas_classe(self.connexion.get_curseur(),self.id_classe)
        cotes=fiche_cote.get_resultat_par_eleve(self.connexion.get_curseur(),id_eleve)
        palmares=fiche_cote.palmares(self.connexion.get_curseur(),self.id_classe,self.id_anne_scolaire,id_eleve)
        for i,cote in enumerate(cotes):
            if i%2==0:
                tags=('evenrow',)
            else:
                tags=('oddrow',)
                
            self.tree.insert('','end',values=(cote[0],cote[1],cote[2],cote[3],cote[4],cote[5],cote[6],cote[7],cote[8],cote[9]),tags=tags)
        #add tag to treeview
        self.tree.tag_configure('oddrow',background='white')
        self.tree.tag_configure('evenrow',background='lightblue')
        #add another row to treeview
         # maximum score
        for i,f in  enumerate(maximas):
            self.tree.insert('','end',values=('Maximas',f[0],f[1],f[2],f[3],f[4],f[5],f[6],f[7],f[8]))
        # total score
        
        self.tree.insert('','end',values=('Total',sum([cote[1] for cote in cotes]),sum([cote[2] for cote in cotes]),sum([cote[3] for cote in cotes]),
                                          sum([cote[4] for cote in cotes]),sum([cote[5] for cote in cotes]),sum([cote[6] for cote in cotes]),
        sum([cote[7] for cote in cotes]),sum([cote[8] for cote in cotes]),sum([cote[9] for cote in cotes])))
       
        #percentage
        for i,f in  enumerate(palmares):
            self.tree.insert('','end',values=('Pourcentage (%)',f[2],f[3],f[4],f[5],f[6],f[7],f[8],f[9],f[10]))
            #classement=f[11]
    
        
        
        
        
        
        self.tree.place(x=300,y=200)
        #lbl classement final
        #self.classemt_label=Label(self.fen,text=f"Classement final: {classement}",font=("Sans Serif",12),fg='white',background='#51a596')
        #self.classemt_label.place(x=300,y=400)

    def fenetre(self):
        return self.fen
        
        
        
        
        
        
        
        
        
        
        
        
        
        