SELECT * FROM gest_ecole.eleve;
use gest_ecole;

SELECT  c.nom_cours AS nom_cours, fc.p1,fc.p2, fc.ex1,(fc.ex2+fc.p1+fc.p2) as semestre1, fc.p3, fc.p4, fc.ex2,(fc.ex2+fc.p3+fc.p4) as semestre2, (fc.ex2+fc.p1+fc.p2+fc.ex2+fc.p3+fc.p4) as Total FROM eleve e INNER JOIN inscription ins ON e.id_eleve = ins.id_eleve INNER JOIN fiche_cote fc ON ins.id_inscription = fc.id_inscription INNER JOIN cours c ON fc.id_cours = c.id_cours WHERE ins.id_inscription = 'INS0000008';



SELECT e.nom_eleve,
       AVG(
           CASE
               WHEN fc.p1 IS NOT NULL THEN fc.p1
               WHEN fc.p2 IS NOT NULL THEN fc.p2
               WHEN fc.p3 IS NOT NULL THEN fc.p3
               WHEN fc.p4 IS NOT NULL THEN fc.p4
               ELSE 0
           END
       ) AS moyenne_annuelle
FROM eleve e
INNER JOIN inscription ins ON e.id_eleve = ins.id_eleve
INNER JOIN fiche_cote fc ON ins.id_inscription = fc.id_inscription
INNER JOIN cours c ON fc.id_cours = c.id_cours
WHERE ins.id_inscription = 'INS0000008' group by(c.max_period);



SELECT e.nom_eleve,
       AVG(
           CASE
               WHEN fc.p1 IS NOT NULL THEN fc.p1
               WHEN fc.p2 IS NOT NULL THEN fc.p2
               WHEN fc.p3 IS NOT NULL THEN fc.p3
               WHEN fc.p4 IS NOT NULL THEN fc.p4
               ELSE 0
           END
       ) AS moyenne_annuelle_classe
FROM eleve e
INNER JOIN inscription ins ON e.id_eleve = ins.id_eleve
INNER JOIN fiche_cote fc ON ins.id_inscription = fc.id_inscription
INNER JOIN cours c ON fc.id_cours = c.id_cours
WHERE ins.id_class = 'Cl001'
GROUP BY e.nom_eleve;
select distinct sum(c.max_period) from cours c 
join classe cl on cl.id_class=c.id_class where c.id_class='Cl001';

select max_period from cours where id_class='Cl001';


select round( (sum(f.p1)/(select distinct sum(c.max_period) from cours c 
join classe cl on cl.id_class=c.id_class where c.id_class='Cl001')*100),2 )as p1,
round( (sum(f.p2)/(select distinct sum(c.max_period) from cours c 
join classe cl on cl.id_class=c.id_class where c.id_class='Cl001')*100),2 )as p2,Round( (sum(f.ex1)/(select distinct sum(c.max_exam) from cours c 
join classe cl on cl.id_class=c.id_class where c.id_class='Cl001')*100),2 )as ex1 from fiche_cote f 
join cours c on c.id_cours= f.id_cours join  inscription i on f.id_inscription=i.id_inscription  group by(i.id_inscription) 
where f.id_inscription='INS0000019';

SELECT
  e.nom_eleve,
  c.nom_cours,
  ROUND( (f.p1) / (c.max_period + c.max_exam) * 100, 2) AS Pourcentage
FROM fiche_cote f
JOIN inscription i ON i.id_inscription = f.id_inscription
JOIN eleve e ON e.id_eleve = i.id_eleve
JOIN cours c ON c.id_cours = f.id_cours
WHERE i.id_anne_scol = 'AN0001' AND i.id_class = 'Cl001'
ORDER BY Pourcentage DESC;



