from tkinter.messagebox import showerror
class User_back:
    def __init__(self,username,pasword,type):
        self.username=username
        self.mdp=pasword
        self.type=type

    #verifier si le user ayant username et pass_word 
    #existe dans la base de données
    def verifier(self,curseur):
        try:
            curseur.execute("select * from utilisateur where username=%s and pass_word=%s",(self.username,self.mdp))
            if curseur.fetchone():
                return True
            else:
                return False
        except Exception as e:
            showerror("Erreur",str(e)) 
            return False
        
    def get_username(self): 
        return self.username
    def get_mdp(self):
        return self.mdp
    def get_type(self):
        return self.type
    def get_all(self,curseur):
        try:
            curseur.execute("select * from utilisateur")
            return curseur.fetchall()
        except Exception as e:
            showerror("Erreur",str(e))
            return False
    def save(self,curseur):
        try:
            curseur.execute("insert into utilisateur(username,pass_word,user_type) values(%s,%s,%s)",(self.username,self.mdp,self.type))
            return True
        except Exception as e:
            showerror("Erreur",str(e))
            return False
    def update(self,curseur,username):
        try:
            curseur.execute("update utilisateur set username=%s,pass_word=%s,user_type=%s where username=%s",(self.username,self.mdp,self.type,username))
            return True
        except Exception as e:
            showerror("Erreur",str(e))
            return False
    def delete(self,curseur,username):
        try:
            curseur.execute("delete from utilisateur where username=%s",(username,))
            return True
        except Exception as e:
            showerror("Erreur",str(e))
            return False
    
    def user_type(self,curseur):
        try:
            curseur.execute("select user_type from utilisateur where username=%s and pass_word=%s",(self.username,self.mdp))
            return curseur.fetchall()
        except Exception as e:
            showerror("Erreur",str(e))
            return False