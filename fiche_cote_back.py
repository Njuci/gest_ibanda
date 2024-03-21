"""
 create table fiche_cote(
 id_cours int auto_increment ,
 id_inscription varchar(70),
 p1 int,
 p2 int default null,
 ex1 int default null,
 p3 int default null,
 p4 int default null,
 ex2 int default null,
 constraint pk_cote  primary key(id_cours,id_inscription),
 constraint pf_id_cours foreign key (id_cours) references cours(id_cours),
 constraint pf_id_inscription foreign key (id_inscription) references inscription(id_inscription)
 );
    en se basant sur les classes back 
    
"""

from tkinter.messagebox import showerror
class Fiche_cote_back:
    def __init__(self,id_cours,id_inscription,p1,p2,ex1,p3,p4,ex2):
        self.id_cours=id_cours
        self.id_inscription=id_inscription
        self.p1=p1
        self.p2=p2
        self.ex1=ex1
        self.p3=p3
        self.p4=p4
        self.ex2=ex2
    def add_fiche_cote(self,cursor):
        try:
            cursor.execute("insert into fiche_cote values(%s,%s,%s,%s,%s,%s,%s,%s)", (self.id_cours, self.id_inscription, self.p1, self.p2, self.ex1, self.p3, self.p4, self.ex2))
            return True
        except Exception as e:
            showerror("Error", str(e))
            return False
    def get_fiche_cote(self,cursor):
        try:
            cursor.execute("select * from fiche_cote")
            return cursor.fetchall()
        except Exception as e:
            showerror("Error", str(e))
        self.cursor.execute("select * from fiche_cote")
        return False
    def get_fiche_cote_by_id_cours_by_id_class_and_id_anne(self,cursor, id_cours,id_class,id_anne):
        try:
            cursor.execute("select * from fiche_cote where id_cours=%s and id_inscription in (select id_inscription from inscription where id_class=%s and id_anne=%s)", (id_cours,id_class,id_anne))
            return cursor.fetchall()
        except Exception as e:
            showerror("Error", str(e))
        self.cursor.execute("select * from fiche_cote where id_cours=%s and id_inscription in (select id_inscription from inscription where id_class=%s and id_anne=%s)", (id_cours,id_class,id_anne))
        return False
    def get_fiche_cote_by_id(self,cursor, id_cours,id_inscription):
        try:
            cursor.execute("select * from fiche_cote where id_cours=%s and id_inscription=%s", (id_cours,id_inscription))
            return cursor.fetchone()
        except Exception as e:
            showerror("Error", str(e))
            return False
    def update_fiche_cote(self,cursor,id_cours,id_inscription):
        try:
            cursor.execute("update fiche_cote set p1=%s, p2=%s, ex1=%s, p3=%s, p4=%s, ex2=%s where id_cours=%s and id_inscription=%s", (self.p1, self.p2, self.ex1, self.p3, self.p4, self.ex2, id_cours, id_inscription))
            return True
        except Exception as e:
            showerror("Error", str(e))
            return False
    def delete_fiche_cote(self,cursor):
        try:
            cursor.execute("delete from fiche_cote where id_cours=%s and id_inscription=%s", (self.id_cours, self.id_inscription))
            return True
        except Exception as e:
            showerror("Error", str(e))
            return False
#     de