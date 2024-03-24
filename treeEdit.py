import tkinter as tk
from tkinter import ttk

class TreeviewEditable(ttk.Treeview):
    def __init__(self, master, **kw):
        #initialize fen 
        self.fen = master
        
        self.new_values = []
        
        
        self.new_values_callback = lambda x: None
        super().__init__(master,**kw)
        self.bind("<Double-1>", self.on_double_click)
        #self.on_item_modfied=tk.event()
    def on_double_click(self, event):
        # Vérifier la partie sélectionnée
        region_clicked = self.identify_region(event.x, event.y)
        if region_clicked not in ("tree", "cell"):
            return
        
        # Récupérer l'élément sélectionné
        selected_iid = self.focus()
        selected_values = self.item(selected_iid)
        
        # Identifier la colonne et la cellule sélectionnées
        column = self.identify_column(event.x)
        column_index = int(column[1:]) - 1
        if column == '#0':
            selected_text = selected_iid['text']
        else:
            selected_text = selected_values['values'][column_index]
        
        # Récupérer la position de la cellule pour placer l'entrée
        column_box = self.bbox(selected_iid, column)
        
        # Créer et placer l'entrée
        entry_editing = ttk.Entry(self.fen, font=('Arial', 10), width=column_box[2])
        entry_editing.editing_column_index = column_index
        entry_editing.editing_item_iid = selected_iid
        entry_editing.insert(0, selected_text)
        entry_editing.select_range(0, tk.END)
        entry_editing.focus()
        entry_editing.bind('<FocusOut>', self.on_entry_focus_out)
        entry_editing.bind('<Return>', self.on_enter_return)
        entry_editing.place(x=column_box[0], y=column_box[1], width=column_box[2], height=column_box[3])

    def on_entry_focus_out(self, event):
        event.widget.destroy()

    def on_enter_return(self, event):
        new_value = event.widget.get()
        selected_iid = event.widget.editing_item_iid
        column_index = event.widget.editing_column_index
        
        # Mettre à jour les valeurs de l'élément
        if column_index == -1:
            self.item(selected_iid, text=new_value)
        else:
            values = self.item(selected_iid)['values']
            values[column_index] = new_value
            self.item(selected_iid, values=values)
            self.new_values = values
            #print(self.new_values)
            # Appeler la fonction de rappel pour notifier que les valeurs ont changé
            self.new_values_callback(self.new_values)
            #print(self.new_values)
       
            self.get_newvalues(self.new_values)
            #self.on_item_modfied(self.new_values)
            
        
        event.widget.destroy()
    @property
    def get_new_values(self):
        return self.new_values
    #@get_new_values.setter
    def get_newvalues(self,values):
        self.new_values=values
    #se basant sur ce code, on peut créer une classe qui permet de modifier les valeurs d'une ligne de la table fiche_cote
