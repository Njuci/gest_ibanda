"""
creer une interface graphique pour AnneScolaire
avec tkinter
en se basant sur le code de login_front.py et ajoutant les fonctionnalités de AnneScolaire dans anne_scolaire_back.py
et en affichant les années scolaires dans une triview
l'attribut encours est un boolean qui indique si l'année scolaire est en cours ou pas   
et le bouton ajouter permet d'ajouter une année scolaire
le bouton ajouter doit appeler la méthode ajouter de la classe AnneScolaire
Un bouton radio doit permettre de choisir si l'année scolaire est en cours ou pas
et la méthode ajouter doit appeler la méthode save de la classe AnneScolaire
et la méthode save doit appeler la méthode execute de la classe curseur
et la méthode execute doit exécuter la requête sql d'insertion
et la méthode execute doit retourner True si l'insertion a réussi
et la méthode execute doit retourner False si l'insertion a échoué
et la méthode save doit retourner True si l'insertion a réussi
"""
from tkinter import *
from tkinter.messagebox import showerror,showinfo,showwarning
from anne_scolaire_back import AnneScolaire
from tkinter.ttk import Treeview
#from side_bar import SideBar   
""" 
pour eviter l'erreur d'importation circulaire j'importe d'une autre manière

"""
import side_bar 
class anne_scolaire:
    def __init__(self,connection):
        self.connexion=connection
    
        self.fen=Tk()
    
        self.fen.title("Année scolaire")
        self.fen.geometry("800x600+150+0")
        self.fen.resizable(False,False)
        self.fen.configure(background='#51a596')
        self.side_bar=side_bar.SideBar(self.fen,self.connexion)
        self.side_bar.place(x=0,y=0)
        self.label_titre=Label(self.fen, borderwidth=3,relief=SUNKEN,text="Année scolaire",font=("Sans Serif",16),fg='white',background='#091821')
        self.label_titre.place(x=300,y=0,width=500,height=80)
        self.label_nom=Label(self.fen,text="Nom de l'année scolaire:",font=("Times",15),fg="black",background='#51a596')
        self.label_nom.place(x=305,y=100,width=250)
        self.tex_nom=Entry(self.fen,bd=4,font=("Arial",15))
        self.tex_nom.place(x=550,y=100,width=200)
        self.label_encours=Label(self.fen,text="En cours:",font=("Times",15),fg="black",background='#51a596')
        self.label_encours.place(x=305,y=150,width=250)
        self.radio_encours=BooleanVar()
        self.radio_encours.set(False)
        self.radio_encours1=Radiobutton(self.fen,text="Oui",variable=self.radio_encours,value=True,font=("Times",15),fg="black",background='#51a596')
        self.radio_encours1.place(x=550,y=150)  
        self.radio_encours2=Radiobutton(self.fen,text="Non",variable=self.radio_encours,value=False,font=("Times",15),fg="black",background='#51a596')
        self.radio_encours2.place(x=650,y=150)
        self.bouton_ajouter=Button(self.fen,text='Ajouter', background='#FF4500',font=("Times",16),fg='white',command=self.ajouter)
        self.bouton_ajouter.place(x=350,y=200,width=100)
        self.bouton_modifier=Button(self.fen,text='Modifier', background='#FF4500',font=("Times",16),fg='white',command=self.modify)
        self.bouton_modifier.place(x=500,y=200,width=100)
        self.bouton_supprimer=Button(self.fen,text='Supprimer', background='#FF4500',font=("Times",16),fg='white',command=self.modify)
        self.bouton_supprimer.place(x=650,y=200,width=100)
        self.selected_id=IntVar()
        self.selected_annee=StringVar()
        self.selected_statut=BooleanVar()
        self.E=None

        self.tree=Treeview(self.fen, columns=('Id','Designation','Statut'), show='headings')
        self.tree.heading('Id', text='Id')
        self.tree.heading('Designation', text='Désignation')
        self.tree.heading('Statut', text='Statut')
        self.tree.column('Id',width=20)
        self.tree.column('Designation',width=100)
        self.tree.column('Statut',width=50)
        #colorer les cases du treeview en fonction de la valeur de la colonne statut
        
        
        self.tree.tag_configure('green', background="green")
        self.tree.tag_configure('red', background="red")
        self.remplir_tree()
        self.tree.place(x=350,y=250)
    def supprier(self):
        self.get_entry()
        annee=AnneScolaire(self.selected_annee,self.selected_statut)
        if annee.delete(self.connexion.get_curseur()):
            showinfo("succès","l'année scolaire a été supprimée")
            self.remplir_tree()
        else:
            showerror("Erreur","l'année scolaire n'a pas été supprimée")
    
    def modify(self):
        self.get_entry()
        annee=AnneScolaire(self.selected_annee,self.selected_statut)
        if annee.update(self.connexion.get_curseur(),self.selected_id):
            showinfo("succès","l'année scolaire a été modifiée")
            self.remplir_tree()
        else:
            showerror("Erreur","l'année scolaire n'a pas été modifiée")
    def ajouter(self):

        annee=AnneScolaire(self.tex_nom.get(),self.radio_encours.get())
        if annee.save(self.connexion.get_curseur()):
            showinfo("succès","l'année scolaire a été ajoutée")
            self.remplir_tree()
        else:
            showerror("Erreur","l'année scolaire n'a pas été ajoutée")
    # colorer les cases du treeview en fonction de la valeur de la colonne statut
        
    def apply_conditional_formatting(self,value):
        # Votre condition ici (par exemple, si value == "actif")
        return 'green' if value == 'V' else 'red'
    
    def remplir_tree(self):
        a=AnneScolaire("FF",True)

        data=a.get_all(self.connexion.get_curseur())
        if data is not None:
            self.tree.delete(*self.tree.get_children())
            #afficher v si l'année scolaire est en cours et F sinon         
                                
            for i, row in enumerate(data):
              #colorer vert la case si l'année scolaire est en cours sinon la colorer en rouge
                if row[2]==1:
                    E='V'
                else:
                    E='F'
                #colorer vert la case si l'année scolaire est en cours sinon la colorer en rouge
                
                self.tree.insert('','end',values=(row[0],row[1],E),tags=(self.apply_conditional_formatting(E),))
                
        
            self.tree.bind('<ButtonRelease-1>',self.get_table_selected_row)

    def fenetre(self):
        return self.fen
    def clean_entry(self):
        self.tex_nom.delete(0,END)
        self.radio_encours.set(False)

    def get_entry(self):
        
        self.selected_annee=self.tex_nom.get()
        self.selected_statut=self.radio_encours.get()
    #voir la ligne selectionnée dans le treeview
    #Creation de la section de tableau
    def get_table_selected_row(self,event):
        self.selected_id=self.tree.item(self.tree.selection())['values'][0]        
        self.clean_entry()
        row=self.tree.item(self.tree.selection())
        self.tex_nom.insert(0,row['values'][1])
        self.radio_encours.set(True if row['values'][2]=='V' else False)
        

    def voir(self):
        print(self.tree.item(self.tree.selection()))
