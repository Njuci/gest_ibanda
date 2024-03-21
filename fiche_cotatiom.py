"""
Fiche de cotation
se basant sur le design de domaine_cours_frontemd.py
et le fiche que le tutilaire ait la possiblié de saisir les notes des etudiants par matiere
en sachant que le saisie est limité par la note maximale de la matiere et qu'il fasse la saisie de la note dand le treeview editable
P1 p2 Ex1 p3 p4 ex2
et aussi le tutilaire peut imprimer la fiche de cotation
"""

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from tkinter import filedialog
from login_back import Connexion
from side_bar_proviseur import Sidebar_prov
from fiche_cote_back import Fiche_cote_back
from inscription_backend import Inscription_back
from cours_backend import cours_back
from classe_backend import Classe
from anne_scolaire_backend import Anne_scolaire
from eleve_backend import Eleve
from domaine_cours_back import Domaine_cours
from tkinter import messagebox
import os
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog
import os
import csv
import pandas as pd
import numpy as np
