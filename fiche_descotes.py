#ense basant sur les formulaire 
from tkinter import *
import side_bar_tutulaire
from tkinter.messagebox import showerror,showinfo
from tkinter import ttk
import treeEdit
from fiche_cote_back import Fiche_cote_back
from login_back import Connexion
from cours_backend import cours_back

class fiche_descotes:
    def __init__(self,connection):
        self.connexion=connection
    
        self.fen=Tk()
        self.new_values=None
    
        self.fen.title("Fiche des cotes du cours ")
        self.fen.geometry("900x600+150+0")
        self.fen.resizable(False,False)
        self.fen.configure(background='#51a596')
        self.side_bar=side_bar_tutulaire.SideBar_tutulaire(self.fen,self.connexion)
        self.side_bar.place(x=0,y=0)
        self.label_titre=Label(self.fen, borderwidth=3,relief=SUNKEN,text="Fiche des cotes",font=("Sans Serif",16),fg='white',background='#091821')
        self.label_titre.place(x=300,y=0,width=500,height=80)
        self.label_nom=Label(self.fen,text="Cours",font=("Times",15),fg="black",background='#51a596')
        self.label_nom.place(x=305,y=100,width=150)
        #combobox pour choisir le cours
        self.cours=ttk.Combobox(self.fen,font=("Arial",15))
        self.cours.place(x=550,y=100,width=200)
        self.remplir_combobox()
        #tableau pour afficher les cotes
        self.tree=treeEdit.TreeviewEditable(self.fen,show='headings',)
        self.tree['columns'] = ('IDInscription  Nom', 'P1', 'P2','EX1','P3','P4','EX2')
        self.tree.heading('#0', text='nuemros')
        self.tree.heading('IDInscription  Nom', text='IDInscription  Nom',anchor='center')
        self.tree.heading('P1', text='P1')
        self.tree.heading('P2', text='P2')
        self.tree.heading('EX1', text='EX1')
        self.tree.heading('P3', text='P3')
        self.tree.heading('P4', text='P4')
        self.tree.heading('EX2', text='EX2')
        self.tree.column('#0', width=40)
        self.tree.column('IDInscription  Nom', width=150)
        self.tree.column('P1', width=40)
        self.tree.column('P2', width=40)
        self.tree.column('EX1', width=40)
        self.tree.column('P3', width=40)
        self.tree.column('P4', width=40)
        self.tree.column('EX2', width=40)
        self.tree.place(x=305, y=150,height=350)
        #scrollbar
        #self.scrol=ttk.Scro
        self.btn_imprimer=Button(self.fen,text="Imprimer",font=("Arial",15),background='#FF4500',command=self.imprimer)
        self.btn_imprimer.place(x=305,y=505,width=190, height=40)
        self.cours.bind("<<ComboboxSelected>>",self.afficher)
        #self.afficher()
        self.tree.new_values_callback=self.avoir_nouvelles_valeurs
        
        
    def avoir_nouvelles_valeurs(self,values):
        self.new_values=values
        print(self.new_values)
        self.decomposer_valeur(self.cours,self.new_values)
        
    def remplir_combobox(self):
        #remplir la combobox avec les cours de la classe
        cour=cours_back("","",0,0,0)
        a=cour.get_cours_by_classe(self.connexion.curseur,1)
        self.cours['values']=str(a[0][0])+'|'+a[0][1]
    
    def fenetre(self):
      return self.fen
    def decomposer_valeur(self,cours,values):
        id_cours=cours.get().split('|')[0]
        id_inscription=values[0].split('|')[0]
        p1=self.new_values[1]
        p2=self.new_values[2]
        ex1=self.new_values[3]
        p3=self.new_values[4]
        p4=self.new_values[5]
        ex2=self.new_values[6]
        liste_cotes=[p1,p2,ex1,p3,p4,ex2]
        liste=[]
        #convertir les valeur en entier et remplacer les valeurs nulles par 0 
        #et si la conversion echoue remplacer 
             
        for i in range(len(liste_cotes)):
            if liste_cotes[i]=='':
                liste.append(0)
            else:
                if self.is_valid_int(liste_cotes[i]):
                    liste.append(int(liste_cotes[i]))
                else:
                    showerror("Erreur","Veuillez entrer des valeurs numériques, la valeur entrée est "+liste_cotes[i]+" qui est remis à 0")
                    liste.append(0)
        
        
        fiche=Fiche_cote_back(id_cours,id_inscription,liste[0],liste[1],liste[2],liste[3],liste[4],liste[5])
        if fiche.get_fiche_cote_by_id(self.connexion.curseur,id_cours,id_inscription):
            if fiche.update_fiche_cote(self.connexion.curseur,id_cours,id_inscription):
                self.afficher(None)
                print("mise à jour réussie")
            else:
                print("mise à jour échouée")

    def is_valid_int(self,text):
        try:
            int(text)
            return True
        except ValueError:
            return False
        
    def afficher(self,event):
        fiche=Fiche_cote_back(0,0,0,0,0,0,0,0)
        a=fiche.get_fiche_cote_by_id_cours_by_id_class_and_id_anne(self.connexion.curseur,self.cours.get().split('|')[0],1,1)
        #effacer les anciennes valeurs
        for i in self.tree.get_children():
            self.tree.delete(i)
            
        for i in a:
            self.tree.insert('', 'end', values=(str(i[0])+'|'+str(i[1]),        str(i[2]), str(i[3]),
                                                      str(i[4]),str(i[5]),
                                                      str(i[6]),str(i[7])))

    def imprimer(self):
        pass
f=fiche_descotes(Connexion())
f.fenetre().mainloop()
        