# -*- coding: utf-8 -*-
'''
@author: Olivier Froger
'''
#Pour changer la couleur des pions, mettre des radio button dans "preferences", qui changeront la couleur dans une variable 
#et mettre la variable dans mettre_pion
#http://www.tutorialspoint.com/python/tk_radiobutton.htm
#w = Radiobutton ( master, option, ...  )
#text, textvariable, value, select()
#[Obsidian]
#definition-foreground = #678CB1
#error-foreground = #FF0000
#string-background = #293134
#keyword-foreground = #93C763
#normal-foreground = #E0E2E4
#comment-background = #293134
#hit-foreground = #E0E2E4
#builtin-background = #293134
#stdout-foreground = #678CB1
#cursor-foreground = #E0E2E4
#break-background = #293134
#comment-foreground = #66747B
#hilite-background = #2F393C
#hilite-foreground = #E0E2E4
#definition-background = #293134
#stderr-background = #293134
#hit-background = #000000
#console-foreground = #E0E2E4
#normal-background = #293134
#builtin-foreground = #E0E2E4
#stdout-background = #293134
#console-background = #293134
#stderr-foreground = #FB0000
#keyword-background = #293134
#string-foreground = #EC7600
#break-foreground = #E0E2E4
#error-background = #293134
from tkinter import Tk, Label, Button, Menu, Canvas, StringVar, Entry, Text, NORMAL, DISABLED, END, PhotoImage
from Game import init, getColor, place, getNumberColor
import time

colorVert, blanc, noir, yOffsetCanvas, xOffsetCanvas, gridOffsetCanvas, tailleCase , Comic, Comic2, Comic3, tourDeJeu, colors, color_player = "#086126", 1, 2, 2, 8, 25, 50, ("Comic sans MS", "9"), ("Comic sans MS", "25"), ("Comic sans MS", "35"), 1, "black", "blue"

def a_accent_maj():
    """
    Permet d'afficher un a accent majuscule
    """
    return chr(0x00c0)

def a_accent():
    """
    Permet d'afficher un a accent
    """
    return chr(0x00e0)

def e_aigu():
    """
    Permet d'afficher un e accent aigu
    """
    return chr(0x00e9)
    
    
def e_grave():
    """
    Permet d'afficher un e accent grave
    """
    return chr(0x00e8)

def e_circonflexe():
    """
    Permet d'afficher un e accent circonflexe
    """
    return chr(0x00ea)

def initialisation():
    """
    Permet d'initialiser par default
    """
    init()
    canvasGrille.delete("pion")
    refresh()

def refresh():
    """
    Permet les informations de jeu
    """
    for x in range(0, 8):
        for y in range(0, 8):
            placer_pion(getColor(x, y), x, y)
    count1Var.set(getNumberColor(blanc))
    count2Var.set(getNumberColor(noir))

def placer_pion(color, x, y):
    """
    Permet de placer un pion
    
    Arguments:
        color -> Le numero de la couleur jouee
        x -> La position x (Horizontale)
        y -> La position y (verticale)
    """
    #photo1 = PhotoImage(file ="pionvert.gif")
    #pionVert = canvasGrille.create_image(226, 226, image =photo1)
    #photo2 = PhotoImage(file ="piongris.gif")
    #pionGris = canvasGrille.create_image(226, 226, image =photo2)
    offsetGrid, borderLineColor, backgroundColor = 5, "black", colorVert
    if color == blanc: backgroundColor = "white"
    elif color == noir: backgroundColor = "black"
    else: return
    canvasGrille.create_oval(gridOffsetCanvas + (x * tailleCase) + offsetGrid, gridOffsetCanvas + (y * tailleCase) + offsetGrid, gridOffsetCanvas + (tailleCase * (x + 1)) - offsetGrid, gridOffsetCanvas + (tailleCase * (y + 1)) - offsetGrid, tags = "pion", fill = backgroundColor, outline = borderLineColor)

