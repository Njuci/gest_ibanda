
from tkinter import *
from side_bar_proviseur import Sidebar_proviseur
from tkinter.messagebox import showerror
from login_back import Connexion
from tkinter import ttk
from tkinter.messagebox import showinfo,showerror,showwarning
from user_back import User_back
#ajouter un interface permetttant d'ajouter, modifier, et supprimer et afficher les users
class utilisateur_front:
    def __init__(self):
        self.connexion=Connexion()
    
        self.fen=Tk()
        self.fen.title("Utilisateur")
        self.fen.geometry("800x600+150+0")
        self.fen.resizable(False,False)
        self.fen.configure(background='#51a596')
        self.side_bar=Sidebar_proviseur(self.fen,self.connexion.get_curseur())
        self.side_bar.place(x=0,y=0)
        self.label_titre=Label(self.fen, borderwidth=3,relief=SUNKEN,text="Utilisateur",font=("Sans Serif",16),fg='white',background='#091821')
        self.label_titre.place(x=300,y=0,width=500,height=80)
        #label pour le username
        self.label_username=Label(self.fen,text="Username",font=("Sans Serif",12),fg='white',background='#51a596')
        self.label_username.place(x=300,y=100)
        #champ pour le username
        self.username=StringVar()
        self.entry_username=Entry(self.fen,textvariable=self.username,font=("Sans Serif",12),fg='black',background='white')
        self.entry_username.place(x=400,y=100)
        #label pour le password
        self.label_password=Label(self.fen,text="Password",font=("Sans Serif",12),fg='white',background='#51a596')
        self.label_password.place(x=300,y=150)
        #champ pour le password
        self.password=StringVar()
        self.entry_password=Entry(self.fen,textvariable=self.password,font=("Sans Serif",12),fg='black',background='white')
        self.entry_password.place(x=400,y=150)
        #label pour le role
        self.label_role=Label(self.fen,text="Role",font=("Sans Serif",12),fg='white',background='#51a596')
        self.label_role.place(x=300,y=200)
        #combobox pour le role
        self.role=StringVar()
        self.combo_role=ttk.Combobox(self.fen,textvariable=self.role,font=("Sans Serif",12))
        self.combo_role['values']=("proviseur","titulaire","secretaire")
        self.combo_role.place(x=400,y=200)
        self.bouton_ajouter=Button(self.fen,text='Ajouter', background='#FF4500',font=("Times",16),fg='white',command=self.ajouter)
        self.bouton_ajouter.place(x=350,y=250,width=100)
        self.bouton_modifier=Button(self.fen,text='Modifier', background='#FF4500',font=("Times",16),fg='white',command=self.modifier)
        self.bouton_modifier.place(x=500,y=250,width=100)
        self.bouton_supprimer=Button(self.fen,text='Supprimer', background='#FF4500',font=("Times",16),fg='white',command=self.supprimer)
        self.bouton_supprimer.place(x=650,y=250,width=100)
        # pour afficher les utilisateurs dasn un treeview
        self.tree=ttk.Treeview(self.fen,columns=('Num','id','username','password','role'),show='headings')
        self.tree.heading('Num',text='Numéro')
        self.tree.heading('id',text='Id')
        self.tree.heading('username',text='Username')
        self.tree.heading('password',text='Password')
        self.tree.heading('role',text='Role')
        self.tree.column('Num',width=50)
        self.tree.column('id',width=50)
        self.tree.column('username',width=100)
        self.tree.column('password',width=100)
        self.tree.column('role',width=100)
        self.afficher()


        
        self.fen.mainloop()
    def get_old_username(self):
        return self.selected[2]
    def ajouter(self):
        username=self.username.get()
        password=self.password.get()
        role=self.role.get()
        user=User_back(username,password,role)
        if user.save(self.connexion.get_curseur()):
            showinfo("Ajout","Utilisateur ajouté avec succès")
            self.afficher()
        else:
            showerror("Erreur","Erreur lors de l'ajout de l'utilisateur")
    def afficher(self):
        self.tree.delete(*self.tree.get_children())
        users=User_back("","","").get_all(self.connexion.get_curseur())
        cpt=0
        print(len(users))
        for user in users:
            cpt+=1
            user=(cpt,user[0],user[1],user[2],user[3])
            self.tree.insert('','end',values=user)
        self.tree.bind('<Button-1>',self.get_selected)
        self.tree.place(x=300,y=300)
    def supprimer(self):
        username=self.username.get()
        user=User_back(username,"","")
        if user.delete(self.connexion.get_curseur()):
            showinfo("Suppression","Utilisateur supprimé avec succès")
            self.afficher()
        else:
            showerror("Erreur","Erreur lors de la suppression de l'utilisateur")
    def clear_champs(self):
        self.username.set('')
        self.password.set('')
        self.role.set('')
    #pour recuperer les champs
    def get_champs(self):
        username=self.username.get()
        password=self.password.get()
        role=self.role.get()
        return (username,password,role)
    #pour modifier un utilisateur
    def modifier(self):
        username=self.username.get()
        password=self.password.get()
        role=self.role.get()
        user=User_back(username,password,role)
        if user.update(self.connexion.get_curseur(),self.get_old_username()):
            showinfo("Modification","Utilisateur modifié avec succès")
            self.afficher()
        else:
            showerror("Erreur","Erreur lors de la modification de l'utilisateur")
    #pour recuperer un utilisateur selectionné
    def get_selected(self,event):
        self.selected=self.tree.item(self.tree.selection())['values']
        print(self.selected)
        self.username.set(self.selected[2])
        self.password.set(self.selected[3])
        self.role.set(self.selected[4])

utilisateur_front()

        
        
        