"""

create table classe(
id_class int auto_increment primary key,
nom varchar(30) unique
);

faire une classe Classe qui a les méthodes suivantes:
- get_all qui retourne toutes les classes
- save qui ajoute une classe
- update qui modifie une classe
- delete qui supprime une classe
- get_nom qui retourne le nom de la classe
- get_id qui retourne l'id de la classe
"""
class Classe:
    def __init__(self, nom):
        self.nom =nom
        self.encours=None
    def get_all(self,curseur):
        try:
            curseur.execute("select * from classe")
            return curseur.fetchall()
        except Exception as e:
            print(str(e))
            return False
    def get_nom(self):
        return self.nom
    def save(self,curseur):
        try:
            curseur.execute("insert into classe(nom) values(%s)",(self.nom,))
            return True
        except Exception as e:
            print(str(e))
            return False
    def update(self,curseur,id):
        try:
            curseur.execute("update classe set nom=%s where id_class=%s",(self.nom,id))
            return True
        except Exception as e:
            print(str(e))
            return False
    def delete(self,curseur):
        try:
            curseur.execute("delete from classe where nom=%s",(self.nom,))
            return True
        except Exception as e:
            print(str(e))
            return False
    def get_id(self,curseur):
        try:
            curseur.execute("select id_class from classe where nom=%s",(self.nom,))
            return curseur.fetchone()[0]
        except Exception as e:
            print(str(e))
            return False
    def get_nom(self,curseur):
        try:
            curseur.execute("select nom from classe where id_class=%s",(self.nom,))
            return curseur.fetchone()[0]
        except Exception as e:
            print(str(e))
            return False