WITH RankedStudents AS (
  SELECT
    i.id_inscription,
    e.nom_eleve,
    ROUND( (sum(f.p1) / (SELECT DISTINCT SUM(c.max_period) FROM cours c
                           JOIN classe cl ON cl.id_class = c.id_class
                           WHERE c.id_class='Cl001') * 100), 2) AS p1,
    ROUND( (sum(f.p2) / (SELECT DISTINCT SUM(c.max_period) FROM cours c
                           JOIN classe cl ON cl.id_class = c.id_class
                           WHERE c.id_class='Cl001') * 100), 2) AS p2,
    ROUND( (sum(f.ex1) / (SELECT DISTINCT SUM(c.max_exam) FROM cours c
                           JOIN classe cl ON cl.id_class = c.id_class
                           WHERE c.id_class='Cl001') * 100), 2) AS ex1,
    SUM(f.p1 + f.p2 + f.ex1) / (
      SELECT SUM((c.max_period*2) + c.max_exam) FROM cours c
      JOIN classe cl ON cl.id_class = c.id_class
      WHERE c.id_class='Cl001'
    ) AS Total_Percentage
  FROM fiche_cote f
  JOIN cours c ON c.id_cours = f.id_cours
  JOIN inscription i ON f.id_inscription = i.id_inscription
  JOIN eleve e ON e.id_eleve = i.id_eleve
  WHERE i.id_anne_scol = 'AN0001' AND i.id_class = 'Cl001'
  GROUP BY i.id_inscription, e.nom_eleve
)
SELECT *, RANK() OVER (ORDER BY Total_Percentage DESC) AS Rang
FROM RankedStudents /*where*/ ;





 WITH RankedStudents AS (
    SELECT
      i.id_inscription,
      e.nom_eleve,
      ROUND(
        (sum(f.p1) / (
          SELECT DISTINCT SUM(c.max_period)
          FROM cours c
          JOIN classe cl ON cl.id_class = c.id_class
          WHERE c.id_class = 'Cl001'
        )) * 100,
        2
      ) AS p1,
      ROUND(
        (sum(f.p2) / (
          SELECT DISTINCT SUM(c.max_period)
          FROM cours c
          JOIN classe cl ON cl.id_class = c.id_class
          WHERE c.id_class = 'Cl001'
        )) * 100,
        2
      ) AS p2,
      ROUND(
        (sum(f.ex1) / (
          SELECT DISTINCT SUM(c.max_exam)
          FROM cours c
          JOIN classe cl ON cl.id_class = c.id_class
          WHERE c.id_class = 'Cl001'
        )) * 100,
        2
      ) AS ex1,
      ROUND(
        SUM(f.p1 + f.p2 + f.ex1) / (
          SELECT SUM((c.max_period * 2) + c.max_exam)
          FROM cours c
          JOIN classe cl ON cl.id_class = c.id_class
          WHERE c.id_class = 'Cl001'
        )*100,
        2
      ) AS Total_Percentage1,ROUND(
        (sum(f.p3) / (
          SELECT DISTINCT SUM(c.max_period)
          FROM cours c
          JOIN classe cl ON cl.id_class = c.id_class
          WHERE c.id_class = 'Cl001'
        )) * 100,
        2
      ) AS p3
      ,ROUND(
        (sum(f.p4) / (
          SELECT DISTINCT SUM(c.max_period)
          FROM cours c
          JOIN classe cl ON cl.id_class = c.id_class
          WHERE c.id_class = 'Cl001'
        )) * 100,
        2
      ) AS p4
      ,ROUND(
        (sum(f.ex2) / (
          SELECT DISTINCT SUM(c.max_exam)
          FROM cours c
          JOIN classe cl ON cl.id_class = c.id_class
          WHERE c.id_class = 'Cl001'
        )) * 100,
        2
      ) AS ex2,
        ROUND(
            SUM(f.p3 + f.p4 + f.ex2) / (
            SELECT SUM((c.max_period * 2) + c.max_exam)
            FROM cours c
            JOIN classe cl ON cl.id_class = c.id_class
            WHERE c.id_class = 'Cl001'
            )*100,
            2
        ) AS Total_Percentage2,
        ROUND(
            (SUM(f.p1 + f.p2 + f.ex1)+SUM(f.p3 + f.p4 + f.ex2)) / (
            SELECT SUM((c.max_period * 4) + c.max_exam*2)
            FROM cours c
            JOIN classe cl ON cl.id_class = c.id_class
            WHERE c.id_class = 'Cl001'
            )*100,
            2
        ) AS Total_Percentage
    FROM fiche_cote f
    JOIN cours c ON c.id_cours = f.id_cours
    JOIN inscription i ON f.id_inscription = i.id_inscription
    JOIN eleve e ON e.id_eleve = i.id_eleve
    WHERE i.id_anne_scol = 'AN0001' AND i.id_class = 'Cl001'
    GROUP BY i.id_inscription, e.nom_eleve
  )
  SELECT *, RANK() OVER (ORDER BY Total_Percentage DESC) AS Rang
  FROM RankedStudents;
  
  
  SELECT DISTINCT sum(c.max_period)as p1,sum(c.max_period)as p2,SUM(c.max_exam)as ex1,sum((c.max_period*2)+c.max_exam) as S1,
  sum(c.max_period)as p3,sum(c.max_period)as p4,SUM(c.max_exam)as ex2,sum((c.max_period*2)+c.max_exam) as S2,sum((c.max_period*2)+c.max_exam)*2 as total
          FROM cours c
          JOIN classe cl ON cl.id_class = c.id_class
          WHERE c.id_class = 'Cl001'