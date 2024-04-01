"""
Ce fichier est un fichier de test pour le cours de frontend
il inclut un interface graphique pour ajouter un cours, modifier un cours, supprimer un cours et afficher les cours dans une treeview

inspire de domaine_cours.py
metttant en oeuvre les classes de cours_back
les id_dom dans un combobox   
Avec le side_bar_proviseur.py
    """
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror,showinfo
from cours_backend import cours_back
from domaine_cours_back import Domaine_cours
from side_bar_proviseur import Sidebar_proviseur
from login_back import Connexion
from secretaire.classe_backend import Classe
import accessoir.generate_key as gn 
class Cours:
    def __init__(self,root):
        self.fen = root
        self.connexion=Connexion()
        self.fen.title("Gestion des cours")
        self.fen.geometry("980x900+150+0")
        self.fen.resizable(0,0)
        self.fen.configure(background='#51a596')
        self.side_bar=Sidebar_proviseur(self.fen,self.connexion)
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
        self.tree=ttk.Treeview(self.fen,columns=('Num','Id Cours','nom_cours','id_dom','max_period','max_exam','id_class'),show='headings')
        self.tree.heading('Num',text='Numéro')
        self.tree.heading('Id Cours', text='Id Cours')
        self.tree.heading('nom_cours',text='Nom du cours')
        self.tree.heading('id_dom',text='Domaine')
        self.tree.heading('max_period',text='Max period')
        self.tree.heading('max_exam',text='Max exam')
        self.tree.heading('id_class',text='Classe')
        self.tree.column('Num',width=90)
        self.tree.column("Id Cours",width=80)
        self.tree.column('nom_cours',width=100)
        self.tree.column('id_dom',width=150)
        self.tree.column('max_period',width=50)    
        self.tree.column('max_exam',width=50)
        self.tree.column('id_class',width=150)
        self.rempkir_combo_dom()    
        self.rempkir_combo_class()
        self.run()
    def rempkir_combo_dom(self):
        a=Domaine_cours("").get_all(self.connexion.get_curseur())
        data=[]
        for i in a:
            data.append(str(i[0]) +"|"+i[1])
        self.combo_dom['values']=data
        self.combo_dom.bind("<<ComboboxSelected>>",self.get_id_dom)
    def get_id_dom(self,event):
        self.id_dom=self.combo_dom.get().split("|")[0]
        
        
    def rempkir_combo_class(self):
        a=Classe("").get_all(self.connexion.get_curseur())
        data=[]
        for i in a:
            data.append(str(i[0]) +"|"+i[1])
        self.combo_class['values']=data
        self.combo_class.bind("<<ComboboxSelected>>",self.get_id_class)
    def get_id_class(self,event):
        self.id_class=self.combo_class.get().split("|")[0]
        
        
    def ajouter(self):
        cours=cours_back(self.nom_cours.get(),self.combo_dom.get().split("|")[0],self.max_period.get(),self.max_exam.get(),self.combo_class.get().split("|")[0])
        id=cours.get_last_id(self.connexion.get_curseur())
        if id[1]==True:
            f=id[0][0]
            
            if  id[0][0] ==None:
                f=1
            else:
                f=id[0][0]+1
        key=gn.generate_key("CR",5,f)
            
        
        if cours.add_cours(self.connexion.get_curseur(),key):
            self.run()
            showinfo("Info", "Cours ajouté avec succès")
        else:
            showerror("Error", "Erreur lors de l'ajout")
    def modifier(self): 
        cours=cours_back(self.nom_cours.get(),self.combo_dom.get().split("|")[0],self.max_period.get(),self.max_exam.get(),self.combo_class.get().split("|")[0])
        if cours.update_cours(self.connexion.get_curseur(),self.id_cours):
            self.run()
            showinfo("Info", "Cours modifié avec succès")
        else:
            showerror("Error", "Erreur lors de la modification")
    
    def supprimer(self):
        cours=cours_back(self.nom_cours.get(),self.combo_dom.get(),self.max_period.get(),self.max_exam.get(),self.combo_class.get())
        if cours.delete_cours(self.connexion.get_curseur()):
            self.run()
            showinfo("Info", "Cours supprimé avec succès")
        else:
            showerror("Error", "Erreur lors de la suppression")
    def run(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for i in cours_back("","","","","").get_all(self.connexion.get_curseur()):
            cpt=1
            
            self.tree.insert("", "end", values=(cpt,i[0],i[1],i[2]+'|'+i[3],i[4],i[5],i[6]+'|'+i[7]))
            cpt=cpt+1
        self.tree.place(x=250,y=400)
        self.tree.bind('<ButtonRelease-1>', self.get_old_selection)
        
        
    def get_old_selection(self,event):
        self.selected=self.tree.item(self.tree.selection()[0])['values']
        self.nom_cours.delete(0,END)
        self.nom_cours.insert(0,self.selected[2])
        self.combo_dom.delete(0,END)
        self.combo_dom.insert(0,self.selected[3])
        self.max_period.delete(0,END)
        self.max_period.insert(0,self.selected[4])
        self.max_exam.delete(0,END)
        self.max_exam.insert(0,self.selected[5])
        self.combo_class.delete(0,END)
        self.combo_class.insert(0,self.selected[6])
        self.id_cours=self.selected[1]
    def fenetre(self):
        return self.fen

if __name__=='__main__' :
    s=Cours(Tk())
    s.fenetre().mainloop()   
    
        