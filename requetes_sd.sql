USE gest_ecole;
select inscription.id_eleve, eleve.nom_eleve from eleve join inscription on 
inscription.id_eleve=eleve.id_eleve; 

select count(inscription.id_eleve),inscription.id_eleve, eleve.nom_eleve from eleve join inscription on 
inscription.id_eleve=eleve.id_eleve group by(inscription.id_eleve); 
SELECT @@global.sql_mode;
SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY','')