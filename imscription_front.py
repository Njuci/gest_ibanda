""""
fais maintenant une interface graphique d'ajout, de modification et de suppression d'une incrisption dasn une classe pour une annee scolaire donnee
avec tkinter tkinter.ttk et tkcalendar

en mettant les elves, les classses et les anne_scollaire dans des combobox
et en mettant le meme sidebar
"""

from tkinter import *
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
from inscription_backend import Inscription_back
from login_back import Connexion
from side_bar import SideBar
from tkinter.ttk import Treeview
from tkinter.messagebox import showerror,showinfo,showwarning
from eleve_back import eleve_back
from classe_backend import Classe
from anne_scolaire_back import AnneScolaire


class InscriptionFront:
    def __init__(self):
        self.connexion=Connexion()
        self.fen=Tk()
        self.fen.title("Inscription")
        self.fen.geometry("900x700+150+0")
        self.fen.resizable(False,False)
        self.fen.configure(background='#51a596')
        self.side_bar=SideBar(self.fen,self.connexion.get_curseur())
        self.side_bar.place(x=0,y=0)
        self.label_titre=Label(self.fen, borderwidth=3,relief=SUNKEN,text="Inscription",font=("Sans Serif",16),fg='white',background='#091821')
        self.label_titre.place(x=300,y=0,width=500,height=80)
        self.label_eleve=Label(self.fen,text="Eleve:",font=("Times",15),fg="black",background='#51a596')
        self.label_eleve.place(x=305,y=100,width=250)
        self.combo_eleve=Combobox(self.fen,font=("Arial",15))
        self.combo_eleve.place(x=550,y=100,width=200)
        self.label_classe=Label(self.fen,text="Classe:",font=("Times",15),fg="black",background='#51a596')
        self.label_classe.place(x=305,y=150,width=250)
        self.combo_classe=Combobox(self.fen,font=("Arial",15))
        self.combo_classe.place(x=550,y=150,width=200)
        self.label_anne=Label(self.fen,text="Annee scolaire:",font=("Times",15),fg="black",background='#51a596')
        self.label_anne.place(x=305,y=200,width=250)
        self.combo_anne=Combobox(self.fen,font=("Arial",15))
        self.combo_anne.place(x=550,y=200,width=200)
        self.id_inscription_LABEL= Label(self.fen,text="Id de l'inscription:",font=("Times",15),fg="black",background='#51a596')
        self.id_inscription_LABEL.place(x=305,y=250,width=250)
        self.id_inscription=Entry(self.fen,bd=4,font=("Arial",15))
        self.id_inscription.place(x=550,y=250,width=200)
        
        self.remplir_combo()
        self.bouton_ajouter=Button(self.fen,text='Ajouter', background='#FF4500',font=("Times",16),fg='white',command=self.ajouter)
        self.bouton_ajouter.place(x=350,y=300,width=100)
        self.bouton_modifier=Button(self.fen,text='Modifier', background='#FF4500',font=("Times",16),fg='white',command=self.modify)
        self.bouton_modifier.place(x=500,y=300,width=100)
        self.bouton_supprimer=Button(self.fen,text='Supprimer', background='#FF4500',font=("Times",16),fg='white',command=self.supprimer)
        self.bouton_supprimer.place(x=650,y=300,width=100)
        #bouton pour afficher chercher les inscriptions par classe
        self.bouton_chercher=Button(self.fen,text='Chercher', background='#FF4500',font=("Times",16),fg='white',command=self.afficher)
        self.bouton_chercher.place(x=800,y=300,width=100)
       #bouton pour afficher chercher les inscriptions par classer et par annee scolaire
        self.bouton_chercher=Button(self.fen,text='Chercher', background='#FF4500',font=("Times",16),fg='white',command=self.afficher)
        self.bouton_chercher.place(x=800,y=300,width=100)

        
        self.selected_id=IntVar()
        self.selected_eleve=StringVar()
        self.selected_classe=StringVar()
        self.selected_anne=StringVar()
        self.E=None
        #affichage des inscriptions ajouter dans un treeview le nom et l'id de l'eleve, le nom et l'id de la classe et l'annee scolaire


        self.tree=Treeview(self.fen, columns=('Id','Id_eleve','Eleve','Classe','Annee scolaire','Id Inscription'), show='headings')
        self.tree.heading('Id', text='Id')
        self.tree.heading('Id_eleve', text='Id_eleve')
        self.tree.heading('Eleve', text='Eleve')
        self.tree.heading('Classe', text='Classe')
        self.tree.heading('Annee scolaire', text='Annee scolaire')
        self.tree.heading('Id Inscription', text='Id Inscription')

        self.tree.column('Id',width=20)
        self.tree.column('Id_eleve',width=40)
        self.tree.column('Eleve',width=100)
        self.tree.column('Classe',width=100)
        self.tree.column('Annee scolaire',width=100)
        self.tree.column('Id Inscription',width=100)
        self.tree.place(x=300,y=350,height=200)
        #button pour imprimer les inscriptions
        self.bouton_imprimer=Button(self.fen,text='Imprimer', background='#FF4500',font=("Times",16),fg='white',command=self.imprimer)
        self.bouton_imprimer.place(x=350,y=550,width=100)

        self.afficher()
        self.fen.mainloop()
    def imprimer(self):
        pass
    def afficher(self):
        self.tree.delete(*self.tree.get_children())
        self.E=Inscription_back(0,0,0,0)
        for row in self.E.get_all(self.connexion.get_curseur()):
            self.tree.insert("",END,values=row)
    def selection(self,evt):
        self.selected_id=self.tree.item(self.tree.selection())['values'][0]
        self.clean_entry()
        row=self.tree.item(self.tree.selection())
        self.combo_eleve.set(row['values'][2])
        self.combo_classe.set(row['values'][3])
        self.combo_anne.set(row['values'][4])
    def clean_entry(self):
        self.combo_eleve.set('')
        self.combo_classe.set('')
        self.combo_anne.set('')
    def ajouter(self):
        if self.E==None:
            self.E=Inscription_back(0,self.combo_eleve.get(),self.combo_classe.get(),self.combo_anne.get())
            if self.E.save(self.connexion.get_curseur()):
                self.afficher()
                showinfo("Succès","Ajout réussi")
            else:
                showerror("Echec","Ajout échoué")
        else:
            showwarning("Echec","Veuillez vider le formulaire")

    def modify(self):
        if self.E==None:
            self.E=Inscription_back(0,self.combo_eleve.get(),self.combo_classe.get(),self.combo_anne.get())
            if self.E.update(self.connexion.get_curseur(),self.selected_id):
                self.afficher()
                self.E=None
                showinfo("Succès","Modification réussie")
            else:
                showerror("Echec","Modification échouée")
        else:
            showwarning("Echec","Veuillez vider le formulaire")

    def supprimer(self):
        if self.E==None:
            self.E=Inscription_back(0,self.combo_eleve.get(),self.combo_classe.get(),self.combo_anne.get())
            self.E=None
            if self.E.delete(self.connexion.get_curseur()):
                self.afficher()
                showinfo("Succès","Suppression réussie")
            else:
                showerror("Echec","Suppression échouée")
        else:
            showwarning("Echec","Veuillez vider le formulaire")
    #faire une methode pour remplir les combobox 
                # les ID des eleves
                # les ID des classes
                # les annees scolaires
    def remplir_combo(self):
        #remplir les combobox de classe et d'annee scolaire et d'eleve
        eleve=eleve_back("","","","","")
        eleves=eleve.get_all(self.connexion.get_curseur())
        for eleve in eleves:
            self.combo_eleve['values']=(eleve[0],eleve[1])
        classe=Classe("")
        classes=classe.get_all(self.connexion.get_curseur())
        for classe in classes:
            self.combo_classe['values']=(classe[0],classe[1])
        anne=AnneScolaire("",True)
        annees=anne.get_all(self.connexion.get_curseur())
        for anne in annees:
            self.combo_anne['values']=(anne[0],anne[1])
        self.combo_eleve.bind("<<ComboboxSelected>>",self.get_id_eleve)
        self.combo_classe.bind("<<ComboboxSelected>>",self.get_id_classe)
        self.combo_anne.bind("<<ComboboxSelected>>",self.get_id_anne)
    def get_id_eleve(self,evt):
        self.selected_eleve.set(self.combo_eleve.get())
    def get_id_classe(self,evt):
        self.selected_classe.set(self.combo_classe.get())
    def get_id_anne(self,evt):
        self.selected_anne.set(self.combo_anne.get())
    def get_eleve(self):
        return self.selected_eleve.get()
    def get_classe(self):
        return self.selected_classe.get()
    def get_anne(self):
        return self.selected_anne.get()
    def get_id(self):
        return self.selected_id.get()
    def fenetre(self):
        return self.fen
