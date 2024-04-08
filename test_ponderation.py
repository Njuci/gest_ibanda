import fiche_cote_back as fiche_cote_back
import login_back as login_back
import secretaire.anne_scolaire_back as amme_scolaire_back


conexion=login_back.Connexion()
anne_scolaire=amme_scolaire_back.AnneScolaire("AN0001",1)

data=[]
for i in anne_scolaire.get_nom_bd(conexion.get_curseur(),'AN0001'):
    data.append(i)
    

print(data)


# Compare this snippet from fiche_descotes.py:

iche=fiche_cote_back.Fiche_cote_back("","",0,0,0,0,0,0)


for i in iche.palmares_clase(conexion.get_curseur(),'Cl001','AN0001'):
    print(i)
# Compare this snippet from bulettin.py:



def get_ranked_students(connection,id_anne, id_class):

  """
  Fonction qui execute la requête SQL avec f-strings et retourne les étudiants classés.

  Args:
    id_anne (str): L'année scolaire.
    id_class (str): La classe.

  Returns:
    list: Une liste de tuples contenant les informations des étudiants et leur rang.
  """

  sql_query = f"""
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
  FROM RankedStudents;
  """

  # Connexion à la base de données
  # Création d'un curseur
  cursor =connection.get_curseur()
  print(sql_query)
  # Exécution de la requête
  cursor.execute(sql_query)

  # Récupération des résultats
  results = cursor.fetchall()

  # Fermeture du curseur
  return results

# Exemple d'utilisation
id_anne = "AN0001"
id_class = "Cl001"
ranked_students = get_ranked_students(conexion,id_anne, id_class)

# Affichage des résultats
for row in ranked_students:
  print(row)
