SELECT * FROM gest_ecole.cours;
use gest_ecole;
select cr.id_cours,cr.nom_cours,cr.id_dom,dom.nom_dom,cr.max_period,cr.max_exam,cr.id_class,cl.nom from cours cr join domaine_cours dom on cr.id_dom =dom.id_dom join classe cl on cr.id_class =cl.id_class;