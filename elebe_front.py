"""
en se basant sur les codes de class_front 
je fais une interface graphique d'ajout, de modification et de suppression d'un élève et en metant le meme sidebar
"""
import datetime as dt
from tkinter import *
from tkinter.messagebox import showerror,showinfo,showwarning
from eleve_back import eleve_back
from tkinter.ttk import Treeview
from login_back import Connexion
from side_bar import SideBar
from tkcalendar import DateEntry
class EleveFront:
    def __init__(self):
        self.connexion=Connexion()
        self.fen=Tk()
        self.fen.title("Eleve")
        self.fen.geometry("800x700+150+0")
        self.fen.resizable(False,False)
        self.fen.configure(background='#51a596')
        self.side_bar=SideBar(self.fen,self.connexion.get_curseur())
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
        #la date de naissance de l'eleve dans un entry yyyy-mm-dd de tkcalendar
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
        self.bouton_ajouter=Button(self.fen,text='Ajouter', background='#FF4500',font=("Times",16),fg='white',command=self.ajouter)
        self.bouton_ajouter.place(x=350,y=350,width=100)
        self.bouton_modifier=Button(self.fen,text='Modifier', background='#FF4500',font=("Times",16),fg='white',command=self.modify)
        self.bouton_modifier.place(x=500,y=350,width=100)
        self.bouton_supprimer=Button(self.fen,text='Supprimer', background='#FF4500',font=("Times",16),fg='white',command=self.supprimer)
        self.bouton_supprimer.place(x=650,y=350,width=100)

        #les variables pour la selection

        self.selected_id=IntVar()
        self.selected_nom=StringVar()
        self.E=None
        #un treeview pour afficher les eleves
        self.tree=Treeview(self.fen, columns=('Id','Num Permanant','Nom','Sexe','Date de naissance','Lieu de naissance'), show='headings')
        self.tree.heading('Id', text='Id')
        self.tree.heading('Num Permanant', text='Num Permanant')
        self.tree.heading('Nom', text='Nom')
        self.tree.heading('Sexe', text='Sexe')
        self.tree.heading('Date de naissance', text='Date de naissance')
        self.tree.heading('Lieu de naissance', text='Lieu de naissance')
        self.tree.column('Id',width=20)
        self.tree.column('Num Permanant',width=100)
        self.tree.column('Nom',width=150)
        self.tree.column('Sexe',width=50)
        self.tree.column('Date de naissance',width=50)
        self.tree.column('Lieu de naissance',width=100)
        self.tree.place(x=300,y=420,height=200)
        #afficher les eleves dans le treeview les lignes paires en '#51a596' et les lignes impaires en '#091821'
        self.tree.tag_configure('pair',background='#51a596')
        self.tree.tag_configure('impair',background='#091821')
        self.afficher()        
    def selection(self,evt):
        #selectionner un eleve dans le treeview
        self.selected_id=self.tree.item(self.tree.selection())['values'][0]        
        self.clean_entry()
        row=self.tree.item(self.tree.selection())
        self.tex_nom.insert(0,row['values'][1])
        self.radio_sexe.set(row['values'][2])
        self.tex_date.set_date(row['values'][3])
        self.tex_lieu.insert(0,row['values'][4])
        self.tex_num.insert(0,row['values'][5])
    def clean_entry(self):
        #vider les champs
        self.tex_nom.delete(0,END)
        self.tex_lieu.delete(0,END)
        self.tex_num.delete(0,END)
    def ajouter(self):
        #ajouter un eleve
        if self.E==None:
            self.E=eleve_back(self.tex_num.get(),self.tex_nom.get(),self.radio_sexe.get(),self.tex_date.get(),self.tex_lieu.get())
            if self.E.save(self.connexion.get_curseur()):
                self.afficher()
                showinfo("Succès","Ajout réussi")
            else:
                showerror("Echec","Ajout échoué")
        else:
            showwarning("Echec","Veuillez vider le formulaire")
    def modify(self):   
        #modifier un eleve
        if self.E==None:
            self.E=eleve_back(self.tex_nom.get(),self.radio_sexe.get(),self.tex_date.get(),self.tex_lieu.get())
            if self.E.update(self.connexion.get_curseur(),self.selected_id):
                self.afficher()
                self.E=None
                showinfo("Succès","Modification réussie")
            else:
                showerror("Echec","Modification échouée")
        else:
            showwarning("Echec","Veuillez vider le formulaire")
    def supprimer(self):
        #supprimer un eleve
        if self.E==None:
            self.E=eleve_back(self.tex_nom.get(),self.radio_sexe.get(),self.tex_date.get(),self.tex_lieu.get())
            self.E=None
            if self.E.delete(self.connexion.get_curseur()):
                self.afficher()
                showinfo("Succès","Suppression réussie")
            else:
                showerror("Echec","Suppression échouée")
        else:
            showwarning("Echec","Veuillez vider le formulaire")
    def afficher(self):
        #afficher les eleves dans le treeview
        self.tree.delete(*self.tree.get_children())
        i=0
        for row in eleve_back("e","e","e","e","e").get_all(self.connexion.get_curseur()):
            if i%2==0:
                self.tree.insert("", "end", values=row,tags=('pair',))
            else:
                self.tree.insert("", "end", values=row,tags=('impair',))
            i+=1
        self.tree.bind("<ButtonRelease-1>",self.selection)
    def get_entry(self):
        self.selected_nom.set(self.tex_nom.get())
    def fenetre(self):
        return self.fen
    
d=EleveFront()
d.fenetre().mainloop()
