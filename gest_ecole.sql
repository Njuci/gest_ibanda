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
 id_an int auto_increment unique,
 id varchar(10) primary  key,
 nom varchar (9) unique,
 encours boolean);
 
create table utilisateur(
id int auto_increment unique,
id_user varchar(10)
primary key,
username varchar(20) unique,
pass_word varchar(20),
user_type varchar(11)

);
create table classe(
id int auto_increment
unique,
id_class varchar(10)
 primary key,
nom varchar(30) unique
);

 create table assigner_class(
 id int auto_increment unique,
 id_tutilaire varchar(10),
 id_class varchar(10),
 id_anne_scolaire varchar(10),
 constraint pk_assign primary key(id_tutilaire,id_anne_scolaire),
 constraint pf_assign_titulaire foreign key (id_tutilaire) references utilisateur(id_user)  on delete cascade on update cascade,
 constraint pf_id_class_assign foreign key (id_class) references classe(id_class)  on delete cascade on update cascade,
 constraint pf_id_anne_assign foreign key (id_anne_scolaire) references anne_scolaire(id) on delete cascade on update cascade
 
 );
create table eleve(
id int auto_increment unique,
id_eleve varchar(10) key,
num_permanant varchar(30) unique,
nom_eleve varchar(30),
sexe char(1),
date_nais date,
lieu_nais varchar(30)
);
alter table eleve add column date_enregistrement datetime default current_timestamp;
create table inscription(
id int auto_increment unique,
id_inscription varchar(70) primary key,
id_eleve varchar(10),
id_anne_scol varchar(10),
id_class varchar(10),
 date_inscrip datetime default current_timestamp,
constraint p_k_inscription unique key(id_eleve,id_anne_scol),
constraint p_f_idel_ins foreign key (id_eleve) references eleve(id_eleve) on delete cascade on update cascade,
constraint p_f_idansc_insc foreign key (id_anne_scol) references anne_scolaire(id) on delete cascade on update cascade,
constraint p_f_id_classe foreign key(id_class) references classe(id_class) on delete cascade on update cascade
);
create table domaine_cours(
id int auto_increment unique,
id_dom varchar(10) primary key,
nom_dom varchar(30) unique
 );
 
 
 create table cours(
 id int unique auto_increment,
 id_cours varchar(10) primary key,
 nom_cours varchar(30),
 id_dom varchar(10),
 max_period int,
 max_exam int,
 id_class varchar(10),
constraint p_f_cls_cours foreign key (id_class) references classe(id_class) on delete cascade on update cascade,
constraint pf_cours_dommaine_cours foreign key (id_dom) references domaine_cours(id_dom) on delete cascade on update cascade
 );create table fiche_cote(
  id_cours varchar(10),
  id_inscription varchar(70),
  p1 int default null,
  p2 int default null,
  ex1 int default null,
  p3 int default null,
  p4 int default null,
  ex2 int default null,
  constraint pk_cote primary key(id_cours, id_inscription), 
  constraint pf_id_cours foreign key (id_cours) references cours(id_cours) on delete cascade on update cascade,
  constraint pf_id_inscription foreign key (id_inscription) references inscription(id_inscription) on delete cascade on update cascade

);
 