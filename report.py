from reportlab.lib.pagesizes import letter,A4,landscape
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate, Frame
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import *
import os

"""_summary_
for key, value in customer_info.items():
        elements.append(Paragraph(f"{key}: {value}", styles['Normal']))

    Returns:
        _type_: _description_
    """

# Fonction pour générer un PDF à partir des données d'un TreeView avec un tableau plus grand et un titre
def generate_pdf_fiche_cote(tree, file_name, heading, titre,information, dimension: list, output_path):
    # Vérifier si le dossier de sortie existe, sinon le créer
    if not os.path.exists(output_path):
        os.makedirs(output_path)


# Obtenir le chemin absolu du dossier courant
    chemin_absolu = os.getcwd()
    d=chemin_absolu.split("\\")
    chemin_absolu=""
    for i in range(len(d)):
        if i==0:
            chemin_absolu=d[i]
        else:
            chemin_absolu=chemin_absolu+"/"+d[i]
    
    print(chemin_absolu)
    doc = SimpleDocTemplate(output_path + '/' + file_name, pagesize=A4)
    doc.pagesize = landscape(A4)
    elements = []
    styles = getSampleStyleSheet()
   
    
    
    # Extraire les données du TreeView
    data = [heading]
    
    for child in tree.get_children():
        values = tree.item(child)['values']
        data.append(values)
    

    # Ajouter un titre au-dessus du tableau
    
    title = Paragraph(titre, styles['Heading1'])
    elements.append(title)
    title = Paragraph("", styles['Heading1'])
    elements.append(title)
    for key, value in information.items():
        elements.append(Paragraph(f"{key}: {value}", styles['Normal']))

    # Ajouter la date
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    date_text = Paragraph("Date: " + today, styles['Normal'])
    elements.append(date_text)
    title = Paragraph("", styles['Heading1'])
    elements.append(title)
    title = Paragraph("", styles['Heading1'])
    elements.append(title)


    # Spécifier une largeur 
    
    
    # Spécifier une hauteur pour chaque ligne
     # Hauteur de la première ligne
    # creer une table
    
    table=Table(data,colWidths=dimension[0],rowHeights=dimension[1])
    
    #table = Table(data,colWidths=colWidth,rowHeights=dimension[1])

    # Styles de la table
    #la premiere colonne soit plus grande que les autres
    
    

    style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightgreen),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('COLWIDTH', (0, 0), (0, -1), 150),  # Augmenter la largeur de la première colonne et les autres colonnes
    
    ])

    # Appliquer le style à la première colonne
    for i in range(len(data[0])):
        if i == 0:
            style.add('BACKGROUND', (i, 1), (i, -1), colors.lightgrey)
        else:
            style.add('BACKGROUND', (i, 1), (i, -1), colors.white)
    

    

    table.setStyle(style)
    
    elements.append(table)

    # Générer le PDF
    doc.build(elements)
    return chemin_absolu+'/'+output_path+file_name



def generate_pdf(tree, file_name, heading, titre, dimension: list, output_path):
    # Vérifier si le dossier de sortie existe, sinon le créer
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    doc = SimpleDocTemplate(output_path + '/' + file_name, pagesize=A4)
    doc.pagesize = landscape(A4)
    
    elements = []

    # Extraire les données du TreeView
    data = [heading]
    
    for child in tree.get_children():
        values = tree.item(child)['values']
        data.append(values)

    # Ajouter un titre au-dessus du tableau
    styles = getSampleStyleSheet()
    title = Paragraph(titre, styles['Heading1'])
    elements.append(title)

    # Ajouter la date
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    date_text = Paragraph("Date: " + today, styles['Normal'])
    elements.append(date_text)
    title = Paragraph("", styles['Heading1'])
    elements.append(title)
    title = Paragraph("", styles['Heading1'])
    elements.append(title)


    # Spécifier une largeur et une hauteur plus grandes pour le tableau
    table = Table(data, colWidths=dimension[0], rowHeights=dimension[1])

    # Styles de la table
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.lightgreen),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    table.setStyle(style)
    
    elements.append(table)

    # Générer le PDF
    doc.build(elements)
    return True

def generate_pdf_data(data_ent, file_name, heading, titre, dimension: list, output_path):
    # Vérifier si le dossier de sortie existe, sinon le créer
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    doc = SimpleDocTemplate(output_path + '/' + file_name, pagesize=A4)
    doc.pagesize = landscape(A4)
    
    elements = []

    # Extraire les données du TreeView
    data = [heading]
    
    for child in data_ent:
        values =child
        data.append(values)

    # Ajouter un titre au-dessus du tableau
    styles = getSampleStyleSheet()
    title = Paragraph(titre, styles['Heading1'])
    elements.append(title)

    # Ajouter la date
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    date_text = Paragraph("Date: " + today, styles['Normal'])
    elements.append(date_text)
    title = Paragraph("", styles['Heading1'])
    elements.append(title)
    title = Paragraph("", styles['Heading1'])
    elements.append(title)


    # Spécifier une largeur et une hauteur plus grandes pour le tableau
    table = Table(data, colWidths=dimension[0], rowHeights=dimension[1])

    # Styles de la table
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    table.setStyle(style)
    
    elements.append(table)

    # Générer le PDF
    doc.build(elements)
    return True
