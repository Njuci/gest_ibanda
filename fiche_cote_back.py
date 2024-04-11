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
    
    def get_last_id(self,curseur):
        try:
            curseur.execute("select max(id) from fiche_cote")
            return curseur.fetchone(),True
        except Exception as e:
            showerror("Error","Error in the database "+str(e))
            return False,False
    
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
            return False
    def get_fiche_cote_by_id_cours_by_id_class_and_id_anne(self,cursor, id_cours,id_class,id_anne):
        try:
            cursor.execute("select i.id_inscription, e.nom_eleve,f.p1,f.p2,f.ex1,f.p3,f.p4,f.ex2 from fiche_cote f join cours c on  f.id_cours=c.id_cours"+" join inscription i on f.id_inscription=i.id_inscription"+
                " join anne_scolaire a on a.id =i.id_anne_scol join "+
                " classe cl on i.id_class=cl.id_class join eleve e on i.id_eleve =e.id_eleve "+
                " where  f.id_cours=%s and cl.id_class=%s and a.id=%s;", (id_cours,id_class,id_anne))
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
#     
#     def get_fiche_cote_by_id_cours_by_id_class_and_id_anne(self,cursor, id_cours,id_class,id_anne)


    def add_fiche_cote(self, cursor):
        try:
            cursor.execute("insert into fiche_cote values(%s,%s,%s,%s,%s,%s,%s,%s)", (self.id_cours, self.id_inscription, self.p1, self.p2, self.ex1, self.p3, self.p4, self.ex2))
            return True
        except Exception as e:
            showerror("Error", str(e))
            return False




    
    def get_resultat_par_eleve(self,cursor,id_inscription):
        try:
            cursor.execute("SELECT  c.nom_cours AS nom_cours, fc.p1,fc.p2, fc.ex1,(fc.ex1+fc.p1+fc.p2) as semestre1, fc.p3, fc.p4, fc.ex2,(fc.ex2+fc.p3+fc.p4) as semestre2, (fc.ex2+fc.p1+fc.p2+fc.ex2+fc.p3+fc.p4) as Total FROM eleve e INNER JOIN inscription ins ON e.id_eleve = ins.id_eleve INNER JOIN fiche_cote fc ON ins.id_inscription = fc.id_inscription INNER JOIN cours c ON fc.id_cours = c.id_cours WHERE ins.id_inscription =%s",(id_inscription,))
            return cursor.fetchall()
        except Exception as e:
            showerror("Error", str(e))
            return False

    #voir les places des eleves par rapport a la moyenne generale
    def get_place(self,cursor,id_inscription):
        try:
            cursor.execute("SELECT  e.nom_eleve, (fc.ex2+fc.p1+fc.p2+fc.ex2+fc.p3+fc.p4) as Total FROM eleve e INNER JOIN inscription ins ON e.id_eleve = ins.id_eleve INNER JOIN fiche_cote fc ON ins.id_inscription = fc.id_inscription WHERE ins.id_inscription =%s",(id_inscription,))
            return cursor.fetchall()
        except Exception as e:
            showerror("Error", str(e))
            return False


    
    def palmares_clase(self,cursor,id_class,id_anne):
        #query pour avoir le palmares
        #on va calculer le total de chaque eleve et on va les classer par ordre decroissant
        
        query= f"""
  WITH RankedStudents AS (
    SELECT
      i.id_inscription,
      e.nom_eleve,
      ROUND(
        (sum(f.p1) / (
          SELECT DISTINCT SUM(c.max_period)
          FROM cours c
          JOIN classe cl ON cl.id_class = c.id_class
          WHERE c.id_class = {id_class!r}
        )) * 100,
        2
      ) AS p1,
      ROUND(
        (sum(f.p2) / (
          SELECT DISTINCT SUM(c.max_period)
          FROM cours c
          JOIN classe cl ON cl.id_class = c.id_class
          WHERE c.id_class = {id_class!r}
        )) * 100,
        2
      ) AS p2,
      ROUND(
        (sum(f.ex1) / (
          SELECT DISTINCT SUM(c.max_exam)
          FROM cours c
          JOIN classe cl ON cl.id_class = c.id_class
          WHERE c.id_class = {id_class!r}
        )) * 100,
        2
      ) AS ex1,
      ROUND(
        SUM(f.p1 + f.p2 + f.ex1) / (
          SELECT SUM((c.max_period * 2) + c.max_exam)
          FROM cours c
          JOIN classe cl ON cl.id_class = c.id_class
          WHERE c.id_class = {id_class!r}
        )*100,
        2
      ) AS Total_Percentage1,ROUND(
        (sum(f.p3) / (
          SELECT DISTINCT SUM(c.max_period)
          FROM cours c
          JOIN classe cl ON cl.id_class = c.id_class
          WHERE c.id_class = {id_class!r}
        )) * 100,
        2
      ) AS p3
      ,ROUND(
        (sum(f.p4) / (
          SELECT DISTINCT SUM(c.max_period)
          FROM cours c
          JOIN classe cl ON cl.id_class = c.id_class
          WHERE c.id_class = {id_class!r}
        )) * 100,
        2
      ) AS p4
      ,ROUND(
        (sum(f.ex2) / (
          SELECT DISTINCT SUM(c.max_exam)
          FROM cours c
          JOIN classe cl ON cl.id_class = c.id_class
          WHERE c.id_class = {id_class!r}
        )) * 100,
        2
      ) AS ex2,
        ROUND(
            SUM(f.p3 + f.p4 + f.ex2) / (
            SELECT SUM((c.max_period * 2) + c.max_exam)
            FROM cours c
            JOIN classe cl ON cl.id_class = c.id_class
            WHERE c.id_class = {id_class!r}
            )*100,
            2
        ) AS Total_Percentage2,
        ROUND(
            (SUM(f.p1 + f.p2 + f.ex1)+SUM(f.p3 + f.p4 + f.ex2)) / (
            SELECT SUM((c.max_period * 4) + c.max_exam*2)
            FROM cours c
            JOIN classe cl ON cl.id_class = c.id_class
            WHERE c.id_class = {id_class!r} 
            )*100,
            2
        ) AS Total_Percentage
    FROM fiche_cote f
    JOIN cours c ON c.id_cours = f.id_cours
    JOIN inscription i ON f.id_inscription = i.id_inscription
    JOIN eleve e ON e.id_eleve = i.id_eleve
    WHERE i.id_anne_scol = {id_anne!r} AND i.id_class = {id_class!r}
    GROUP BY i.id_inscription, e.nom_eleve
  )
  SELECT *, RANK() OVER (ORDER BY Total_Percentage DESC) AS Rang
  FROM RankedStudents ;
  """
        try:
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            showerror("Error", str(e))
            return False
    def palmares_clase_Orientation(self,cursor,id_class,id_anne):
        #query pour avoir le palmares
        #on va calculer le total de chaque eleve et on va les classer par ordre decroissant
        
        query= f"""
  WITH RankedStudents AS (
    SELECT
      i.id_inscription,
      e.nom_eleve,
      ROUND(
        (sum(f.p1) / (
          SELECT DISTINCT SUM(c.max_period)
          FROM cours c
          JOIN classe cl ON cl.id_class = c.id_class
          WHERE c.id_class = {id_class!r}
        )) * 100,
        2
      ) AS p1,
      ROUND(
        (sum(f.p2) / (
          SELECT DISTINCT SUM(c.max_period)
          FROM cours c
          JOIN classe cl ON cl.id_class = c.id_class
          WHERE c.id_class = {id_class!r}
        )) * 100,
        2
      ) AS p2,
      ROUND(
        (sum(f.ex1) / (
          SELECT DISTINCT SUM(c.max_exam)
          FROM cours c
          JOIN classe cl ON cl.id_class = c.id_class
          WHERE c.id_class = {id_class!r}
        )) * 100,
        2
      ) AS ex1,
      ROUND(
        SUM(f.p1 + f.p2 + f.ex1) / (
          SELECT SUM((c.max_period * 2) + c.max_exam)
          FROM cours c
          JOIN classe cl ON cl.id_class = c.id_class
          WHERE c.id_class = {id_class!r}
        )*100,
        2
      ) AS Total_Percentage1,ROUND(
        (sum(f.p3) / (
          SELECT DISTINCT SUM(c.max_period)
          FROM cours c
          JOIN classe cl ON cl.id_class = c.id_class
          WHERE c.id_class = {id_class!r}
        )) * 100,
        2
      ) AS p3
      ,ROUND(
        (sum(f.p4) / (
          SELECT DISTINCT SUM(c.max_period)
          FROM cours c
          JOIN classe cl ON cl.id_class = c.id_class
          WHERE c.id_class = {id_class!r}
        )) * 100,
        2
      ) AS p4
      ,ROUND(
        (sum(f.ex2) / (
          SELECT DISTINCT SUM(c.max_exam)
          FROM cours c
          JOIN classe cl ON cl.id_class = c.id_class
          WHERE c.id_class = {id_class!r}
        )) * 100,
        2
      ) AS ex2,
        ROUND(
            SUM(f.p3 + f.p4 + f.ex2) / (
            SELECT SUM((c.max_period * 2) + c.max_exam)
            FROM cours c
            JOIN classe cl ON cl.id_class = c.id_class
            WHERE c.id_class = {id_class!r}
            )*100,
            2
        ) AS Total_Percentage2,
        ROUND(
            (SUM(f.p1 + f.p2 + f.ex1)+SUM(f.p3 + f.p4 + f.ex2)) / (        SELECT SUM((c.max_period * 4) + c.max_exam*2)
            FROM cours c
            JOIN classe cl ON cl.id_class = c.id_class
            WHERE c.id_class = {id_class!r} 
            )*100,
            2
        ) AS Total_Percentage
    FROM fiche_cote f
    JOIN cours c ON c.id_cours = f.id_cours
    JOIN inscription i ON f.id_inscription = i.id_inscription
    JOIN eleve e ON e.id_eleve = i.id_eleve
    WHERE i.id_anne_scol = {id_anne!r} AND i.id_class = {id_class!r}
    GROUP BY i.id_inscription, e.nom_eleve
  )
  SELECT *, case 
  WHEN Total_Percentage < 50 THEN 'echoue'
  WHEN Total_Percentage >= 50 AND Total_Percentage < 60 THEN 'section pedagogie'
  WHEN Total_Percentage >= 60 AND Total_Percentage < 70 THEN 'section commerciale'
  ELSE 'section scientifique' END AS Orientation
  
  
  FROM RankedStudents ;
  """
        try:
            cursor.execute(query)     
            return cursor.fetchall()
        except Exception as e:
            showerror("Error", str(e))
            return False



    def palmares(self,cursor,id_class,id_anne,id_inscrption):
        #query pour avoir le palmares
        #on va calculer le total de chaque eleve et on va les classer par ordre decroissant
        
        query= f"""
  WITH RankedStudents AS (
    SELECT
      i.id_inscription,
      e.nom_eleve,
      ROUND(
        (sum(f.p1) / (
          SELECT DISTINCT SUM(c.max_period)
          FROM cours c
          JOIN classe cl ON cl.id_class = c.id_class
          WHERE c.id_class = {id_class!r}
        )) * 100,
        2
      ) AS p1,
      ROUND(
        (sum(f.p2) / (
          SELECT DISTINCT SUM(c.max_period)
          FROM cours c
          JOIN classe cl ON cl.id_class = c.id_class
          WHERE c.id_class = {id_class!r}
        )) * 100,
        2
      ) AS p2,
      ROUND(
        (sum(f.ex1) / (
          SELECT DISTINCT SUM(c.max_exam)
          FROM cours c
          JOIN classe cl ON cl.id_class = c.id_class
          WHERE c.id_class = {id_class!r}
        )) * 100,
        2
      ) AS ex1,
      ROUND(
        SUM(f.p1 + f.p2 + f.ex1) / (
          SELECT SUM((c.max_period * 2) + c.max_exam)
          FROM cours c
          JOIN classe cl ON cl.id_class = c.id_class
          WHERE c.id_class = {id_class!r}
        )*100,
        2
      ) AS Total_Percentage1,ROUND(
        (sum(f.p3) / (
          SELECT DISTINCT SUM(c.max_period)
          FROM cours c
          JOIN classe cl ON cl.id_class = c.id_class
          WHERE c.id_class = {id_class!r}
        )) * 100,
        2
      ) AS p3
      ,ROUND(
        (sum(f.p4) / (
          SELECT DISTINCT SUM(c.max_period)
          FROM cours c
          JOIN classe cl ON cl.id_class = c.id_class
          WHERE c.id_class = {id_class!r}
        )) * 100,
        2
      ) AS p4
      ,ROUND(
        (sum(f.ex2) / (
          SELECT DISTINCT SUM(c.max_exam)
          FROM cours c
          JOIN classe cl ON cl.id_class = c.id_class
          WHERE c.id_class = {id_class!r}
        )) * 100,
        2
      ) AS ex2,
        ROUND(
            SUM(f.p3 + f.p4 + f.ex2) / (
            SELECT SUM((c.max_period * 2) + c.max_exam)
            FROM cours c
            JOIN classe cl ON cl.id_class = c.id_class
            WHERE c.id_class = {id_class!r}
            )*100,
            2
        ) AS Total_Percentage2,
        ROUND(
            (SUM(f.p1 + f.p2 + f.ex1)+SUM(f.p3 + f.p4 + f.ex2)) / (
            SELECT SUM((c.max_period * 4) + c.max_exam*2)
            FROM cours c
            JOIN classe cl ON cl.id_class = c.id_class
            WHERE c.id_class = {id_class!r} 
            )*100,
            2
        ) AS Total_Percentage
    FROM fiche_cote f
    JOIN cours c ON c.id_cours = f.id_cours
    JOIN inscription i ON f.id_inscription = i.id_inscription
    JOIN eleve e ON e.id_eleve = i.id_eleve
    WHERE i.id_anne_scol = {id_anne!r} AND i.id_class = {id_class!r}
    GROUP BY i.id_inscription, e.nom_eleve
  )
  SELECT *, RANK() OVER (ORDER BY Total_Percentage DESC) AS Rang
  FROM RankedStudents where id_inscription={id_inscrption!r};
  """
        try:
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            showerror("Error", str(e))
            return False
        
