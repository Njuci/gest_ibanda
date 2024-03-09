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
    
