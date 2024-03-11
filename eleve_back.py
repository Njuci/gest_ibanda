"""
create table eleve(
id_eleve int auto_increment  primary key,
num_permenant varchar(30) unique,
nom_eleve varchar(30),
sexe char(1),
date_nais date,
lieu_nais varchar(30)
);

une classe eleve_back qui a
une methode  save, delete,update get et get_all
"""
class 