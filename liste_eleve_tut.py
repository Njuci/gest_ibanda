"""cette classe est dediee à l'affichage de la liste des eleves d'une classe
pour une année scolaire donnée
pour une classe donnée

se referer à la classe SideBar_tutulaire pour voir comment elle est utilisée

"""

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
from secretaire.eleve_back import eleve_back as Eleve
from secretaire.anne_scolaire_back import AnneScolaire
from secretaire.classe_backend import Classe
from tkinter.ttk import Treeview
from login_back import Connexion
import side_bar_tutulaire as side_bar_tutulaire

class ListeEleveTut:
    def __init__(self,connection):
        
        self.connexion=connection['connexion']
        self.id_user=connection['id_user']
        self.id_classe=connection['id_classe']
        self.id_anne_scolaire=connection['id_annee_scolaire']    
        self.fen=Tk()
        self.fen.title("Liste des élèves")
        self.fen.geometry("800x600+150+0")
        self.fen.resizable(0,0)
    
        self.fen.configure(background='#51a596')
        self.side_bar=side_bar_tutulaire.SideBar_tutulaire(self.fen,self.connexion)
        self.side_bar.place(x=0,y=0)
        self.label_titre=Label(self.fen, borderwidth=3,relief=SUNKEN,text="Liste des élèves",font=("Sans Serif",16),fg='white',background='#091821')
        self.label_titre.place(x=300,y=0,width=500,height=80)
        self.label_classe=Label(self.fen,text="Classe",font=("Sans Serif",12),fg='white',background='#51a596')
        self.label_classe.place(x=300,y=100)
        self.combo_classe=ttk.Combobox(self.fen,font=("Sans Serif",12))
        #self.combo_classe.place(x=400,y=100)
        self.label_anne_scolaire=Label(self.fen,text="Année scolaire",font=("Sans Serif",12),fg='white',background='#51a596')
        #self.label_anne_scolaire.place(x=300,y=150)
        self.combo_anne_scolaire=ttk.Combobox(self.fen,font=("Sans Serif",12))
        self.combo_anne_scolaire.place(x=400,y=150)
        self.bouton_afficher=Button(self.fen,text='Afficher', background='#FF4500',font=("Times",16),fg='white',command=self.afficher)
        self.bouton_afficher.place(x=350,y=200,width=100)
        self.tree=ttk.Treeview(self.fen,columns=('Num','id_eleve','Nom','Prenom','Sexe','Date de naissance'),show='headings')
        self.tree.heading('Num',text='Numéro')
        self.tree.heading('id_eleve',text='id_eleve')
        self.tree.heading('Nom',text='Nom')
        self.tree.heading('Prenom',text='Prenom')
        self.tree.heading('Sexe',text='Sexe')
        self.tree.heading('Date de naissance',text='Date de naissance')
        self.tree.column('Num',width=50)
        self.tree.column('id_eleve',width=80)
        self.tree.column('Nom',width=100)
        self.tree.column('Prenom',width=100)
        self.tree.column('Sexe',width=50)
        self.tree.column('Date de naissance',width=150)
        self.tree.place(x=300,y=250,height=200)
        self.remplir_combo()
        self.fen.mainloop()
        self.afficher()
    def remplir_combo(self):
        self.combo_classe['values']=Classe("").get_all(self.connexion.get_curseur())
        self.combo_anne_scolaire['values']=AnneScolaire("","").get_all(self.connexion.get_curseur())
    def afficher(self):
        self.tree.delete(*self.tree.get_children())
        id_classe=self.combo_classe.get().split('-')[0]
        id_anne_scolaire=self.combo_anne_scolaire.get().split('-')[0]
        eleves=Eleve.eleve_classe(self.connexion.get_curseur(),self.id_classecolaire)
        for i,eleve in enumerate(eleves):
            self.tree.insert('','end',values=(i+1,eleve[0],eleve[1],eleve[2],eleve[3],eleve[4]))
        self.tree.place(x=300,y=250,height=200)
        self.tree.bind('<Double-1>',self.selection)
    def selection(self,evt):
        item=self.tree.selection()
        id_eleve=self.tree.item(item,'values')[1]
        showinfo("Informations",Eleve.get_eleve(self.connexion,id_eleve))
        #print(id_eleve)

if __name__ == '__main__':
    connexion=Connexion()
    
    ListeEleveTut(connexion)