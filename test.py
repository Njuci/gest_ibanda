from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors

# Créer un nouveau fichier PDF
c = canvas.Canvas("bulletin_scolaire.pdf", pagesize=letter)

# Ajouter du texte au PDF
c.setFont("Helvetica", 12)
c.drawString(100, 750, "BULLETIN SCOLAIRE")

# Ajouter des informations sur l'élève
c.drawString(100, 730, "Nom de l'élève: Jérémie Ndeke Museremu Msexe")
c.drawString(100, 710, "Classe: 7E / A")
c.drawString(100, 690, "Ecole: CS Etoile")
c.drawString(100, 670, "Ville: Bukavu")
c.drawString(100, 650, "Année scolaire: 2022 / 2023")

# Ajouter les résultats des matières
c.drawString(100, 630, "Résultats des matières:")
c.drawString(100, 610, "Mathématiques:")
c.drawString(150, 590, "Premier Semestre:")
c.drawString(150, 570, "Algèbre: 80/160")
c.drawString(150, 550, "Arithmétique: 20/40")
c.drawString(150, 530, "Géométrie: 40/80")
c.drawString(150, 510, "Deuxième Semestre:")
c.drawString(150, 490, "Algèbre: 85/160")
c.drawString(150, 470, "Arithmétique: 20/40")
c.drawString(150, 450, "Géométrie: 30/80")

# Ajouter la moyenne générale
c.drawString(100, 430, "Moyenne générale: 75%")

# Enregistrer le PDF
c.save()