#faire une classe pour les eleves
#faire une classe pour les classes
#faire une classe pour les annees scolaires
#faire une classe pour les inscriptions
#faire une classe pour la connexion
#faire une classe pour le sidebar
#faire une classe pour l'interface graphique
#faire une methode pour remplir les combobox
#faire une methode pour ajouter une inscription
#faire une methode pour modifier une inscription
#faire une methode pour supprimer une inscription
#faire une methode pour afficher les inscriptions
#faire une methode pour selectionner une inscription
#faire une methode pour nettoyer les champs
#faire une methode pour recuperer l'id de l'eleve
#faire une methode pour recuperer l'id de la classe
#faire une methode pour recuperer l'id de l'annee scolaire
#faire une methode pour recuperer l'id de l'inscription
#faire une methode pour recuperer l'eleve
#faire une methode pour recuperer la classe
#faire une methode pour recuperer l'annee scolaire
#faire une methode pour recuperer l'id

#faire une methode pour recuperer l'eleve
#faire une methode pour recuperer la classe
#faire une methode pour recuperer l'annee scolaire
    
#faire une methode pour recuperer l'id
#faire une methode pour recuperer l'eleve
#faire une methode pour recuperer la classe
#faire une methode pour recuperer l'annee scolaire
#faire une methode pour recuperer l'id
    




























        
d=InscriptionFront()
d.fen.mainloop()
