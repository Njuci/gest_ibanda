"""

 create table assigner_class(
 id_tutilaire int,
 id_class int,
 id_anne_scolaire int,
 constraint pk_assign primary key(id_tutilaire,id_class,id_anne_scolaire),
 constraint pf_assign_titulaire foreign key (id_tutilaire) references utilisateur(id_user),
 constraint pf_id_class_assign foreign key (id_class) references classe(id_class),
 constraint pf_id_anne_assign foreign key (id_anne_scolaire) references anne_scolaire(id) 
 
 );
 liaison entre les classes utilisateur,classe et anne_scolaire
commme les classes utilisateur,classe et anne_scolaire sont des classes de base de l'application
"""
from tkinter.messagebox import showerror,showinfo
class Assigner_class_back:
    def __init__(self,id_tutilaire,id_class,id_anne_scolaire):
        self.id_tutilaire = id_tutilaire
        self.id_class = id_class
        self.id_anne_scolaire = id_anne_scolaire
    def get_all(self,curseur):
        try:
            curseur.execute("select A.id_tutilaire,B.username,A.id_class,C.nom,A.id_anne_scolaire,D.nom from assigner_class A join utilisateur B on A.id_tutilaire = B.id_user join  classe C on A.id_class = C.id_class join anne_scolaire D on A.id_anne_scolaire = D.id")
            return curseur.fetchall()
        except Exception as e:
          
            showerror("Erreur",str(e))
            return False
    def get_all_b(self,curseur,id):
        try:
            curseur.execute("select A.id_tutilaire,B.username,A.id_class,C.nom,A.id_anne_scolaire,D.nom from assigner_class A join utilisateur B on A.id_tutilaire = B.id_user join  classe C on A.id_class = C.id_class join anne_scolaire D on A.id_anne_scolaire = D.id")
            return curseur.fetchall()
        except Exception as e:
          
            showerror("Erreur",str(e))
            return False
    
    def get_all_c(self,curseur,id_user):
        try:
            curseur.execute("select A.id_tutilaire,B.username,A.id_class,C.nom,A.id_anne_scolaire,D.nom from assigner_class A join utilisateur B on A.id_tutilaire = B.id_user join  classe C on A.id_class = C.id_class join anne_scolaire D on A.id_anne_scolaire = D.id where A.id_tutilaire=%s",(id_user,))
            return curseur.fetchall()
        except Exception as e:          
            showerror("Erreur",str(e))
            return False
    def save(self,curseur):
        try:
            curseur.execute("insert into assigner_class(id_tutilaire,id_class,id_anne_scolaire) values(%s,%s,%s)",(self.id_tutilaire,self.id_class,self.id_anne_scolaire))
            return True
        except Exception as e:
            showerror("Erreur",str(e))
            
            return False
    def update(self,curseur,id_tutilaire,id_class,id_anne_scolaire):
        try:
            curseur.execute("update assigner_class set id_tutilaire=%s,id_class=%s,id_anne_scolaire=%s where id_tutilaire=%s and id_class=%s and id_anne_scolaire=%s",(self.id_tutilaire,self.id_class,self.id_anne_scolaire,
                                                                                                                                                                       id_tutilaire,id_class,id_anne_scolaire))
            return True
        except Exception as e:
            showerror("Erreur",str(e))
            return False
    def delete(self,curseur,id_tutilaire,id_class,id_anne_scolaire):
        try:
            curseur.execute("delete from assigner_class where id_tutilaire=%s and id_class=%s and id_anne_scolaire=%s",(id_tutilaire,id_class,id_anne_scolaire))
            return True
        except Exception as e:
            showerror("Erreur",str(e))
            return False
        