"""treeview editable and crud operations in mysql table using python tkinter and mysql.connector 
reference: https://youtu.be/K04P7TLLhFo
"""
 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
import mysql.connector
from mysql.connector import Error
import os
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Fiche_cotation:
    def __init__(self,root):
        self.root=root
        self.root.title("Fiche de cotation")
        self.root.geometry("1350x700+0+0")
        self.root.configure(background='#091821')
        self.root.resizable(0,0)
        self.connexion=mysql.connector.connect(host='localhost',user='root',password='',database='gestion_des_notes')
        self.cursor=self.connexion.cursor()
        self.id_cours=StringVar()
        self.id_inscription=StringVar()
        self.p1=StringVar()
        self.p2=StringVar()
        self.ex1=StringVar()
        self.p3=StringVar()
        self.p4=StringVar()
        self.ex2=StringVar()
        self.id_class=StringVar()
        self.id_anne=StringVar()
        self.id_eleve=StringVar()
        self.id_cours=StringVar()
        self.id_inscription=StringVar()
        self.p1=StringVar()
        self.p2=StringVar()
        self.ex1=StringVar()
        self.p3=StringVar()
        self.p4=StringVar()
        self.ex2=StringVar()
        self.id_class=StringVar()
        self.id_anne=StringVar()
        self.id_eleve=StringVar()
        self.id_cours=StringVar()
        self.id_inscription=StringVar()
        self.p1=StringVar()
        self.p2=StringVar()
        self.ex1=StringVar()
        self.p3=StringVar()
        self.p4=StringVar()
        self.ex2=StringVar()
        self.id_class=StringVar()
        self.id_anne=StringVar()
        self.id_eleve=StringVar()
        self.id_cours=StringVar()
        self.id_inscription=StringVar()
        self.p1=StringVar()
        self.p2=StringVar()
        self.ex1=StringVar()
        self.p3=StringVar()
        self.p4=StringVar()
        self.ex2=StringVar()
        self.id_class=StringVar()
        self.id_anne=StringVar()
        self.id_eleve=StringVar()
        self.id_cours=StringVar()
        self.id_inscription=StringVar()
        self.p1=StringVar()
        self.p2=StringVar()
        self.ex1=StringVar
        self.p3=StringVar()
        self.p4=StringVar()
        self.ex2=StringVar()
        self.id_class=StringVar()
        self.id_anne=StringVar()
        self.id_eleve=StringVar()
        
        self.label_titre=Label(self.root, borderwidth=3,relief=SUNKEN,text="Fiche de cotation",font=("Sans Serif",16),fg='white',background='#091821')
        self.label_titre.place(x=300,y=0,width=500,height=80)
        self.label_nom_cours=Label(self.root,text="Nom du cours",font=("Sans Serif",12),fg='white',background='#091821')
        self.label_nom_cours.place(x=300,y=100)
        self.nom_cours=Entry(self.root,font=("Sans Serif",12))
        self.nom_cours.place(x=400,y=100)
        self.label_dom=Label(self.root,text="Domaine",font=("Sans Serif",12),fg='white',background='#091821')
        self.label_dom.place(x=300,y=150)
        
        self.combo_dom=ttk.Combobox(self.root,font=("Sans Serif",12))
        self.combo_dom.place(x=400,y=150)
        self.label_max_period=Label(self.root,text="Max period",font=("Sans Serif",12),fg='white',background='#091821')
        self.label_max_period.place(x=300,y=200)
        self.max_period=Entry(self.root,font=("Sans Serif",12))
        self.max_period.place(x=400,y=200)
        self.label_max_exam=Label(self.root,text="Max exam",font=("Sans Serif",12),fg='white',background='#091821')
        self.label_max_exam.place(x=300,y=250)
        self.max_exam=Entry(self.root,font=("Sans Serif",12))
        self.max_exam.place(x=400,y=250)
        self.label_class=Label(self.root,text="Classe",font=("Sans Serif",12),fg='white',background='#091821')
        self.label_class.place(x=300
                                    ,y=300)
        self.combo_class=ttk.Combobox(self.root,font=("Sans Serif",12))
        self.combo_class.place(x=400
                                    ,y=300)
        self.bouton_ajouter=Button(self.root,text='Ajouter', background='#FF4500',font=("Times",16),fg='white',command=self.ajouter)
        self.bouton_ajouter.place(x=350,y=350,width=100)
        self.bouton_modifier=Button(self.root,text='Modifier', background='#FF4500',font=("Times",16),fg='white',command=self.modifier)
        self.bouton_modifier.place(x=500,y=350,width=100)
        self.bouton_supprimer=Button(self.root,text='Supprimer', background='#FF4500',font=("Times",16),fg='white',command=self.supprimer)
        self.bouton_supprimer.place(x=650,y=350,width=100)
        self.tree=ttk.Treeview(self.root,columns=('Num','nom_cours','id_dom','max_period','max_exam','id_class'),show='headings')
        self.tree.heading('Num',text='Numéro')
        self.tree.heading('nom_cours',text='Nom du cours')
        self.tree.heading('id_dom',text='Domaine')
        self.tree.heading('max_period',text='Max period')
        self.tree.heading('max_exam',text='Max exam')
        self.tree.heading('id_class',text='Classe')
        self.tree.column('Num',width=50)
        self.tree.column('nom_cours',width=100)
        self.tree.column('id_dom',width=100)
        self.tree.column('max_period',width=100)
        self.tree.column('max_exam',width=100)
        self.tree.column('id_class',width=100)
        self.rempkir_combo_dom()
        self.rempkir_combo_class()
        self.run()
    def rempkir_combo_dom(self):
        self.cursor.execute("select * from domaine_cours")
        a=self.cursor.fetchall()
        self.combo_dom['values']=[i[0] for i in a]
    def rempkir_combo_class(self):
        self.cursor.execute("select * from classe")
        a=self.cursor.fetchall()
        self.combo_class['values']=[i[0] for i in a]
    def ajouter(self):
        
        try:
            self.cursor.execute("insert into cours values(%s,%s,%s,%s,%s)", (self.nom_cours.get(), self.combo_dom.get(), self.max_period.get(), self.max_exam.get(), self.combo_class.get()))
            self.connexion.commit()
            self.run()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            
    def modifier(self):
        try:
            self.cursor.execute("update cours set nom_cours=%s, id_dom=%s, max_period=%s, max_exam=%s, id_class=%s where id_cours=%s", (self.nom_cours.get(), self.combo_dom.get(), self.max_period.get(), self.max_exam.get(), self.combo_class.get(), self.id_cours))
            self.connexion.commit()
            self.run()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            
    def supprimer(self):
        try:
            self.cursor.execute("delete from cours where id_cours=%s", (self.id_cours,))
            self.connexion.commit()
            self.run()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            
    def run(self):
        self.cursor.execute("select * from cours")
        data=self.cursor.fetchall()
        self.tree.delete(*self.tree.get_children())
        for i in data:
            self.tree.insert('','end',values=i)
        self.tree.place(x=300,y=400,width=700,height=200)
        self.tree.bind("<ButtonRelease-1>",self.get_data)
    def get_data(self,event):

            