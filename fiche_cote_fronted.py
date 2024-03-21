"""
faire une interface graphique pour ajouter un cours, modifier un cours, supprimer un cours et afficher les cours dans une treeview
inspire de domaine_cours.py
metttant en oeuvre les classes de cours_back
ou on pourra choisir le classe à coté de chaque cours
que le treeview soit editable et la colone des elebves soit remplie automatiquement avec les eleves de la classe choisie pour chaque cours
Avec le side_bar_prof.py


    """
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror,showinfo
from fiche_cote_back import fiche_cote_back
from cours_backend import cours_back
from domaine_cours_back import Domaine_cours
from side_bar_proviseur import Sidebar_proviseur
from login_back import Connexion

class fiche_cote:
    def __init__(self):
        self.fen = Tk()
        self.connexion=Connexion()
        self.fen.title("Gestion des cours")
        self.fen.geometry("800x900+150+0")
        self.fen.resizable(0,0)
        self.fen.configure(background='#51a596')
        self.side_bar=Sidebar_proviseur(self.fen,self.connexion.get_curseur())
        self.side_bar.place(x=0,y=0)
        self.label_titre=Label(self.fen, borderwidth=3,relief=SUNKEN,text="Gestion des cours",font=("Sans Serif",16),fg='white',background='#091821')
        self.label_titre.place(x=300,y=0,width=500,height=80)
        self.label_nom_cours=Label(self.fen,text="Nom du cours",font=("Sans Serif",12),fg='white',background='#51a596')
        self.label_nom_cours.place(x=300,y=100)
        self.nom_cours=Entry(self.fen,font=("Sans Serif",12))
        self.nom_cours.place(x=400,y=100)
        self.label_dom=Label(self.fen,text="Domaine",font=("Sans Serif",12),fg='white',background='#51a596')
        self.label_dom.place(x=300,y=150)
        self.combo_dom=ttk.Combobox(self.fen,font=("Sans Serif",12))
        self.combo_dom.place(x=400,y=150)
        self.label_max_period=Label(self.fen,text="Max period",font=("Sans Serif",12),fg='white',background='#51a596')
        self.label_max_period.place(x=300,y=200)
        self.max_period=Entry(self.fen,font=("Sans Serif",12))
        self.max_period.place(x=400,y=200)
        self.label_max_exam=Label(self.fen,text="Max exam",font=("Sans Serif",12),fg='white',background='#51a596')
        self.label_max_exam.place(x=300,y=250)
        self.max_exam=Entry(self.fen,font=("Sans Serif",12))
        self.max_exam.place(x=400,y=250)
        self.label_class=Label(self.fen,text="Classe",font=("Sans Serif",12),fg='white',background='#51a596')
        self.label_class.place(x=300,y=300)
        self.combo_class=ttk.Combobox(self.fen,font=("Sans Serif",12))
        self.combo_class.place(x=400
                                    ,y=300) 
        self.bouton_ajouter=Button(self.fen,text='Ajouter', background='#FF4500',font=("Times",16),fg='white',command=self.ajouter)
        self.bouton_ajouter.place(x=350,y=350,width=100)
        self.bouton_modifier=Button(self.fen,text='Modifier', background='#FF4500',font=("Times",16),fg='white',command=self.modifier)
        self.bouton_modifier.place(x=500,y=350,width=100)
        self.bouton_supprimer=Button(self.fen,text='Supprimer', background='#FF4500',font=("Times",16),fg='white',command=self.supprimer)
        self.bouton_supprimer.place(x=650,y=350,width=100)
        self.tree=ttk.Treeview(self.fen,columns=('Num','nom_cours','id_dom','max_period','max_exam','id_class'),show='headings')
        #le treeview soit editable et la colone des elebves soit remplie automatiquement avec les eleves de la classe choisie pour chaque cours
        self.tree.heading('Num',text='Numéro')
        self.tree.heading('nom_cours',text='Nom du cours')
        self.tree.heading('id_dom',text='Domaine')
        self.tree.heading('max_period',text='Max period')
        self.tree.heading('max_exam',text='Max exam')
        self.tree.heading('id_class',text='Classe')
        self.tree.column('Num',width=50)
        self.tree.column('nom_cours',width=100)
        self.tree.column('id_dom',width=100)
        self.tree.column('max_period',width=100)
        self.tree.column('max_exam',width=100)
        self.tree.column('id_class',width=100)
        self.rempkir_combo_dom()
        self.rempkir_combo_class()
        self.run()
    def rempkir_combo_dom(self):
        a=Domaine_cours("").get_all(self.connexion.get_curseur())
        self.combo_dom['values']=[i[0] for i in a]
    def rempkir_combo_class(self):
        a=Classe("").get_all(self.connexion.get_curseur())
        self.combo_class['values']=[i[0] for i in a]
    def ajouter(self):  
        a=cours_back(self.nom_cours.get(),self.combo_dom.get(),self.max_period.get(),self.max_exam.get(),self.combo_class.get())
        if a.add_cours(self.connexion.get_curseur()):
            showinfo("Information", "Cours ajouté avec succès")
            self.run()
        else:
            showerror("Error", "Erreur d'ajout")
    def modifier(self):
        a=cours_back(self.nom_cours.get(),self.combo_dom.get(),self.max_period.get(),self.max_exam.get(),self.combo_class.get())
        if a.update_cours(self.connexion.get_curseur(),self.id_cours):
            showinfo("Information", "Cours modifié avec succès")
            self.run()
        else:
            showerror("Error", "Erreur de modification")
    def supprimer(self):
        a=cours_back(self.nom_cours.get(),self.combo_dom.get(),self.max_period.get(),self.max_exam.get(),self.combo_class.get())
        if a.delete_cours(self.connexion.get_curseur()):
            showinfo("Information", "Cours supprimé avec succès")
            self.run()
        else:
            showerror("Error", "Erreur de suppression")
    def run(self):
        a=cours_back("","","","","","")
        data=a.get_cours(self.connexion.get_curseur())
        self.tree.delete(*self.tree.get_children())
        for i in data:
            self.tree.insert('','end',values=i)
        self.tree.place(x=300,y=400,width=500,height=400)
        self.tree.bind('<ButtonRelease-1>',self.get)
    def get(self,event):
        self.id_cours=self.tree.item(self.tree.selection())['values'][0]
        self.nom_cours.delete(0,END)
        self.nom_cours.insert(0,self.tree.item(self.tree.selection())['values'][1])
        self.combo_dom.set(self.tree.item(self.tree.selection())['values'][2])
        self.max_period.delete(0,END)
        self.max_period.insert(0,self.tree.item(self.tree.selection())['values'][3])
        self.max_exam.delete(0,END)
        self.max_exam.insert(0,self.tree.item(self.tree.selection())['values'][4])
        self.combo_class.set(self.tree.item(self.tree.selection())['values'][5])
fiche_cote().fen.mainloop()