#en double cliquant dessus  
#on peut aussi ajouter un bouton pour ajouter une ligne à la table
#on peut aussi ajouter un bouton pour supprimer une ligne de la table
#on peut aussi ajouter un bouton pour enregistrer les modifications
#on peut aussi ajouter un bouton pour annuler les modifications
#on peut aussi ajouter un bouton pour quitter la fenêtre
#on peut aussi ajouter un bouton pour imprimer la table
#on peut aussi ajouter un bouton pour exporter la table en format excel
class fiche_cote_front:
    def __init__(self):
        self.new_values=None
        # Créer la fenêtre principale
        self.fen = tk.Tk()
        self.fen.title("Fiche de cote")
        self.fen.geometry("800x600")
        self.fen.resizable(False, False)
        #comboox pour choisir le cours à coté au coin gquache en haut en utilisant place
        self.label = tk.Label(self.fen, text="Choisir le cours à coter")
        self.label.place(x=500, y=0)
        self.cours = ttk.Combobox(self.fen, values=["MATH", "PHYS", "INFO"])
        self.cours.place(x=500, y=30)
        #bouton pour ajouter une ligne
        self.add = tk.Button(self.fen, text="Ajouter une ligne")
        self.add.place(x=500, y=60)
        #bouton pour supprimer une ligne
        self.delete = tk.Button(self.fen, text="Supprimer une ligne")
        self.delete.place(x=500, y=90)
        #bouton pour enregistrer les modifications
        self.save = tk.Button(self.fen, text="Enregistrer les modifications")
        self.save.place(x=500, y=120)
        
        
    
        
        # Créer le tableau
        self.tree = TreeviewEditable(self.fen)
        self.tree['columns'] = ('IDInscription  Nom', 'P1', 'P2','EX1','P3','P4','EX2')
        self.tree.heading('#0', text='nuemros')
        self.tree.heading('IDInscription  Nom', text='IDInscription  Nom')
        self.tree.heading('P1', text='P1')
        self.tree.heading('P2', text='P2')
        self.tree.heading('EX1', text='EX1')
        self.tree.heading('P3', text='P3')
        self.tree.heading('P4', text='P4')
        self.tree.heading('EX2', text='EX2')
        self.tree.column('#0', width=40)
        self.tree.column('IDInscription  Nom', width=150)
        self.tree.column('P1', width=40)
        self.tree.column('P2', width=40)
        self.tree.column('EX1', width=40)
        self.tree.column('P3', width=40)
        self.tree.column('P4', width=40)
        self.tree.column('EX2', width=40)
        self.tree.place(x=0, y=150)
        # Ajouter des valeurs
        self.tree.insert('', 'end', text='1', values=['1', '2', '3','4','5','6','7'])
        self.tree.insert('', 'end', text='2', values=['1', '2', '3','4','5','6','7'])
        self.tree.insert('', 'end', text='3', values=['1', '2', '3','4','5','6','7'])
        self.tree.insert('', 'end', text='4', values=['1', '2', '3','4','5','6','7'])
        self.tree.insert('', 'end', text='5', values=['1', '2', '3','4','5','6','7'])
        self.tree.insert('', 'end', text='6', values=['1', '2', '3','4','5','6','7'])
        self.tree.insert('', 'end', text='7', values=['1', '2', '3','4','5','6','7'])
        self.tree.insert('', 'end', text='8', values=['1', '2', '3','4','5','6','7'])
        self.tree.insert('', 'end', text='9', values=['1', '2', '3','4','5','6','7'])
        # Associer la fonction de rappel pour les nouvelles valeurs
        # #variable pour les nouvelles valeurs
        #self.tree.on_item_modfied.bind(self.on_enter_return)
      
        
        self.tree.new_values_callback=self.avoir_nouvelles_valeurs
        
        #print(self.get_values())
        #print(self.get_values)
        #print(self.tree.get_new_values)
        
        
        self.fen.mainloop()
    #rem
    
    
    def on_enter_return(self,s):
        print(s)
    #fonction pour afficher les nouvelles valeurs
    def avoir_nouvelles_valeurs(self,values):        
        self.new_values=values
        print(self.new_values)
    
   
        
    
    def get_values(self):
        
        selected_iid =self.tree.focus()
        self.new_values = self.tree.item(selected_iid)['values']
        #print( self.new_values)
       
    #fonction pour afficher les nouvelles valeurs
    def get_new_values(self):
        
        return self.tree.get_new_values()
        
    def on_new_values(self, new_values):
        print(new_values[1])
    #fonction pour ajouter une ligne
    def add_line(self):
        pass
    #fonction pour supprimer une ligne
    def delete_line(self):
        pass
    #fonction pour enregistrer les modifications
    def save_modifications(self):
        pass
    #fonction pour annuler les modifications
    def cancel_modifications(self):
        pass
    #fonction pour quitter la fenêtre
    def quit(self):
        pass
    #fonction pour imprimer la table
    def print_table(self):
        pass
    #fonction pour exporter la table en format excel
    def export_table(self):
        pass
    def get_valeue(self):
        clm=self.tree.focus()
        values=self.tree.item(clm)['values']
        print(values)
        
#fiche_cote_front()

#on peut aussi ajouter un bouton pour ajouter une ligne à la table
#on peut aussi ajouter un bouton pour supprimer une ligne de la table
    
        
        
        
     
    