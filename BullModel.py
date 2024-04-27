from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Paragraph,Image
from reportlab.pdfgen import canvas

class PdfBulletin:
    def __init__(self,Dataa):
        left=10
        right=10
        top=5
        bottom=10

        print('DATA BULLETINS',Dataa[0][0],Dataa)

        #Entete du bulletins 
        imgPath="téléchargement.png"
        imgPath1="arm.PNG"
        Data=[[[Image(imgPath, width=80,height=40)],'REPUBLIQUE DEMOCRATIQUE DU CONGO \n MINISTERE DE L\'ENSEIGNEMENT PRIMAIRE, SECONDAIRE ET TECHNIQUE',[Image(imgPath1, width=60,height=40)],]]
        L=[120,350,120,]
        H=[70]
        Entete=Table(Data,colWidths=L, rowHeights=H,style=[('GRID', (0, 0), (-1, -1), 1, colors.white)])
        style= TableStyle([('FONTSIZE', (0, 0), (-1,-1),10),
        ('VALIGN', (0, 0), (-1,-1),'MIDDLE'),
        ('ALIGN', (0, 0), (-1,-1),'CENTER'),

        ])
        Entete.setStyle(style)



        # N° code section
        EcoleInfo=[['N° ID','','','','','','','','','','','','','','','','','','','','','','','','','','','',]]
        L=[38,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]
        H=[12]
        NumId=Table(EcoleInfo,colWidths=L, rowHeights=H,style=[('GRID', (0, 0), (-1, -1), 1, colors.black)])
        style= TableStyle([('FONTSIZE', (0, 0), (-1,-1),9),
        ('VALIGN', (0, 0), (0,0),'MIDDLE'),

        ])
        NumId.setStyle(style)
        #Code Ecole creation des cases 
        EcoleInfo=[[1,'-',6,3,1,4,7,0]]
        L=[20,20,20,20,20,20,20,20]
        H=[11]
        CodeEco=Table(EcoleInfo,colWidths=L, rowHeights=H,style=[('GRID', (0, 0), (-1, -1), 1, colors.black)])
        style= TableStyle([('FONTSIZE', (0, 0), (-1,-1),9),
        ('VALIGN', (0, 0), (-1,-1),'MIDDLE'),

        ])
        CodeEco.setStyle(style)
        #Informations sur ecole 

        EcoleInfo=[['VILLE :','BUKAVU'],['COMMUNE :','IBANDA'],['ECOLE :','INSTITUT IBANDA'],['CODE :',CodeEco]]
        L=[70,195,65,160]
        H=[12,12,12,15]
        EcoInfoTable=Table(EcoleInfo,colWidths=L, rowHeights=H,style=[('GRID', (0, 0), (-1, -1), 1, colors.white)])
        style= TableStyle([('FONTSIZE', (0, 0), (-1,-1),8),
        ('VALIGN', (0, 0), (-1,-1),'MIDDLE'),
        ('PADDING', (0, 0), (-1,-1),2),
        ])
        EcoInfoTable.setStyle(style)



        #NumeroPermanent
        Num=[['', '','', '','', '','','','','','', '','', '','', '']]
        L=[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]
        H=[11]
        NumPerm=Table(Num,colWidths=L, rowHeights=H,style=[('GRID', (0, 0), (-1, -1), 1, colors.black)])
        style= TableStyle([('FONTSIZE', (0, 0), (-1,-1),9),
        ('VALIGN', (0, 0), (-1,-1),'MIDDLE'),

        ])
        NumPerm.setStyle(style)

        #Informations sur élève 
        EleveInfo=[['ELEVE :','',"SEXE :"],['NE(E) A :','','LE......./......./....'],['CLASSE :',' '],['N PERM :',NumPerm]]
        L=[60,150,100,200]
        H=[12,12,12,15]
        EleveInfoTable=Table(EleveInfo,colWidths=L, rowHeights=H,style=[('GRID', (0, 0), (-1, -1), 1, colors.white)])
        style= TableStyle([('FONTSIZE', (0, 0), (-1,-1),8),
        ('VALIGN', (0, 0), (-1,-1),'MIDDLE'),
        ('PADDING', (0, 0), (-1,-1),2),
        ('SPAN', (1, 3), (2,3)),
        ('SPAN', (1, 2), (2,2)),
        ])
        EleveInfoTable.setStyle(style)


        #Ligne amnee scolaire
        Data=[['BULLETIN DE LA 8e ANNEE CYCLE TERMINAL DE L\'EDUCATION DE BASE (CTEB) :','ANNEE SCOLAIRE 2023 - 2024']]
        L=[440,150]
        H=[15]
        AnneeTable=Table(Data,colWidths=L, rowHeights=H,style=[('GRID', (0, 0), (-1, -1), 1, colors.white)])
        style= TableStyle([('FONTSIZE', (0, 0), (-1,-1),9),
        ('VALIGN', (0, 0), (-1,-1),'MIDDLE'),
        ('PADDING', (0, 0), (-1,-1),2),
        ])
        AnneeTable.setStyle(style)

        #Informations de pied de page
        ligne1='L\'élève ne pourra passer dans la classe supérieur s\'il n\'a subi avec succès un examen de repêchage en................................................................\n.................................................................................................................................................................................................................................(1)\n- L\'élève passe dans la classe supérieur (1)\n- L\'élève double la classe (1)'
        Data=[['','',''],['Signature de l\'élève ','Sceau de l\'école','Fait à.........................le......./....../20....\n Le chef d\'Etablissement       Nom et Signature'],['(1) Biffer la mention inutile \nNote importante: Le bulletin est sans valeur s\'il est raturé ou surchargé.','','']]
        Data[0][0]=ligne1
        L=[200,190,195]
        H=[50,20,25]
        PiedTable=Table(Data,colWidths=L, rowHeights=H,style=[('GRID', (0, 0), (-1, -1), 1, colors.white)])
        style= TableStyle([('FONTSIZE', (0, 0), (-1,-1),9),
        ('VALIGN', (0, 0), (-1,-1),'MIDDLE'),
        ('PADDING', (0, 0), (-1,-1),2),
        ('SPAN', (0, 0), (2,0)),
        ('SPAN', (0, 2), (2,2)),
        ])
        PiedTable.setStyle(style)
        #Information générale du bulletin
        data = [
            [Entete,'', '','', '','', '','','','','','', '','', '','', '','','',''],
            [NumId,'', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['PROVINCE : SUD-KIVU','', '','', '','', '','','','','','', '','', '','', '','','',''],
            [EcoInfoTable, '','', '','', '','','',EleveInfoTable,'','', '','', '','', '','','',''],
            [AnneeTable,'', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['BRANCHE','PREMIER SEMESTRE', '','', '','', '','','SECOND SEMESTRE','','','', '','', '','TOTAL\nGENERAL', '','','EXAMEN DE\n REPECHAGE',''],
            ['','MAX', 'TRAV.\n JOUR.','', 'EXAMEN','', 'TOTAL','','MAX','TRAV.\n JOUR.','','EXAMEN', '','TOTAL', '','', '','','',''],
            ['','', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['','', 'P1','P2', '','', '','','','P3','P4','', '','', '','', '','','%','Sign.Prof'],
            ['DOMAINE DES SCIENCES','', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['Sous domaines des mathésmatiques','', '','', '','', '','','','','','', '','', '','', '','','',''],
            [Dataa[0][0],40,Dataa[0][1],Dataa[0][2],80,Dataa[0][3],160,Dataa[0][4],40,Dataa[0][4],Dataa[0][5],80,Dataa[0][6],160,Dataa[0][7],320, Dataa[0][8],'','',''],
            [Dataa[1][0],10,Dataa[1][1],Dataa[1][2],20,Dataa[1][3],40,Dataa[1][4],10,Dataa[1][4],Dataa[1][5],20,Dataa[1][6],40,Dataa[1][7],80, Dataa[1][8],'','',''],
            [Dataa[2][0],20,Dataa[2][1],Dataa[2][2],40,Dataa[2][3],80,Dataa[2][4],20,Dataa[2][4],Dataa[2][5],40,Dataa[2][6],80,Dataa[2][7],160, Dataa[2][8],'','',''],
            [Dataa[3][0],10,Dataa[3][1],Dataa[3][2],20,Dataa[3][3],40,Dataa[3][4],10,Dataa[3][4],Dataa[3][5],20,Dataa[3][6],40,Dataa[3][7],80, Dataa[3][8],'','',''],
            ['Sous-Total',80, Dataa[0][1]+Dataa[1][1]+Dataa[2][1]+Dataa[3][1],'', '','', '','','','','','', '','', '','', '','','',''],
            ['Sous domaine des sciences de la vie et de la terre','', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['','', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['','', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['','', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['','', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['Sous domaines des Sciences Physique, Technologie et TIC','', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['','', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['','', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['','', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['','', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['DOMAINES DES LANGUES','', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['','', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['','', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['','', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['DOMAINE DE L\'UNIVERS SOCIAL ET ENVIRONNEMENT','', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['','', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['','', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['','', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['','', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['','', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['','', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['DOMAINE DES ARTS','', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['','', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['','', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['','', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['DOMAINE DU DEVELOPPEMENT PERSONNEL','', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['','', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['','', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['MAXIMA GEN','', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['TOTAUX','', '','', '','', '','','','','','', '','', '','', '','','-PASSE (1) \n-Double (1)\n\nLE CHEF D\'ET.\nSceau de l\'école',''],
            ['POURCENTAGE','', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['PLACE / Nbr Elè ','', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['APPLICATION','', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['CONDUITE','', '','', '','', '','','','','','', '','', '','', '','','',''],
            ['SIGNAT. RESP.','', '','', '','', '','','','','','', '','', '','', '','','',''],
            [PiedTable,'', '','', '','', '','','','','','', '','', '','', '','','','']   
        ]

        #Definitions des largeurs de colonnes
        taille =[90,30,25,25,25,25,25,25,25,25,25 ,25 ,25 ,25 ,25 ,25 ,25,25,25,60]

        # Définition des styles de cellule pour les fusions
        HeightRow =[60,12,12,55,15,11,12,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,100]
        style = TableStyle([   # Renvoie à la ligne
                            
                            ('ROWHEIGHTS', (0, 0), (0,0),100),
                            
                            # ligne en tete
                            ('SPAN', (0, 0), (19,0)),
                            ('SPAN', (0, 1), (19,1)),

                            ('SPAN', (0, 2), (19,2)),
                            ('VALIGN', (0, 2), (0,2),'MIDDLE'),
                            ('FONTSIZE', (0, 2), (0,2),9),
                        
                            # ligne infos eleves 
                            ('SPAN', (0, 3), (7, 3)),
                            ('ALIGN', (0,3), (0,3),'RIGHT'),
                            ('ALIGN', (1,5), (1,5),'CENTER'),

                            ('SPAN', (8, 3), (19, 3)),

                            # ligne classe et annee scolaire
                            ('SPAN', (0, 4), (19,4)),
                            # ligne Branche
                            ('SPAN', (0, 5), (0,8)),
                            #Premier semestre
                            ('SPAN', (1, 5), (7,5)),
                            #Max
                            ('SPAN', (1, 6), (1,8)),
                            ('ALIGN',  (1,6), (1,6),'CENTER'),
                            #Travaux journ
                            ('SPAN', (2, 6), (3,6)),
                            ('WORDWRAP',(2,6), (2,6),1),
                            ('ALIGN', (2,6), (2,6),'CENTER'),
                            ('SPAN', (2, 6), (3,7)),
                            #Exament
                            ('SPAN', (4, 6), (5,6)),
                            ('ALIGN', (4,6), (4,6),'CENTER'),
                            ('SPAN', (4, 6), (5,8)),
                            #TotalGeneral
                            ('SPAN', (6, 6), (7,6)),
                            ('ALIGN', (6,6), (6,6),'CENTER'),
                            ('SPAN', (6, 6), (7,8)),

                            #Second semestre
                            ('SPAN', (8, 5), (14,5)),
                            ('ALIGN', (8,5), (8,5),'CENTER'),

                            #Max
                            ('SPAN', (8, 6), (8,8)),
                            ('ALIGN', (8,6), (8,6),'CENTER'),
                            #TravauxJournalier
                            ('SPAN', (9, 6), (10,6)),
                            ('SPAN', (9, 6), (10,7)),
                            ('ALIGN', (9,6), (9,6),'CENTER'),

                            #TravauxJournalier
                            ('SPAN', (11, 6), (12,6)),
                            
                            ('SPAN', (11, 6), (12,8)),
                            ('ALIGN', (10,6), (10,6),'CENTER'),
                            #TotalGen
                            ('SPAN', (13, 6), (14,6)),
                            ('SPAN', (13, 6), (14,8)),
                            ('ALIGN', (13,6), (13,6),'CENTER'),
                            #TotGeneral
                            ('SPAN', (15, 5), (16,5)),
                            ('SPAN', (15, 5), (16,8)),
                            ('ALIGN', (15,5), (15,5),'CENTER'),

                            #LigneVide
                            ('SPAN', (17, 5), (17,50)),
                            ('BACKGROUND', (17, 5), (17,5),colors.black),

                            #Exament de repechage
                            ('SPAN', (18, 5), (19,5)),
                            ('ALIGN', (18,5), (18,5),'CENTER'),
                            ('SPAN', (18, 5), (19,7)),
            

                            
                            
                            
                            #('GRID', (0, 0), (-1,-1),0,(0,0,0,0)),
                            #Trav Journalier
                            # ajout de l'alignement pour chaque lignes
                            ('VALIGN', (0, 0), (-1,-1),'MIDDLE'),
                            ('FONTSIZE', (0, 0), (-1,-1),8),

                            #Corps du bulletins

                            #Colonnes 19 et 20
                            ('ALIGN', (18,6), (18,6),'CENTER'),
                            ('SPAN', (18, 9), (19,9)),
                            ('SPAN', (18, 9), (19,10)),
                            ('BACKGROUND', (18, 9), (18,9),colors.black),
                            #Domaines1
                            ('SPAN', (0, 9), (16,9)),
                            ('ALIGN', (0,9), (0,9),'CENTER'),
                            ('FONTWEIGHT', (0,9), (0,9),'BOLD'),
                            ('BACKGROUND', (0, 9), (0,9),'#f0efec'),
                            ('SPAN', (0, 10), (16,10)),
                            ('ALIGN', (0,10), (0,10),'CENTER'),
                            ('BACKGROUND', (0, 10), (0,10),'#f0efec'),

                            #Domaines2
                            ('SPAN', (0, 16), (16,16)),
                            ('SPAN', (18, 16), (19,16)),
                            ('ALIGN', (0,16), (0,16),'CENTER'),
                            ('BACKGROUND', (0, 16), (0,16),'#f0efec'),
                            ('BACKGROUND', (18, 16), (18,16),'#f0efec'),

                            #Domaines3
                            ('SPAN', (0, 21), (16,21)),
                            ('SPAN', (18, 21), (19,21)),
                            ('ALIGN', (0, 21), (0,21),'CENTER'),
                            ('BACKGROUND',(0, 21), (0,21),'#f0efec'),
                            ('BACKGROUND', (18, 21), (18,21),'#f0efec'),

                            #Domaines4
                            ('SPAN', (0, 26), (16,26)),
                            ('SPAN', (18, 26), (19,26)),
                            ('ALIGN', (0, 26), (0,26),'CENTER'),
                            ('BACKGROUND',(0, 26), (0,26),'#f0efec'),
                            ('BACKGROUND', (18, 26), (18,26),'#f0efec'),

                            #Domaines5
                            ('SPAN', (0, 30), (16,30)),
                            ('SPAN', (18, 30), (19,30)),
                            ('ALIGN', (0, 30), (0,30),'CENTER'),
                            ('BACKGROUND',(0, 30), (0,30),'#f0efec'),
                            ('BACKGROUND', (18, 30), (18,30),'#f0efec'),
                            #Domaines6
                            ('SPAN', (0, 37), (16,37)),
                            ('SPAN', (18, 37), (19,37)),
                            ('ALIGN', (0, 37), (0,37),'CENTER'),
                            ('BACKGROUND',(0, 37), (0,37),'#f0efec'),
                            ('BACKGROUND', (18, 37), (18,37),'#f0efec'),

                            #Domaines7
                            ('SPAN', (0, 41), (16,41)),
                            ('SPAN', (18, 41), (19,41)),
                            ('ALIGN', (0, 41), (0,41),'CENTER'),
                            ('BACKGROUND',(0, 41), (0,41),'#f0efec'),
                            ('BACKGROUND', (18, 41), (18,41),'#f0efec'),

                            #PIED DES PAGES NOIR
                            ('SPAN', (1, 44), (1,49)),
                            ('BACKGROUND',(1, 44), (1,49),colors.black),
                            ('SPAN', (1, 50), (2,50)),
                            ('SPAN', (3, 50), (7,50)),
                            ('SPAN', (8, 50), (9,50)),
                            ('SPAN', (10, 50), (16,50)),

                            ('BACKGROUND',(4, 49), (8,49),colors.black),
                            ('BACKGROUND',(4, 48), (8,48),colors.black),
                            ('BACKGROUND',(4, 48), (4,44),colors.black),
                            ('BACKGROUND',(6, 48), (6,44),colors.black),
                            ('BACKGROUND',(8, 48), (8,44),colors.black),

                            ('BACKGROUND',(11, 48), (17,48),colors.black),
                            ('BACKGROUND',(11, 49), (17,49),colors.black),
                            ('BACKGROUND',(11, 48), (11,44),colors.black),
                            ('BACKGROUND',(13, 48), (13,44),colors.black),
                            ('BACKGROUND',(15, 48), (15,44),colors.black),

                            #Decision
                            ('SPAN', (18, 50), (19,50)),
                            ('SPAN', (18, 50), (19,45)),
                            ('SPAN', (18, 44), (19,44)),
                            ('BACKGROUND',(18, 44),(18, 44),'#f0efec'),

                            #pied de page
                            ('SPAN', (0, 51), (19,51)),

                    
                            ],)

        # Création du tableau
        table = Table(data, colWidths=taille, rowHeights=HeightRow, style=[('GRID', (0, 0), (-1, -1), 1, colors.black)])

        # Application du style de fusion
        table.setStyle(style)

        # Création du document PDF
        doc = SimpleDocTemplate("BulletinPDF.pdf", pagesize=letter,
        leftMargin=left,
        rightMargin=right,
        topMargin=top,
        bottomMargin=bottom)
        content = [table,table]
        doc.build(content)

