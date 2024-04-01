"""_summary_
ajouter un cours dans la bd

 create table cours(
 id_cours int auto_increment primary key,
 nom_cours varchar(30),
 id_dom int,
 max_period int,
 max_exam int,
 id_class int,
constraint p_f_cls_cours foreign key (id_class) references classe(id_class),
constraint pf_cours_dommaine_cours foreign key (id_dom) references domaine_cours(id_dom)
 );
 en se basant sur les classes back 
    """
    
from tkinter.messagebox import showerror
class cours_back:
      def __init__(self,nom,dom,max_p,max_e,id_cls):
      
         self.nom_cours=nom
         self.id_dom=dom
         self.max_period=max_p
         self.max_exam=max_e
         self.id_class=id_cls
   
      def add_cours(self,cursor,id):
         try:
            cursor.execute("insert into cours (id_cours,nom_cours,id_dom,max_period,max_exam,id_class)  values(%s,%s,%s,%s,%s,%s)", (id,self.nom_cours, self.id_dom, self.max_period, self.max_exam, self.id_class))
            return True
         except Exception as e:
            showerror("Error", str(e))
            return False
      def get_nombre_cours_by_classe(self,cursor,id_class):
         try:
            cursor.execute("select count(*) from cours where id_class=%s", (id_class,))
            return cursor.fetchone()
         except Exception as e:
            showerror("Error", str(e))
            return False
      def get_nombre_cours_by_domaine(self,cursor,id_dom):
         try:
            cursor.execute("select count(*) from cours where id_dom=%s", (id_dom,))
            return cursor.fetchone()
         except Exception as e:
            showerror("Error", str(e))
            return False
      def get_nombre_cours_by_classe_domaine(self,cursor,id_class,id_dom):
         try:
            cursor.execute("select count(*) from cours where id_class=%s and id_dom=%s", (id_class,id_dom))
            return cursor.fetchone()
         except Exception as e:
            showerror("Error", str(e))
            return False
      
      def get_all(self,cursor):
         try:
            cursor.execute("select cr.id_cours,cr.nom_cours,cr.id_dom,dom.nom_dom,cr.max_period,cr.max_exam,cr.id_class,cl.nom from cours cr join domaine_cours dom on cr.id_dom =dom.id_dom join classe cl on cr.id_class =cl.id_class")
            return cursor.fetchall()
         except Exception as e:
            showerror("Error", str(e))
            return False
   
   
      def get_cours(self,cursor):
         try:
            cursor.execute("select * from cours")
            return cursor.fetchall()
         except Exception as e:
            showerror("Error", str(e))
            return False
   
      def get_cours_by_id(self,cursor, id_cours):
         try:
            cursor.execute("select * from cours where id_cours=%s", (id_cours,))
            return cursor.fetchone()
         except Exception as e:
            showerror("Error", str(e))
            return False
         
      def update_cours(self,cursor,id_cours):
         try:
            cursor.execute("update cours set nom_cours=%s, id_dom=%s, max_period=%s, max_exam=%s, id_class=%s where id_cours=%s", (self.nom_cours, self.id_dom, self.max_period, self.max_exam, self.id_class, id_cours))
            return True
         except Exception as e:
            showerror("Error", str(e))
            return False
         
      def delete_cours(self,cursor):
         try:
            cursor.execute("delete from cours where id_cours=%s", (self.id_cours,))
            return True
         except Exception as e:
            showerror("Error", str(e))
            return False
      def get_cours_by_classe(self,cursor,id_class):
         try:
            cursor.execute("select id_cours,nom_cours from cours where id_class=%s", (id_class,))
            return cursor.fetchall()
         except Exception as e:
            showerror("Error", str(e))
            return False,True
      def get_cours_by_domaine(self,cursor,id_dom):
         try:
            cursor.execute("select * from cours where id_dom=%s", (id_dom,))
            return cursor.fetchall()
         except Exception as e:
            showerror("Error", str(e))
            return False
      def get_cours_by_classe_domaine(self,cursor,id_class,id_dom):
         try:
            cursor.execute("select * from cours where id_class=%s and id_dom=%s", (id_class,id_dom))
            return cursor.fetchall()
         except Exception as e:
            showerror("Error", str(e))
            return False
      def get_cours_by_classe_domaine(self,cursor,id_class,id_dom):
         try:
            cursor.execute("select * from cours where id_class=%s and id_dom=%s", (id_class,id_dom))
            return cursor.fetchall()
         except Exception as e:
            showerror("Error", str(e))
            return False
      def get_cours_by_classe_domaine(self,cursor,id_class,id_dom):
         try:
            cursor.execute("select * from cours where id_class=%s and id_dom=%s", (id_class,id_dom))
            return cursor.fetchall()
         except Exception as e:
            showerror("Error", str(e))
            return False
      def get_cours_by_classe_domaine(self,cursor,id_class,id_dom):
         try:
            cursor.execute("select * from cours where id_class=%s and id_dom=%s", (id_class,id_dom))
            return cursor.fetchall()
         except Exception as e:
            showerror("Error", str(e))
            return False
      def verifier_ponderation_p_exam(self,cursor,id_cours):
         try:
            cursor.execute("select max_exam,max_period from cours where id_cours=%s", (id_cours,))
            return cursor.fetchone()
         except Exception as e:
            showerror("Error", str(e))
            return False
      def get_last_id(self,curseur):
        try:
            curseur.execute("select max(id) from cours")
            f=[curseur.fetchone(),True]
            
            return f
        except Exception as e:
            showerror("Erreur",str(e))
            return False,False
    