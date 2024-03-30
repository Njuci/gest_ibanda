from tkinter import *
from tkinter.messagebox import showerror,showinfo,showwarning
from login_back import Connexion
from user_back import User_back
import secretaire.anne_scolaire_front as anne_scolaire_front 
class Login_front:
    def __init__(self):
        self.fen=Tk()
        self.fen.title("Connexion")
        self.fen.geometry("400x300+450+200")
        self.fen.resizable(False,False)
        self.fen.configure(background='#51a596')        
        self.label_titre=Label(self.fen, borderwidth=3,relief=SUNKEN,text="Connexion",font=("Sans Serif",16),fg='white',background='#091821')
        self.label_titre.place(x=0,y=0,width=400,height=80)
        self.label_username=Label(self.fen,text=" Nom d'Utilisateur:",font=("Times",15),fg="black",background='#51a596')
        self.label_username.place(x=5,y=100,width=150)
        self.tex_username=Entry(self.fen,bd=4,font=("Arial",15))
        self.tex_username.place(x=155,y=100,width=200)
        
        self.label_mdp=Label(self.fen,text="Mot de passe :",font=("Times",15),fg="black",background='#51a596')
        self.label_mdp.place(x=5,y=150,width=150)
        self.tex_mdp=Entry(self.fen,bd=4,font=("Arial",15))
        self.tex_mdp.place(x=150,y=150,width=200)
        self.bouton_con=Button(self.fen,text='Se Connecter', background='#FF4500',font=("Times",16),fg='white',command=self.login)
        self.bouton_con.place(x=100,y=250,width=200)
    def verify_input(self):
        if self.tex_username=="" or self.tex_mdp=="":
            showwarning("Invalid input","veuillez remplir les deux champs")
            self.tex_mdp.delete(0,END)
            self.tex_username.delete(0,END)
            return False
        else:
            return True

    def login(self):
        con=Connexion()
        if con.login():
            if self.verify_input():
                user=User_back(self.tex_username.get(),self.tex_mdp.get(),"defaut")
                #Verification de l'existence de l'utilisateur
                if user.verifier(con.curseur):                    
                    
                    type=user.user_type(con.curseur)
                    if type !=False:
                        showinfo("succès","vous etes connectées")
                       
                        if type[0][0]=="secretaire":
                            self.fen.destroy()
                            anne=anne_scolaire_front.anne_scolaire(con)
                            anne.fenetre().mainloop()



                    
                else:
                    print("cursor ec")
                    

                
        
    def fenetre(self):
        return self.fen
    