"""ROUND( (sum(f.p2) / (SELECT DISTINCT SUM(c.max_period) FROM cours c
                           JOIN classe cl ON cl.id_class = c.id_class
                           WHERE c.id_class='Cl001') * 100), 2) AS p2,
                ROUND( (sum(f.ex1) / (SELECT DISTINCT SUM(c.max_exam) FROM cours c
                           JOIN classe cl ON cl.id_class = c.id_class
                           WHERE c.id_class='{id_class}') * 100), 2) AS ex1,
                ROUND( SUM(f.p1 + f.p2 + f.ex1) / (
                SELECT SUM((c.max_period*2) + c.max_exam) FROM cours c
                JOIN classe cl ON cl.id_class = c.id_class
                WHERE c.id_class='{id_class}'
                ),2) AS Total_Percentage
                FROM fiche_cote f
                JOIN cours c ON c.id_cours = f.id_cours
                JOIN inscription i ON f.id_inscription = i.id_inscription
                JOIN eleve e ON e.id_eleve = i.id_eleve
                WHERE i.id_anne_scol = '{id_anne}' AND i.id_class = '{id_class}'
                GROUP BY i.id_inscription, e.nom_eleve);
                SELECT *, RANK() OVER (ORDER BY Total_Percentage DESC) AS Rang" 
                
        try:
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            showerror("Error", str(e))
            return False"""