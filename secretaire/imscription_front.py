""""
fais maintenant une interface graphique d'ajout, de modification et de suppression d'une incrisption dasn une classe pour une annee scolaire donnee
avec tkinter tkinter.ttk et tkcalendar

en mettant les elves, les classses et les anne_scollaire dans des combobox
et en mettant le meme sidebar
"""
import sys
sys.path.append('/accessoir')
sys.path.append('/titulaire')
sys.path.append('/secretaire')
import fiche_cote_back as fch

from tkinter import *
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
from .inscription_backend import Inscription_back
from .  import side_bar
from tkinter.ttk import Treeview
from tkinter.messagebox import showerror,showinfo,showwarning,askyesno
from .eleve_back import eleve_back
from .classe_backend import Classe
from .anne_scolaire_back import AnneScolaire
import generate_key as gn
import cours_backend as cours
from tkinter.messagebox import showerror
class InscriptionFront:
    def __init__(self,connection):
        self.connexion=connection
        self.fen=Tk()
        self.fen.title("Inscription")
        self.fen.geometry("1000x700+150+0")
        self.fen.resizable(False,False)
        self.fen.configure(background='#51a596')
        self.side_bar=side_bar.SideBar(self.fen,self.connexion)
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
        self.id_inscription=Label(self.fen,font=("Arial",15),text='')
        self.id_inscription.place(x=550,y=250,width=200)
        
        self.remplir_combo()
        self.bouton_ajouter=Button(self.fen,text='Ajouter', background='#FF4500',font=("Times",16),fg='white',command=self.ajouter)
        self.bouton_ajouter.place(x=350,y=300,width=100)
        self.bouton_modifier=Button(self.fen,text='Modifier', background='#FF4500',font=("Times",16),fg='white',command=self.modifier)
        self.bouton_modifier.place(x=500,y=300,width=100)
        self.bouton_supprimer=Button(self.fen,text='Supprimer', background='#FF4500',font=("Times",16),fg='white',command=self.supprimer)
        self.bouton_supprimer.place(x=650,y=300,width=100)
        #bouton pour afficher chercher les inscriptions par classe
        self.bouton_chercher=Button(self.fen,text='Chercher', background='#FF4500',font=("Times",16),fg='white',command=self.afficher)
        self.bouton_chercher.place(x=800,y=300,width=100)
       #bouton pour afficher chercher les inscriptions par classer et par annee scolaire
        self.bouton_chercher=Button(self.fen,text='Chercher', background='#FF4500',font=("Times",16),fg='white',command=self.afficher)
        self.bouton_chercher.place(x=800,y=300,width=100)

        
        self.selected_id=StringVar()
        self.selected_eleve=StringVar()
        self.selected_classe=StringVar()
        self.selected_anne=StringVar()
        self.E=None
        #affichage des inscriptions ajouter dans un treeview le nom et l'id de l'eleve, le nom et l'id de la classe et l'annee scolaire


        self.tree=Treeview(self.fen, columns=('Id','Id_el','Eleve','Classe','Nom','Annee scolaire','Id Inscr'), show='headings')
        self.tree.heading('Id', text='Id')
        self.tree.heading('Id_el', text='Id_el')
        self.tree.heading('Eleve', text='Eleve')
        self.tree.heading('Classe', text='Classe')
        self.tree.heading('Nom',text='Nom classe')
        self.tree.heading('Annee scolaire', text='Annee scolaire')
        self.tree.heading('Id Inscr', text='Id Inscr')

        self.tree.column('Id',width=20)
        self.tree.column('Id_el',width=100)
        self.tree.column('Eleve',width=100)
        self.tree.column('Classe',width=100)
        self.tree.column('Nom',width=100)    
        
        self.tree.column('Annee scolaire',width=100)
        self.tree.column('Id Inscr',width=100)
        self.tree.place(x=300,y=350,height=200)
        #button pour imprimer les inscriptions
        self.bouton_imprimer=Button(self.fen,text='Imprimer', background='#FF4500',font=("Times",16),fg='white',command=self.imprimer)
        self.bouton_imprimer.place(x=350,y=550,width=100)

        self.afficher()
      
    def imprimer(self):
        pass
    def afficher(self):
        self.tree.delete(*self.tree.get_children())
        self.E=Inscription_back("",0,0)
        #compyer le nombre d'inscriptions
        inscription=self.E.get_all_b(self.connexion.get_curseur())
        #remplir le treeview avec les inscriptions id et nom de l'eleve, id et nom de la classe et l'annee scolaire
        cpt=0
        #afficher les inscriptions
        for row in inscription:
            cpt+=1
            self.tree.insert("",END,values=(cpt,row[0],row[1],row[3],row[4],row[2]+'|'+row[6],row[5]))
        self.tree.bind('<Double-1>',self.selection)
    def selection(self,evt):
        self.selected_id=self.tree.item(self.tree.selection())['values'][6]
        self.clean_entry()
        row=self.tree.item(self.tree.selection())
       
        self.combo_eleve.set(row['values'][1]+'|'+ row['values'][2])
        self.combo_classe.set(row['values'][3]+'|'+row['values'][4])
        self.combo_anne.set(row['values'][5])
        #self.id_inscription['text']=row[6]
        #set la valeur de l' id inscription dans lelabel id_inscription
        self.id_inscription['text']=row['values'][6]
    def clean_entry(self):
        self.combo_eleve.set('')
        self.combo_classe.set('')
        self.combo_anne.set('')
        self.id_inscription['text']=''
    def ajouter(self):
        self.connexion.db.autocommit=False
        #start transaction
        self.connexion.db.start_transaction()
            
        self.E=Inscription_back(self.combo_eleve.get().split("|")[0],self.combo_anne.get().split("|")[0],self.combo_classe.get().split("|")[0])
        cour=cours.cours_back("","","","","")
        #recuperer les cours de la classe
        resultat=cour.get_cours_by_classe(self.connexion.get_curseur(),self.combo_classe.get().split("|")[0])
        print(resultat)
        
        id=self.E.get_last_id(self.connexion.get_curseur())
        if id[1]==True:
            f=id[0][0]
            
            if  id[0][0] ==None:
                    f=1
            else:
                f=id[0][0]+1
            key=gn.generate_key("INS",8,f)    
        
        if self.E.save(self.connexion.get_curseur(),key):
            if len(resultat)!=0:
                    
                for i in resultat:
                    print(i[0])
                    fiche=fch.Fiche_cote_back(i[0],key,0,0,0,0,0,0)
                    
                    if fiche.add_fiche_cote(self.connexion.curseur):
                        print()
                        
                        
                    else:
                        self.connexion.db.rollback()
                        showerror('Fiche ', "Veuillez terminer la configuration de la classe")
                
                self.afficher()
                self.E=None
                showinfo("Succès","Ajout réussi")
                self.connexion.db.commit()
            else:
                showerror('Fiche ', "Veuillez terminer la configuration de la classe")
                self.connexion.db.rollback()
                
                #commit
            #commit
            self.connexion.db.autocommit=True
                
            
            
            #creer une transaction qui permet de donner 0 à l'eleve pour chaque cours de la classe ou il est inscrit maintenant
            #creer une transaction qui permet de donner 0 à l'eleve pour chaque cours de la classe ou il est inscrit maintenant
            
            
        else:
            showerror("Echec","Ajout échoué")
            self.E=None 
            self.connexion.db.rollback()    
            self.connexion.db.autocommit=True
    #faire une methode pour modifier une inscription en se basant sur la fonction self.ajoouter 
    #et en ajoutant une transaction pour modifier les notes des eleves
    #faire une methode pour supprimer une inscription en se basant sur la fonction self.ajoouter
    #et en ajoutant une transaction pour supprimer les notes des eleves
    def modifier(self):
        self.E=Inscription_back(self.combo_eleve.get().split("|")[0],self.combo_anne.get().split("|")[0],self.combo_classe.get().split("|")[0])
        self.E.id_inscription=self.selected_id
        
        
        self.connexion.db.autocommit=False
        #start transaction
        self.connexion.db.start_transaction()
        
        self.E.delete_fiche(self.connexion.get_curseur(),self.selected_id)
        cour=cours.cours_back("","","","","")
        #recuperer les cours de la classe
        resultat=cour.get_cours_by_classe(self.connexion.get_curseur(),self.combo_classe.get().split("|")[0])
        print(resultat)
        
        if self.E:
                
            
            if self.E.update(self.connexion.get_curseur(),self.selected_id):
                if len(resultat)!=0:
                    for i in resultat:
                        print(i[0])
                        fiche=fch.Fiche_cote_back(i[0],self.selected_id,0,0,0,0,0,0)
                        if fiche.add_fiche_cote(self.connexion.curseur):
                            print()
                            
                        else:
                            self.connexion.db.rollback()
                            showerror('Fiche ', "Veuillez terminer la configuration de la classe")
                            self.connexion.db.autocommit=True

                            
                
                    self.afficher()
                    self.E=None
                    showinfo("Succès","Modification réussie")
                    self.connexion.db.commit()
                    self.connexion.db.autocommit=True
                else:
                    self.afficher()
                    self.E=None
                    showerror('Fiche ', "Veuillez terminer la    configuration de la classe")
                    self.connexion.db.autocommit=True
                
            else:
                showerror("Echec","Modification échouée")
                self.E=None
                self.connexion.db.rollback()
                self.connexion.db.autocommmit=True
        else:
            showwarning("Echec","Veuillez vider le formulaire")
            self.connexion.db.rollback()
    
            self.connexion.db.autocommit=True
        
    
    
    #
    def modify(self):
        if self.E==None:
            self.E=Inscription_back(0,self.combo_eleve.get(),self.combo_classe.get(),self.combo_anne.get())
            
            
            if self.E.update(self.connexion.get_curseur(),self.selected_id):
                self.afficher()
                
                self.E=None
                showinfo("Succès","Modification réussie")
            else:
                showerror("Echec","Modification échouée")
                self.E=None
        else:
            showwarning("Echec","Veuillez vider le formulaire")

    def supprimer(self):
        if self.E==None:
            self.E=Inscription_back(0,self.combo_eleve.get(),self.combo_classe.get(),self.combo_anne.get())
            if askyesno("Confirmation", "Êtes-vous sûr de vouloir supprimer cette inscription ?"):
                if self.E.delete(self.connexion.get_curseur()):
                    self.afficher()
                    showinfo("Succès", "Suppression réussie")
                    self.E = None
                else:
                    self.E = None
                    showerror("Echec", "Suppression échouée")
            else:
                showinfo("Annulation", "Suppression annulée")
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
        eleve_t=[]
        for eleve in eleves:
            eleve_t.append(str(eleve[0])+"|"+eleve[2])
        self.combo_eleve['values']=eleve_t
        classe=Classe("")
        classes=classe.get_all(self.connexion.get_curseur())
        class_t=[]
        for classe in classes:
            class_t.append(str(classe[0])+"|"+classe[1])
            
        self.combo_classe['values']=class_t
        anne=AnneScolaire("",True)
        annees=anne.get_all(self.connexion.get_curseur())
        anne_liste=[]
        for anne in annees:
            anne_liste.append(str(anne[0])+"|" +anne[1])
        anne_liste=tuple(anne_liste)
            
        self.combo_anne['values']= anne_liste
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
    




























