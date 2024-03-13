from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image
from reportlab.lib import colors

# Création du document PDF
doc = SimpleDocTemplate("bulletin_aperçu.pdf", pagesize=letter)
content = []

# Informations sur l'école
school_info = [
    ["École:", "Nom de l'école"],
    ["Adresse:", "Adresse de l'école"],
    # Ajoutez d'autres informations sur l'école si nécessaire
]

# Informations sur l'élève
student_info = [
    ["Nom:", "Prénom Nom de l'élève"],
    ["Classe:", "8ème année"],
    ["Numéro de matricule:", "123456"],
    # Ajoutez d'autres informations sur l'élève si nécessaire
]

# Liste des matières et des notes obtenues par l'élève
subjects = [
    ["Matière", "Note"],
    ["Mathématiques", "15"],
    ["Français", "14"],
    ["Histoire", "13"],
    # Ajoutez d'autres matières et notes ici
]

# Moyenne générale
average_grade = "Moyenne générale: 14.0"

# Appréciation générale de l'enseignant
teacher_comment = "Appréciation générale de l'enseignant: Bon travail, continuez ainsi!"

# Tableaux pour les informations sur l'école, l'élève et les matières
school_table = Table(school_info)
student_table = Table(student_info)
subjects_table = Table(subjects)

# Appliquer des styles aux tableaux
school_table.setStyle(TableStyle([('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
                                  ('VALIGN', (0, 0), (-1, -1), 'TOP')]))
student_table.setStyle(TableStyle([('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
                                   ('VALIGN', (0, 0), (-1, -1), 'TOP')]))
subjects_table.setStyle(TableStyle([('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
                                    ('VALIGN', (0, 0), (-1, -1), 'TOP')]))

# Ajouter les tableaux au contenu du document
content.extend([school_table, student_table, subjects_table])

# Ajouter la moyenne générale et l'appréciation de l'enseignant au contenu du document
content.append(average_grade)
content.append(teacher_comment)
