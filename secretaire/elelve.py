
"""

create table eleve(
id_eleve int auto_increment  primary key,
num_permanant varchar(30) unique,
nom_eleve varchar(30),
sexe char(1),
date_nais date,
lieu_nais varchar(30)
);

en se basant sur les codes de class_front 
je fais une interface graphique d'ajout, de modification et de suppression d'un élève et en metant le meme sidebar
"""
import accessoir.generate_key as gn
import datetime as dt
from tkcalendar import DateEntry
from tkinter import *
from tkinter.messagebox import showerror,showinfo,showwarning
from . eleve_back import eleve_back
#from login_back import Connexion
#from side_bar import SideBar
from tkinter.ttk import Treeview,Combobox
from . import side_bar
import report
import login_back 
class EleveFront:
    def __init__(self,connection):
        self.connexion=connection
        self.fen=Tk()
        self.fen.title("Eleve")
        self.fen.geometry("900x900+150+0")
        self.fen.resizable(False,False)
        self.fen.configure(background='#51a596')
        self.side_bar=side_bar.SideBar(self.fen,self.connexion)
        self.side_bar.MenuContainer.config(width=230,height=400)
        
        self.side_bar.place(x=0,y=0)
        self.label_titre=Label(self.fen, borderwidth=3,relief=SUNKEN,text="Eleve",font=("Sans Serif",16),fg='white',background='#091821')
        self.label_titre.place(x=300,y=0,width=500,height=80)
        self.label_nom=Label(self.fen,text="Nom de l'eleve:",font=("Times",15),fg="black",background='#51a596')
        self.label_nom.place(x=305,y=100,width=250)
        self.tex_nom=Entry(self.fen,bd=4,font=("Arial",15))
        self.tex_nom.place(x=550,y=100,width=200)
        self.label_sexe=Label(self.fen,text="Sexe:",font=("Times",15),fg="black",background='#51a596')
        self.label_sexe.place(x=305,y=150,width=250)
        #le sexe de l'eleve soit M ou F dans un bouton radio
        self.radio_sexe=StringVar()
        self.radio_sexe.set("M")
        self.radio_sexeM=Radiobutton(self.fen,text="M",variable=self.radio_sexe,value="M",font=("Times",15),fg="black",background='#51a596')
        self.radio_sexeM.place(x=550,y=150)
        self.radio_sexeF=Radiobutton(self.fen,text="F",variable=self.radio_sexe,value="F",font=("Times",15),fg="black",background='#51a596')
        self.radio_sexeF.place(x=600,y=150)
        self.label_date=Label(self.fen,text="Date de naissance:",font=("Times",15),fg="black",background='#51a596')
        self.label_date.place(x=305,y=200,width=250)
        #la date de naissance de l'eleve dans un entry yyyy-mm-dd
        #format de la date yyyy-mm-dd
        self.tex_date=DateEntry(self.fen,font=("Arial",15),background='black',foreground='white',date_pattern='yyyy-mm-dd')
        self.tex_date.place(x=550,y=200,width=200)
        self.label_lieu=Label(self.fen,text="Lieu de naissance:",font=("Times",15),fg="black",background='#51a596')
        self.label_lieu.place(x=305,y=250,width=250)
        self.tex_lieu=Entry(self.fen,bd=4,font=("Arial",15))
        self.tex_lieu.place(x=550,y=250,width=200)
        #entrer du numero permanent de l'eleve
        self.label_num=Label(self.fen,text="Numero permanent:",font=("Times",15),fg="black",background='#51a596')
        self.label_num.place(x=305,y=300,width=250)
        self.tex_num=Entry(self.fen,bd=4,font=("Arial",15))
        self.tex_num.place(x=550,y=300,width=200)
        #les boutons ajouter, modifier et supprimer
        self.bouton_ajouter=Button(self.fen,text='Ajouter', background='#FF4500',font=("Times",16),fg='white',command=self.add)
        self.bouton_ajouter.place(x=350,y=350,width=100)
        self.bouton_modifier=Button(self.fen,text='Modifier', background='#FF4500',font=("Times",16),fg='white',command=self.modify)
        self.bouton_modifier.place(x=500,y=350,width=100)
        self.bouton_supprimer=Button(self.fen,text='Supprimer', background='#FF4500',font=("Times",16),fg='white',command=self.supprimer)
        self.bouton_supprimer.place(x=650,y=350,width=100)
        self.afficher() 
        #les variables pour la selection
        self.combobox_date=Combobox(self.fen,font=("Arial",15))
        self.combobox_date.place(x=100,y=420,width=100)
        self.combobox_date['values']=('Tous','Aujourd\'hui','Cette semaine','Ce mois','Cette année')
        self.combobox_date.bind('<<ComboboxSelected>>',self.afficher_eleve)
        #bouton pour imprimer
        
        #un treeview pour afficher les eleves
        self.tree=Treeview(self.fen, columns=('Id','Num Permanant','Nom','Sexe','Date de naissance','Lieu de naissance','Date Enre'), show='headings')
        self.tree.heading('Id', text='Id',anchor='center')
        self.tree.heading('Num Permanant', text='NumP',anchor='w')
        self.tree.heading('Nom', text='Nom',anchor='w')
        self.tree.heading('Sexe', text='Sexe',anchor='w')
        self.tree.heading('Date de naissance', text='Date de naissance',anchor='w')
        self.tree.heading('Lieu de naissance', text='Lieu de naissance',anchor='w')
        self.tree.heading('Date Enre',text="Date Enregistrement",anchor='w')
        self.tree.column('Id',width=80,anchor='center')
        self.tree.column('Num Permanant',width=80,anchor='center')
        self.tree.column('Nom',width=150,anchor='center')
        self.tree.column('Sexe',width=30,anchor='center')
        self.tree.column('Date de naissance',width=80,anchor='center')
        self.tree.column('Lieu de naissance',width=70,anchor='center')
        self.tree.column('Date Enre',width=80,anchor='center')
        
        #scrollbar
        self.scrollbar=Scrollbar(self.fen,orient=VERTICAL,command=self.tree.yview)
        self.scrollbar.place(x=880,y=400,height=200)
        self.tree.config(yscrollcommand=self.scrollbar.set)

    
        self.tree.place(x=250,y=400,height=200)
        
        #afficher les eleves dans le treeview les lignes paires en '#51a596' et les lignes impaires en '#091821'
        
        self.tree.tag_configure('oddrow',background='white')
        self.tree.tag_configure('evenrow',background='lightblue')
        self.afficher_eleve()
        self.tree.bind('<ButtonRelease-1>',self.selection)
        self.bouton_imp=Button(self.fen,text='Imprimer', background='#FF4500',font=("Times",16),fg='white',command=self.imprimer)
        self.bouton_imp.place(x=100,y=440,width=100)

        self.selected_id=IntVar()
    def imprimer(self):
        report.generate_pdf(self.tree,"liste des eleves.pdf",['Id','Num Permanant','Nom','Sexe','Date de naissance','Lieu de naissance','Date Enre'],"Listes des elves",
                            [100,20])
    

    def add(self):
        nom=self.tex_nom.get()
        sexe=self.radio_sexe.get()
        date_nais=self.tex_date.get()  
        lieu_nais=self.tex_lieu.get()
        num_permanent=self.tex_num.get()
        if nom and sexe and date_nais and lieu_nais and num_permanent:
            eleve=eleve_back(num_permanent,nom,sexe,date_nais,lieu_nais)
            id=eleve.get_last_id(self.connexion.get_curseur())
            if id[1]==True:
                f=id[0][0]
            
                if  id[0][0] ==None:
                    f=1
                else:
                    f=id[0][0]+1
            key=gn.generate_key("EL",8,f)
            print(key)
            curseur=login_back.Connexion()
            curseur.login()
            
            if eleve.save(curseur.db.cursor(),key):
                showinfo("Ajout Eleve","Eleve Ajouté(e)")
                self.clean_entry()
                self.afficher_eleve()
        else:
            showwarning("Attention","Veuillez remplir tous les champs")
    def modify(self):
        nom=self.tex_nom.get()
        sexe=self.radio_sexe.get()
        date_nais=self.tex_date.get_date()
        lieu_nais=self.tex_lieu.get()
        num_permanent=self.tex_num.get()
        id=self.selected_id

        if nom and sexe and date_nais and lieu_nais and num_permanent:
            eleve=eleve_back(num_permanent,nom,sexe,date_nais,lieu_nais)
            eleve.update(self.connexion.get_curseur(),id)
            showinfo("Modification","Information de l'élève modifié")
            self.clean_entry()
            self.afficher_eleve()
        else:
            showwarning("Attention","Veuillez selectionner un élève")
    def supprimer(self):
        id=self.selected_id
        if id:
            eleve=eleve_back(self.connexion.get_curseur())
            eleve.delete_eleve(id)
            self.afficher_eleve()
        else:
            showwarning("Attention","Veuillez selectionner un élève")
    def afficher_eleve(self):
        eleve=eleve_back("","","","","")
        eleves=eleve.get_all(self.connexion.get_curseur())
        self.tree.delete(*self.tree.get_children())
        cpt=1
        for eleve in eleves:
            if cpt%2==0:
                tag='evenrow'
        
                self.tree.insert('','end',values=eleve,tags=(tag,))
                cpt=cpt+1
            else:
                tag='oddrow'
                self.tree.insert('','end',values=eleve,tags=(tag,))
                cpt=cpt+1
           
    def afficher(self):
        pass
    def selection(self,evt):
        #selectionner un eleve dans le treeview
        self.selected_id=self.tree.item(self.tree.selection())['values'][0]        
        self.clean_entry()
        row=self.tree.item(self.tree.selection())
        self.tex_nom.insert(0,row['values'][2])
        self.radio_sexe.set(row['values'][3])
        self.tex_date.set_date(row['values'][4])
        self.tex_lieu.insert(0,row['values'][5])
        self.tex_num.insert(0,row['values'][1])
    def clean_entry(self):
        #vider les champs
        self.tex_nom.delete(0,END)
        self.tex_lieu.delete(0,END)
        self.tex_num.delete(0,END)
    def fenetre(self):
        return self.fen
    

