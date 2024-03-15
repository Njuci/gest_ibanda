"""

cette classe nous permettra de gerer les assignations des classes aux utilisateurs
a savoir les enseignants  titulaires des classes
Interface comme celui de la classe utilisateur
avec des commentaires precis


"""
from tkinter import *
from tkinter.messagebox import showerror,showinfo
from assigner_class_back import Assigner_class_back
from user_back import User_back
from classe_backend import Classe
from anne_scolaire_back import AnneScolaire
from tkinter.ttk import Treeview
from login_back import Connexion
from tkinter import ttk
from side_bar_proviseur import Sidebar_proviseur
class Assigner_class_front:
    def __init__(self):
        self.fen=Tk()
        self.connexion=Connexion()
        self.fen.title("Assigner classe")
        self.fen.geometry("800x600")
        self.fen.resizable(0,0)
        self.fen.configure(background='#51a596')
        self.side_bar=Sidebar_proviseur(self.fen,self.connexion.get_curseur())
        self.side_bar.place(x=0,y=0)
        self.label_titre=Label(self.fen, borderwidth=3,relief=SUNKEN,text="Assigner classe",font=("Sans Serif",16),fg='white',background='#091821')
        self.label_titre.place(x=300,y=0,width=500,height=80)
        self.label_tutilaire=Label(self.fen,text="Titulaire",font=("Sans Serif",12),fg='white',background='#51a596')
        self.label_tutilaire.place(x=300,y=100)
        self.combo_tutilaire=ttk.Combobox(self.fen,font=("Sans Serif",12))
        self.combo_tutilaire.place(x=400,y=100)
        self.label_class=Label(self.fen,text="Classe",font=("Sans Serif",12),fg='white',background='#51a596')
        self.label_class.place(x=300,y=150)
        self.combo_class=ttk.Combobox(self.fen,font=("Sans Serif",12))
        self.combo_class.place(x=400,y=150)
        self.label_anne_scolaire=Label(self.fen,text="Année scolaire",font=("Sans Serif",12),fg='white',background='#51a596')
        self.label_anne_scolaire.place(x=300,y=200)
        self.combo_anne_scolaire=ttk.Combobox(self.fen,font=("Sans Serif",12))
        self.combo_anne_scolaire.place(x=400,y=200)
        self.bouton_ajouter=Button(self.fen,text='Ajouter', background='#FF4500',font=("Times",16),fg='white',command=self.ajouter)
        self.bouton_ajouter.place(x=350,y=250,width=100)
        self.bouton_modifier=Button(self.fen,text='Modifier', background='#FF4500',font=("Times",16),fg='white',command=self.modifier)
        self.bouton_modifier.place(x=500,y=250,width=100)
        self.bouton_supprimer=Button(self.fen,text='Supprimer', background='#FF4500',font=("Times",16),fg='white',command=self.supprimer)
        self.bouton_supprimer.place(x=650,y=250,width=100)
        self.id_tutilaire=IntVar()
        self.id_class=IntVar()
        self.id_anne_scolaire=IntVar()
        self.tree=ttk.Treeview(self.fen,columns=('Num','id_tutilaire','Nom Titulaire','id_class','id_anne_scolaire'),show='headings')
        self.tree.heading('Num',text='Numéro')
        self.tree.heading('id_tutilaire',text='Titulaire')
        self.tree.heading('Nom Titulaire',text='Nom Titulaire')
        self.tree.heading('id_class',text='Classe')
        self.tree.heading('id_anne_scolaire',text='Année scolaire')
        self.tree.column('Num',width=50)
        self.tree.column('id_tutilaire',width=50)
        self.tree.column('Nom Titulaire',width=100)
        self.tree.column('id_class',width=100)
        self.tree.column('id_anne_scolaire',width=100)
        self.run()
    def ajouter(self):
        assign=Assigner_class_back(self.id_tutilaire.get(),self.id_class.get(),self.id_anne_scolaire.get())
        if assign.save(self.connexion.get_curseur()):
            showinfo("Succès","Assignation reussie")
            self.afficher()
        else:
            showerror("Erreur","Echec de l'assignation")

    def modifier(self):
        assign=Assigner_class_back(self.id_tutilaire.get(),self.id_class.get(),self.id_anne_scolaire.get())
        if assign.update(self.connexion.get_curseur(),self.id_tutilaire.get(),self.id_class.get(),self.id_anne_scolaire.get()):
            showinfo("Succès","Modification reussie")
            self.afficher()
        else:
            showerror("Erreur","Echec de la modification")
    
    def supprimer(self):
        assign=Assigner_class_back(self.id_tutilaire.get(),self.id_class.get(),self.id_anne_scolaire.get())
        if assign.delete(self.connexion.get_curseur(),self.id_tutilaire.get(),self.id_class.get(),self.id_anne_scolaire.get()):
            showinfo("Succès","Suppression reussie")
            self.afficher()
        else:
            showerror("Erreur","Echec de la suppression")
    def get_old_selection(self):
        self.selected=self.tree.item(self.tree.selection()[0])['values']
        self.id_tutilaire.set(self.selected[1])
        self.id_class.set(self.selected[3])
        self.id_anne_scolaire.set(self.selected[4])

    def afficher(self):
        assign=Assigner_class_back(0,0,0)
        data=assign.get_all(self.connexion.get_curseur())
        self.tree.delete(*self.tree.get_children())
        cpt=0

        for row in data:
            cpt+=1
            self.tree.insert('','end',values=(cpt,row[0],row[1],row[2],row[3]))
        self.tree.bind('<Button-1>',self.get_selection)
    def get_selection(self,event):

        self.selected=self.tree.item(self.tree.selection()[0])['values']
        #renplir les combobox avec les valeurs selectionnees
        self.combo_tutilaire.set(self.selected[2])
        self.combo_class.set(self.selected[3])
        self.combo_anne_scolaire.set(self.selected[4])
    #pour remplir les combobox
    def remplir_combo(self):
        #remplir la combobox titulaire
        user=User_back("","","")
        data=user.get_all(self.connexion.get_curseur())
        self.combo_tutilaire['values']=[(str(row[0])+"|"+row[1]) for row in data]
        self.combo_tutilaire.bind('<<ComboboxSelected>>',self.get_id_tutilaire)
        #remplir la combobox classe
        
        classe=Classe("")
        data=classe.get_all(self.connexion.get_curseur())
        self.combo_class['values']=[(str(data[0])+"|"+data[1]) for data in data]
        self.combo_class.bind('<<ComboboxSelected>>',self.get_id_class)
        #remplir la combobox anne scolaire
        anne=AnneScolaire("",0)
        data=anne.get_all(self.connexion.get_curseur())
        self.combo_anne_scolaire['values']=[(str(data[0])+"|"+data[1]) for data in data]
        self.combo_anne_scolaire.bind('<<ComboboxSelected>>',self.get_id_anne_scolaire)
    def get_id_tutilaire(self,event):
        self.id_tutilaire.set(self.combo_tutilaire.get())
    def get_id_class(self,event):
        self.id_class.set(self.combo_class.get())
    def get_id_anne_scolaire(self,event):
        self.id_anne_scolaire.set(self.combo_anne_scolaire.get())
    def run(self):
        self.remplir_combo()
        self.afficher()
        self.tree.place(x=300,y=300)
        self.fen.mainloop()
if __name__ == '__main__':
    assign=Assigner_class_front()
        