"""
comme dans le ficjier anne_scolaire_backend.py on a creer une classe inscription_back qui est une classe de liaison entre l'interface et la base de donnees
create table inscription(
id_inscription varchar(70) unique,
id_eleve int,
id_anne_scol int,
id_class int,
constraint p_k_inscription primary key(id_eleve,id_anne_scol,id_class),
constraint p_f_idel_ins foreign key (id_eleve) references eleve(id_eleve),
constraint p_f_idansc_insc foreign key (id_anne_scol) references anne_scolaire(id),
constraint p_f_id_classe foreign key(id_class) references classe(id_class)

);

en se referant a la table inscription on peut dire que la classe inscription est une classe de liaison entre les classes eleve,anne_scolaire et classe
cette classe est une classe de liaison entre les classes eleve,anne_scolaire et classe
comme les classes eleve,anne_scolaire et classe sont des classes de base de l'application
"""
from tkinter import messagebox
class Inscription_back:
    def __init__(self,id_eleve,id_anne_scol,id_class):
        self.id_inscription = None
        self.id_eleve = id_eleve
        self.id_anne_scol = id_anne_scol
        self.id_class = id_class
   
    def get_all(self,curseur):
        try:
            curseur.execute("select inscription.id_eleve, eleve.nom_eleve,inscription.id_anne_scol,inscription.id_class,cl.nom ,inscription.id_inscription from eleve"+
                            " join inscription on inscription.id_eleve=eleve.id_eleve join classe cl on cl.id_class=inscription.id_class")
            
            return curseur.fetchall()
        except Exception as e:
            print(str(e))
            return False
    #get last id
    #
    def get_last_id(self,curseur):
        try:
            curseur.execute("select max(id) from inscription")
            return curseur.fetchone(),True
        except Exception as e:
            messagebox.showerror("Error","Error in the database "+str(e))
            return False,False
    
    
    def save(self,curseur,id):
        try:
            curseur.execute("insert into inscription(id_inscription,id_eleve,id_anne_scol,id_class) values(%s,%s,%s,%s)",(id,self.id_eleve,self.id_anne_scol,self.id_class))
            return True
        except Exception as e:
            print(str(e))
            return False
    def update(self,curseur,id):
        try:
            curseur.execute("update inscription set id_inscription=%s,id_eleve=%s,id_anne_scol=%s,id_class=%s where id_inscription=%s",(self.id_inscription,self.id_eleve,self.id_anne_scol,self.id_class,id))
            return True
        except Exception as e:
            print(str(e))
            return False
    def delete(self,curseur):
        try:
            curseur.execute("delete from inscription where id_inscription=%s",(self.id_inscription,))
            return True
        except Exception as e:
            print(str(e))
            return False
    def get_id_inscription(self):
        return self.id_inscription
    def get_id_eleve(self):
        return self.id_eleve
    def get_id_anne_scol(self):
        return self.id_anne_scol
    def get_id_class(self):
        return self.id_class
    def get_id_inscription(self,curseur):
        try:
            curseur.execute("select id_inscription from inscription where id_eleve=%s and id_anne_scol=%s and id_class=%s",(self.id_eleve,self.id_anne_scol,self.id_class))
            return curseur.fetchone()[0]
        except Exception as e:
            print(str(e))
            return False
    # faire apparairaitre les eleves  inscrits dans , leurs noms
    # faire apparaitre les eleves inscrits dans
        #ne classe pour une annee scolaire donnee et les afficher dans un list rn faisant la jointure entre les tables eleve et inscription
    def get_eleve_inscrit(self,curseur):
        try:
            curseur.execute("select * from inscription where id_anne_scol=%s and id_class=%s",(self.id_anne_scol,self.id_class))
            return curseur.fetchall()
        except Exception as e:
            print(str(e))
            return False
    

    # les gets des elèves avec leurs nom

    def get_eleve_inscrit(self,curseur):
        try:
            curseur.execute("select * from inscription where id_anne_scol=%s and id_class=%s",(self.id_anne_scol,self.id_class))
            return curseur.fetchall()
        except Exception as e:
            print(str(e))
            return False
    #afficher les noms des  eleves inscrits dans une classe pour une annee scolaire donnee
    def get_eleve_inscrit(self,curseur):
        try:
            curseur.execute("select nom from inscription,eleve where id_anne_scol=%s and id_class=%s and inscription.id_eleve=eleve.id_eleve",(self.id_anne_scol,self.id_class))
            return curseur.fetchall()
        except Exception as e:
            print(str(e))
            return False
    #afficher les noms des  eleves inscrits dans une classe pour une annee scolaire donnee
        
    def get_eleve_inscrit(self,curseur):
        try:
            curseur.execute("select nom from inscription,eleve where id_anne_scol=%s and id_class=%s and inscription.id_eleve=eleve.id_eleve",(self.id_anne_scol,self.id_class))
            return curseur.fetchall()
        except Exception as e:
            print(str(e))
            return False