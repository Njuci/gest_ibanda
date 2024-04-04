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
from tkinter.messagebox import showerror,showinfo
class eleve_back:
    """
    A class representing a student.
    
    Attributes:
        num_permenant (int): The student's permanent number.
        nom_eleve (str): The student's name.
        sexe (str): The student's gender.
        date_nais (str): The student's date of birth.
        lieu_nais (str): The student's place of birth.
    """
    
    def __init__(self, num_permenant:str, nom_eleve: str, sexe: str, date_nais: str, lieu_nais: str):
        """
        Initializes the eleve_back object with the provided values for the student's information.
        
        Args:
            num_permenant (str): The student's permanent number.
            nom_eleve (str): The student's name.
            sexe (str): The student's gender.
            date_nais (str): The student's date of birth.
            lieu_nais (str): The student's place of birth.
        """
        self.num_permenant = num_permenant
        self.nom_eleve = nom_eleve
        self.sexe = sexe
        self.date_nais = date_nais
        self.lieu_nais = lieu_nais
    def get_eleve(self,curseur,id):
        try:
            curseur.execute("select * from eleve where id_eleve=%s", (id,))
            return curseur.fetchone()
        except Exception as e:
            showerror('error',str(e))
            
    def get_eleve_inscrit(self,curseur,id_anne_scol,id_class):
        try:
            curseur.execute("select e.id_eleve,e.nom_eleve,e.sexe,e.lieu_nais,e.date_nais,i.id_inscription from inscription i join eleve e on  i.id_eleve=e.id_eleve where i.id_anne_scol=%s and id_class=%s ",(id_anne_scol,id_class))
            return curseur.fetchall()
        except Exception as e:
            print(str(e))
            return False
            
    
    def get_eleves(self,curseur,id_anne,id_classe):
        """
        voir les eleves d'une classe pour annee scolaire
        """
        try:
            curseur.execute("select count(*) from inscription where id_class=%s and id_anne_scol=%s",(id_classe,id_anne))
            return curseur.fetchone()
        except Exception as e:
            showerror("Erreur",f"Error getting all student information: {str(e)}")
            return False
    def get_eleves_fille(self,curseur,id_anne,id_classe):
        """
        voir les eleves filles d'une classe pour annee scolaire
        """
        try:
            curseur.execute("select count(*) from inscription i join eleve e where i.id_class=%s and i.id_anne_scol=%s and e.sexe='F'",(id_classe,id_anne))
            return curseur.fetchone()
        except Exception as e:
            showerror("Erreur",f"Error getting all student information: {str(e)}")
            return False
    
    def get_last_id(self,curseur):
        try:
            curseur.execute("select max(id) from eleve")
            f=[curseur.fetchone(),True]
            
            return f
        except Exception as e:
            showerror("Erreur",str(e))
            return False,False
    def get_eleves_garcon(self,curseur,id_anne,id_classe):
        """
        voir les eleves garcons d'une classe pour annee scolaire
        """
        try:
            curseur.execute("select count(*) from inscription i join eleve e where i.id_class=%s and i.id_anne_scol=%s and e.sexe='M'",(id_classe,id_anne))
            return curseur.fetchone()
        except Exception as e:
            showerror("Erreur",f"Error getting all student information: {str(e)}")
            return False
        
        
        
    def get_all(self,curseur):
        """
        Get all the students' information.
        """
        try:
            # Add code here to get all the students' information
            curseur.execute("select id_eleve,num_permanant,nom_eleve,sexe,date_nais,lieu_nais, Date_format(date_enregistrement,'%Y-%m-%d') from eleve order by(date_enregistrement)")
            return curseur.fetchall()
        except Exception as e:
            # Handle any exceptions that occur during getting all the students' information
           showerror("Erreur",f"Error getting all student information: {str(e)}")
           return False
    
    def save(self,curseur,id):
        """
        Save the student's information.
        """
        try:
            # Add code here to save the student's information
            query="insert into eleve(id_eleve,num_permanant,nom_eleve,sexe,date_nais,lieu_nais)  values(%s,%s,%s,%s,%s,%s)",(id,self.num_permenant,self.nom_eleve,self.sexe,self.date_nais,self.lieu_nais)
            curseur.execute("insert into eleve(id_eleve,num_permanant,nom_eleve,sexe,date_nais,lieu_nais)  values(%s,%s,%s,%s,%s,%s)",(id,self.num_permenant,self.nom_eleve,self.sexe,self.date_nais,self.lieu_nais,))
            return True
        except Exception as e:
            # Handle any exceptions that occur during saving
           showerror("Erreur",f"Error saving student information: {str(e)}")
           return False
        #ajoouter un eleve

    def ajouter_eleve(self,curseur):
        

        pass
        
            



    def update(self,curseur,id_eleve):
        """
        Update the student's information.
        """
        try:
            # Add code here to update the student's information
            curseur.execute("update eleve set nom_eleve=%s,sexe=%s,date_nais=%s,lieu_nais=%s ,num_permanant=%s where id_eleve=%s ",(self.nom_eleve,self.sexe,self.date_nais,self.lieu_nais,self.num_permenant,id_eleve))
            return True
        except Exception as e:
            # Handle any exceptions that occur during updating
           showerror("Erreur",f"Error updating student information: {str(e)}")
           return False
    def delete(self,curseur,id_eleve):
        """
        Delete the student's information.
        """
        try:
            # Add code here to delete the student's information
            curseur.execute("delete from eleve where id_eleve=%s",(id_eleve,))
            return True
        except Exception as e:
            # Handle any exceptions that occur during deleting
           showerror("Erreur",f"Error deleting student information: {str(e)}")
           return False