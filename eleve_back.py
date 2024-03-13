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
    def get_all(self,curseur):
        """
        Get all the students' information.
        """
        try:
            # Add code here to get all the students' information
            curseur.execute("select * from eleve")
            return curseur.fetchall()
        except Exception as e:
            # Handle any exceptions that occur during getting all the students' information
           showerror("Erreur",f"Error getting all student information: {str(e)}")
           return False
        
    def save(self,curseur):
        """
        Save the student's information.
        """
        try:
            # Add code here to save the student's information
            query="insert into eleve  values(%s,%s,%s,%s,%s)",(self.num_permenant,self.nom_eleve,self.sexe,self.date_nais,self.lieu_nais)
            print(query)
            curseur.execute(query)
            return True
        except Exception as e:
            # Handle any exceptions that occur during saving
           showerror("Erreur",f"Error saving student information: {str(e)}")
           return False
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