"""

 create table anne_scolaire(
 id int auto_increment  primary  key,
 nom varchar (9) unique,
 encours boolean);
 
"""
"""class AnneScolaire:"""
class AnneScolaire:
    def __init__(self, nom, encours):
        self.nom = nom
        self.encours = encours
    def get_all(self,curseur):
        try:
            curseur.execute("select * from anne_scolaire")
            return curseur.fetchall()
        except Exception as e:
            print(str(e))
            return False
    
    def get_nom(self):
        return self.nom
    def get_encours(self):
        return self.encours
    def save(self,curseur):
        try:
            curseur.execute("insert into anne_scolaire(nom,encours) values(%s,%s)",(self.nom,self.encours))
            return True
        except Exception as e:
            print(str(e))
            return False
    def update(self,curseur,id):
        try:
            curseur.execute("update anne_scolaire set nom=%s,encours=%s where id=%s",(self.nom,self.encours,id))
            curseur.execute("update anne_scolaire set encours=%s where nom=%s",(self.encours,self.nom))
            return True
        except Exception as e:
            print(str(e))
            return False
    #Effacer une année scolaire sans effacer les classes et les élèves ET les notes
    def delete(self,curseur):
        try:
            curseur.execute("delete from anne_scolaire where nom=%s",(self.nom,))
            return True
        except Exception as e:
            print(str(e))
            return False