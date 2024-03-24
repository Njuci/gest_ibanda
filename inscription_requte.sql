SELECT * FROM gest_ecole.inscription;
use gest_ecole;
select * from fiche_cote where id_cours=1 and id_inscription in (select id_inscription from inscription where id_class=1 and id_anne_scol=1);
select e.nom_eleve from fiche_cote f join cours c on  f.id_cours=c.id_cours
				join inscription i on f.id_inscription=i.id_inscription 
                join anne_scolaire a on a.id =i.id_anne_scol join
                classe cl on i.id_class=cl.id_class join eleve e on i.id_eleve =e.id_eleve
                where  f.id_cours=1 and cl.id_class=1 and a.id=1;