def mettre_pion(event):
    """
    Recupere un clic souris et joue le pion dans la case appropriee
    
    Arguments:
        event -> L'event du clic
    """
    global tourDeJeu
    if(place(1 + (tourDeJeu % 2), ((event.x) - gridOffsetCanvas) // tailleCase, ((event.y) - gridOffsetCanvas) // tailleCase) == 0):
        tourDeJeu += 1
    refresh()

def regles():
    """
    Permet d'afficher la fenetre des regles
    """
    fenetreRegles = Tk()
    fenetreRegles.title("R" + e_grave() + "gles du jeu")
    fenetreRegles.geometry("500x500")
    fenetreRegles.resizable(0, 0)
    fenetreRegles.mainloop()

def preferences():
    """
    Permet d'afficher la fenetre des preferences
    """
    fenetrePreferences = Tk()
    fenetrePreferences.title("Pr" + e_aigu() + "f" + e_aigu() + "rences")
    fenetrePreferences.geometry("500x500")
    fenetrePreferences.resizable(0, 0)
    fenetrePreferences.mainloop()

def a_propos():
    """
    Permet d'afficher la fenetre a propos
    """
    fenetreAPropos = Tk()
    fenetreAPropos.title(a_accent_maj() + " propos de")
    fenetreAPropos.geometry("500x500")
    fenetreAPropos.resizable(0, 0)
    fenetreAPropos.mainloop()

def parler(event = None):
    """
    Permet au joueur d'envoyer un message dans le chat
    """
    textTraitment(chatEntry.get(), "player", str(pseudoEntry.get()), colors)
    chatEntry.delete(0, END) 

def textTraitment(text, user, name, color):
    """
    Permet d'afficher du texte dans la zone appropriee
    
    Arguments:
        text -> Le texte a afficher
        user -> La parsonne qui parle (Joueur: "player", Systeme: "system", Adversaire: "opponent", Spectateur: "spec")
        name -> Le nom a afficher
        color -> La couleur du texte
    """
    if(str(text) == "" or len(text) == text.count(" ")): return
    textTime = time.strftime('%H:%M:%S : ', time.localtime())
    text = textTime + str(name) + " -> " + str(text)
    textLabel.config(state = NORMAL)
    textLabel.insert(0.0, text + "\n")
    textLabel.tag_configure(color, foreground = color)
    textLabel.tag_add(color, "1." + str(len(textTime + str(name) + " -> ")), "1." + str(len(text)))
    color_user = "black"
    if(user == "player"): color_user = color_player
    elif(user == "system"): color_user = "red"
    else: color_user = "black"
    textLabel.tag_configure("name", foreground = color_user)
    textLabel.tag_add("name", "1." + str(len(textTime)), "1." + str(len(textTime + name)))
    textLabel.config(state = DISABLED)

def connexion():
    """
    Permet d'initialiser la connexion
    """
    Label(canvasInfos, text = str(pseudoEntry.get()), bg = colorVert, fg = 'red').place(x = 50, y = 2)
    pseudoEntry.place_forget()
    connexionButton.place_forget()
    textLabel.config(state = NORMAL)
    textLabel.config(fg = "red")
    textTraitment("Vous " + e_circonflexe() + "tes connect" + e_aigu() + " en tant que " + str(pseudoEntry.get()), "system", "Syst" + e_grave() + "me", "red")
    
fenetre = Tk()
fenetre.title("Othello")
fenetre.geometry("800x450")
fenetre.resizable(0, 0)

menubar = Menu(fenetre)
     
menufichier = Menu(menubar, tearoff = 0)
menufichier.add_command(label = "Nouvelle partie", command = initialisation)
menufichier.add_command(label = "Pr" + e_aigu() + "f" + e_aigu() + "rences", command = preferences)
menufichier.add_command(label = "Quitter", command = fenetre.destroy)

menuaide = Menu(menubar, tearoff = 0)
menuaide.add_command(label = "R" + e_grave() + "gles du jeu", command = regles)
menuaide.add_command(label = a_accent_maj() + " propos de", command = a_propos)

menubar.add_cascade(label = "Fichier", menu = menufichier)
menubar.add_cascade(label = "Aide", menu = menuaide)

fenetre.config(menu = menubar)
canvasInfos = Canvas(fenetre, bg = colorVert, height = 450, width = 365)
canvasInfos.place(x = 435, y = 0)
canvasGrille = Canvas(fenetre, bg = colorVert, height = 450, width = 435)
canvasGrille.place(x = 0, y = 0)
canvasGrille.bind("<Button-1>", mettre_pion)
photo = PhotoImage(file ="fond.gif")
item = canvasGrille.create_image(226, 226, image =photo)
Label(canvasGrille, text = "A", font = Comic, bg = colorVert).place(x = 45, y = yOffsetCanvas)
Label(canvasGrille, text = "B", font = Comic, bg = colorVert).place(x = 95, y = yOffsetCanvas)
Label(canvasGrille, text = "C", font = Comic, bg = colorVert).place(x = 145, y = yOffsetCanvas)
Label(canvasGrille, text = "D", font = Comic, bg = colorVert).place(x = 195, y = yOffsetCanvas)
Label(canvasGrille, text = "E", font = Comic, bg = colorVert).place(x = 245, y = yOffsetCanvas)
Label(canvasGrille, text = "F", font = Comic, bg = colorVert).place(x = 295, y = yOffsetCanvas)
Label(canvasGrille, text = "G", font = Comic, bg = colorVert).place(x = 345, y = yOffsetCanvas)
Label(canvasGrille, text = "H", font = Comic, bg = colorVert).place(x = 395, y = yOffsetCanvas)
Label(canvasGrille, text = "1", font = Comic, bg = colorVert).place(x = xOffsetCanvas, y = 40)
Label(canvasGrille, text = "2", font = Comic, bg = colorVert).place(x = xOffsetCanvas, y = 90)
Label(canvasGrille, text = "3", font = Comic, bg = colorVert).place(x = xOffsetCanvas, y = 140)
Label(canvasGrille, text = "4", font = Comic, bg = colorVert).place(x = xOffsetCanvas, y = 190)
Label(canvasGrille, text = "5", font = Comic, bg = colorVert).place(x = xOffsetCanvas, y = 240)
Label(canvasGrille, text = "6", font = Comic, bg = colorVert).place(x = xOffsetCanvas, y = 290)
Label(canvasGrille, text = "7", font = Comic, bg = colorVert).place(x = xOffsetCanvas, y = 340)
Label(canvasGrille, text = "8", font = Comic, bg = colorVert).place(x = xOffsetCanvas, y = 390)
Label(fenetre, text = "Othello", font = Comic2, bg = colorVert).place(x = 570, y = 35)
Label(canvasInfos, text = "Psuedo:", font = Comic, bg = colorVert).place(x = 5, y = 2)
pseudoEntry=Entry(canvasInfos)
pseudoEntry.place(x = 50, y = 2)
connexionButton=Button(canvasInfos, text = "Connexion", command = connexion)
connexionButton.place(x = 185, y = 2)
count1Var = StringVar()
count2Var = StringVar()
count1Label = Label(canvasInfos, textvariable = count1Var, font = Comic3, fg = 'white', bg = colorVert)
count2Label = Label(canvasInfos, textvariable = count2Var, font = Comic3, bg = colorVert)
count1Label.place(x = 115, y = 70)
count2Label.place(x = 240, y = 70)
x1, x2, y1, y2 = gridOffsetCanvas, gridOffsetCanvas, gridOffsetCanvas, gridOffsetCanvas

for i in range(0, 9):
    canvasGrille.create_line(x1, y1, x1 + 400, y1)
    canvasGrille.create_line(x2, y2, x2, y2 + 400)
    y1 += tailleCase
    x2 += tailleCase
    
Button(fenetre, text = "Nouvelle partie", command = initialisation).place(x = 710, y = 1)
chatEntry = Entry(canvasInfos, width = 35)
chatEntry.bind("<Return>", parler)
chatEntry.place(x = 40, y = 400)
textLabel = Text(canvasInfos, state = DISABLED, width = 41, height = 8, font = ("comic sans ms", 10))
textLabel.config(fg = "black")
textLabel.place(x = 20, y = 185)
Button(fenetre, text = "Envoyer", command = parler).place(x = 710, y = 400)
fenetre.mainloop()
