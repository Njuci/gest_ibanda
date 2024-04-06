SELECT * FROM gest_ecole.eleve;


SELECT  ins.id_inscription,e.nom_eleve, c.nom_cours AS nom_cours, fc.p1,fc.p2, fc.ex1,(fc.ex2+fc.p1+fc.p2) as semestre1, fc.p3, fc.p4, fc.ex2,(fc.ex2+fc.p3+fc.p4) as semestre2, (fc.ex2+fc.p1+fc.p2+fc.ex2+fc.p3+fc.p4) as Total
FROM eleve e
INNER JOIN inscription ins ON e.id_eleve = ins.id_eleve
INNER JOIN fiche_cote fc ON ins.id_inscription = fc.id_inscription
INNER JOIN cours c ON fc.id_cours = c.id_cours
WHERE ins.id_inscription = 'INS0000008';



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
WHERE ins.id_inscription = 'INS0000008' group by(ins.id_inscription);



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
