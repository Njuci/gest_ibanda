"""
imterface graphique pour le domaine de cours
comme le fichier assigner_class_front.py, l
e fichier domaine_cours_front.py est un fichier qui contient une classe qui permet de gerer l'interface graphique pour le domaine de cours

"""
from tkinter import *
from tkinter.ttk import Treeview
from domaine_cours_back import Domaine_cours
from login_back import Connexion
from side_bar_proviseur import Sidebar_proviseur
from tkinter.messagebox import showerror,showinfo
from tkinter import ttk

class Domaine_cours_front:
    def __init__(self):
        self.fen=Tk()
        self.connexion=Connexion()
        self.fen.title("Domaine de cours")
        self.fen.geometry("800x600")
        self.fen.resizable(0,0)
        self.fen.configure(background='#51a596')
        self.side_bar=Sidebar_proviseur(self.fen,self.connexion.get_curseur())
        self.side_bar.place(x=0,y=0)
        self.label_titre=Label(self.fen, borderwidth=3,relief=SUNKEN,text="Domaine de cours",font=("Sans Serif",16),fg='white',background='#091821')
        self.label_titre.place(x=300,y=0,width=500,height=80)
        self.label_nom=Label(self.fen,text="Nom",font=("Sans Serif",12),fg='white',background='#51a596')
        self.label_nom.place(x=300,y=100)
        self.entry_nom=Entry(self.fen,font=("Sans Serif",12))
        self.entry_nom.place(x=400,y=100)
        self.bouton_ajouter=Button(self.fen,text='Ajouter', background='#FF4500',font=("Times",16),fg='white',command=self.ajouter)
        self.bouton_ajouter.place(x=350,y=150,width=100)
        self.bouton_modifier=Button(self.fen,text='Modifier', background='#FF4500',font=("Times",16),fg='white',command=self.modifier)
        self.bouton_modifier.place(x=500,y=150,width=100)
        self.bouton_supprimer=Button(self.fen,text='Supprimer', background='#FF4500',font=("Times",16),fg='white',command=self.supprimer)
        self.bouton_supprimer.place(x=650,y=150,width=100)
        self.id_domaine=IntVar()
        self.tree=ttk.Treeview(self.fen,columns=('Num','id_domaine','Nom'),show='headings')
        self.tree.heading('Num',text='Numéro')
        self.tree.heading('id_domaine',text='Id')
        self.tree.heading('Nom',text='Nom')
        self.tree.column('Num',width=50)
        self.tree.column('id_domaine',width=50)
        self.tree.column('Nom',width=100)
        self.run()
    def afficher(self):
        domaine=Domaine_cours("")
        data=domaine.get_all(self.connexion.get_curseur())
        for i in self.tree.get_children():
            self.tree.delete(i)
        for i in range(len(data)):
            self.tree.insert('','end',values=(i+1,data[i][0],data[i][1]))
        #selection d'un element dans le treeview
        self.tree.bind("<Button-1>",self.selection)
        self.tree.place(x=300,y=200)

    def selection(self,event):
        item=self.tree.selection()[0]
        self.id_domaine.set(self.tree.item(item,"values")[1])
        self.entry_nom.delete(0,END)
        self.entry_nom.insert(0,self.tree.item(item,"values")[2])



    def ajouter(self):
        domaine=Domaine_cours(self.entry_nom.get())
        if domaine.ajouter(self.connexion.get_curseur()):
            showinfo("Succès","Domaine ajouté avec succès")
            self.run()
        else:
            showerror("Erreur","Erreur lors de l'ajout du domaine")


    def modifier(self):
        domaine=Domaine_cours(self.entry_nom.get())
        if domaine.update(self.id_domaine.get(),self.connexion.get_curseur()):
            showinfo("Succès","Domaine modifié avec succès")
            self.run()
        else:
            showerror("Erreur","Erreur lors de la modification du domaine")

    def supprimer(self):

        domaine=Domaine_cours(self.entry_nom.get())
        if domaine.delete(self.id_domaine.get(),self.connexion.get_curseur()):
            showinfo("Succès","Domaine supprimé avec succès")
            self.run()
        else:
            showerror("Erreur","Erreur lors de la suppression du domaine")
    def run(self):
        self.afficher()
        self.fen.mainloop()
d=Domaine_cours_front()
# d.run()
# d.fen.mainloop()  