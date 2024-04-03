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
    
    def get_last_id(self,curseur):
        try:
            curseur.execute("select max(id) from utilisateur")
            f=[curseur.fetchone(),True]
            
            return f
        except Exception as e:
            showerror("Erreur",str(e))
            return False,False
        
    def get_username(self): 
        return self.username
    def get_mdp(self):
        return self.mdp
    def get_type(self):
        return self.type
    def get_all(self,curseur):
        try:
            curseur.execute("select * from utilisateur order by id_user")
            return curseur.fetchall()
        except Exception as e:
            showerror("Erreur",str(e))
            return False
    def get_all_tutilaire(self,curseur):
        try:
            curseur.execute("select * from utilisateur where user_type='tutilaire' order by id_user")
            return curseur.fetchall()
        except Exception as e:
            showerror("Erreur",str(e))
            return False

    
    
    def save(self,curseur,id):
        try:
            curseur.execute("insert into utilisateur(id_user,username,pass_word,user_type) values(%s,%s,%s,%s)",(id,self.username,self.mdp,self.type))
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
            curseur.execute("select user_type,id_user from utilisateur where username=%s and pass_word=%s",(self.username,self.mdp))
            return curseur.fetchall()
        except Exception as e:
            showerror("Erreur",str(e))
            return False