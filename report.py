from reportlab.lib.pagesizes import letter,A4,landscape
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate, Frame
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import *

# Fonction pour générer un PDF à partir des données d'un TreeView avec un tableau plus grand et un titre
def generate_pdf(tree,file_name,heading,titre,dimension:list):
    doc = SimpleDocTemplate(file_name, pagesize=A4)
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
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    table.setStyle(style)
    
    elements.append(table)

    # Générer le PDF
    doc.build(elements)
    return True