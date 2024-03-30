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
import accessoir.generate_key as gn
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
        self.id_domaine=StringVar()
        self.tree=ttk.Treeview(self.fen,columns=('Num','id_domaine','Nom'),show='headings')
        self.tree.heading('Num',text='Numéro')
        self.tree.heading('id_domaine',text='Id')
        self.tree.heading('Nom',text='Nom')
        self.tree.column('Num',width=30)
        self.tree.column('id_domaine',width=80)
        self.tree.column('Nom',width=140)
        self.tree.tag_configure('evenrow',background='lightgray',foreground='black')
        self.tree.tag_configure('oddrow',background='white',foreground='black')
        self.afficher()
        
        #selection d'un element dans le treeview
        self.tree.bind("<Double-Button-1>",self.selection)
        self.tree.place(x=300,y=200,height=200)

        
        
        #scrollbar
        self.scrollbar=Scrollbar(self.fen,orient=VERTICAL,command=self.tree.yview)
        self.scrollbar.place(x=555,y=200,height=200)
        self.tree.config(yscrollcommand=self.scrollbar.set)
        
        
        #impression  des domaine_cours
        self.bouton_imp=Button(self.fen,text='Imprimer', background='#FF4500',font=("Times",16),fg='white',command=self.imprimer)
        self.bouton_imp.place(x=650,y=400,width=100)
        #self.afficher()
        
        self.run()

    def imprimer(self):
        pass
        
    def afficher(self):
        domaine=Domaine_cours("")
        data=domaine.get_all(self.connexion.get_curseur())
        for i in self.tree.get_children():
            self.tree.delete(i)
        for i in range(len(data)):
            tags='evenrow' if i%2==0 else 'oddrow'
            self.tree.insert('','end',values=(i+1,data[i][0],data[i][1]),tags=(tags,))
        #selection d'un element dans le treeview
        self.tree.bind("<Double-Button-1>",self.selection)
        self.tree.place(x=300,y=200,height=200)

    def selection(self,event):        
        item=self.tree.selection()[0]
        self.id_domaine.set(self.tree.item(item,"values")[1])
        self.entry_nom.delete(0,END)
        self.entry_nom.insert(0,self.tree.item(item,"values")[2])


    def clear_entry(self):
        self.entry_nom.delete(0,END)
        
    def ajouter(self):
        domaine=Domaine_cours(self.entry_nom.get())
        id=domaine.get_last_id(self.connexion.get_curseur())
        if id[1]==True:
            f=id[0][0]
            
            if  id[0][0] ==None:
                f=1
            else:
                f=id[0][0]+1
    
            key=gn.generate_key("DOM",5,f)
            
            
        if domaine.save(self.connexion.get_curseur(),key):
            showinfo("Succès","Domaine ajouté avec succès")
            self.clear_entry()
            self.run()
        else:
            showerror("Erreur","Erreur lors de l'ajout du domaine")


    def modifier(self):
        domaine=Domaine_cours(self.entry_nom.get())
        if domaine.update(self.connexion.get_curseur(),self.id_domaine.get()):
            showinfo("Succès","Domaine modifié avec succès")
            self.clear_entry()
        
            self.run()
        else:
            showerror("Erreur","Erreur lors de la modification du domaine")

    def supprimer(self):

        domaine=Domaine_cours(self.entry_nom.get())
        if domaine.delete(self.connexion.get_curseur(),self.id_domaine.get()):
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