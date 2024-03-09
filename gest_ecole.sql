drop database if exists gest_ecole;
create database gest_ecole;
use gest_ecole;
drop table if exists fiche_cote;
drop table if exists cours;
drop table if exists domaine_cours;
drop table if exists inscription;
drop table if exists assigner_class;
drop table if exists classe;
drop table if exists utilisateur;
drop table if exists anne_scolaire;

 create table anne_scolaire(
 id int auto_increment  primary  key,
 nom varchar (9) unique,
 encours boolean);
 
create table utilisateur(
id_user int auto_increment primary key,
username varchar(20) unique,
pass_word varchar(20),
user_type varchar(6)
);
create table classe(
id_class int auto_increment primary key,
nom varchar(30) unique
);

 create table assigner_class(
 id_tutilaire int,
 id_class int,
 id_anne_scolaire int,
 constraint pk_assign primary key(id_tutilaire,id_class,id_anne_scolaire),
 constraint pf_assign_titulaire foreign key (id_tutilaire) references utilisateur(id_user),
 constraint pf_id_class_assign foreign key (id_class) references classe(id_class),
 constraint pf_id_anne_assign foreign key (id_anne_scolaire) references anne_scolaire(id) 
 
 );
create table eleve(
id_eleve int auto_increment  primary key,
num_permenant varchar(30) unique,
nom_eleve varchar(30),
sexe char(1),
date_nais date,
lieu_nais varchar(30)
);
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
create table domaine_cours(
id_dom int auto_increment primary key,
nom_dom varchar(30) unique
 );
 
 
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
 create table fiche_cote(
 id_cours int,
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
 