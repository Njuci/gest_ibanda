""""

create table domaine_cours(
id_dom int auto_increment primary key,
nom_dom varchar(30) unique
 );
 

"""
from tkinter.messagebox import showerror,showinfo

class Domaine_cours:
    def __init__(self, nom_dom):
        self.nom_dom = nom_dom
    def get_all(self,curseur):
        try:
            curseur.execute("select id_dom,nom_dom from domaine_cours order by(id_dom)")
            return curseur.fetchall()
        except Exception as e:
            showerror("Erreur",str(e))
            return False
    def get_nom(self):
        return self.nom_dom
    def save(self,curseur,id):
        try:
            curseur.execute("insert into domaine_cours(id_dom,nom_dom) values(%s,%s)",(id,self.nom_dom,))
            return True
        except Exception as e:
            showerror("Erreur",str(e))
            return False
    def update(self,curseur,id):
        try:
            curseur.execute("update domaine_cours set nom_dom=%s where id_dom=%s",(self.nom_dom,id))
            return True
        except Exception as e:
            showerror("Erreur",str(e))
            return False
    def delete(self,curseur,id):
        try:
            curseur.execute("delete from domaine_cours where id_dom=%s",(id,))
            return True
        except Exception as e:
            showerror("Erreur",str(e))
            return False
    
    def get_last_id(self,curseur):
        try:
            curseur.execute("select max(id) from domaine_cours")
            f=[curseur.fetchone(),True]
            
            return f
        except Exception as e:
            showerror("Erreur",str(e))
            return False,False
    def get_id(self,curseur):
        try:
            curseur.execute("select id_dom from domaine_cours where nom_dom=%s",(self.nom_dom,))
            return curseur.fetchone()[0]
        except Exception as e:
            showerror("Erreur",str(e))
            return False 
    def get_nom(self,curseur):
        try:
            curseur.execute("select nom_dom from domaine_cours where id_dom=%s",(self.nom_dom,))
            return curseur.fetchone()[0]
        except Exception as e:
            showerror("Erreur",str(e))
            return False
        