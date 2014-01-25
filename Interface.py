# -*- coding: utf-8 -*-
'''
@author: Olivier Froger
'''
from tkinter import Tk, Label, Button, Menu, Canvas, StringVar, Entry, Text, NORMAL, DISABLED, END
from Game import init, getColor, place, getNumberColor
from random import randrange
import time

colorVert, blanc, noir, yOffsetCanvas, xOffsetCanvas, gridOffsetCanvas, tailleCase , Comic, Comic2, Comic3, tourdejeu, colors, color_player = "#086126", 1, 2, 2, 8, 25, 50, ("Comic sans MS", "9"), ("Comic sans MS", "25"), ("Comic sans MS", "35"), 1, ["red", "green", "yellow", "blue"], "orange"

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
    offsetGrid, backgroundColor, borderLineColor = 5, colorVert, "black"
    if color == blanc: backgroundColor = "white"
    elif color == noir: backgroundColor = "black"
    else: borderLineColor = colorVert
    Can.create_oval(gridOffsetCanvas + (x * tailleCase) + offsetGrid, gridOffsetCanvas + (y * tailleCase) + offsetGrid, gridOffsetCanvas + (tailleCase * (x + 1)) - offsetGrid, gridOffsetCanvas + (tailleCase * (y + 1)) - offsetGrid, fill = backgroundColor, outline = borderLineColor)

def mettre_pion(event):
    """
    Recupere un clic souris et joue le pion dans la case appropriee
    
    Arguments:
        event -> L'event du clic
    """
    global tourdejeu
    if(place(1 + (tourdejeu % 2), ((event.x) - gridOffsetCanvas) // tailleCase, ((event.y) - gridOffsetCanvas) // tailleCase) == 0):
        tourdejeu += 1
    refresh()

def regles():
    """
    Permet d'afficher la fenetre des regles
    """
    fen1 = Tk()
    fen1.title("R" + e_grave() + "gles du jeu")
    fen1.geometry("500x500")
    fen1.resizable(0, 0)
    fen1.mainloop()

def preferences():
    """
    Permet d'afficher la fenetre des preferences
    """
    fen2 = Tk()
    fen2.title("Pr" + e_aigu() + "f" + e_aigu() + "rences")
    fen2.geometry("500x500")
    fen2.resizable(0, 0)
    fen2.mainloop()

def a_propos():
    """
    Permet d'afficher la fenetre a propos
    """
    fen3 = Tk()
    fen3.title(a_accent_maj() + " propos de")
    fen3.geometry("500x500")
    fen3.resizable(0, 0)
    fen3.mainloop()

def parler(event = None):
    """
    Permet au joueur d'envoyer un message dans le chat
    """
    textTraitment(en.get(), "player", str(ps.get()), colors[randrange(len(colors))])
    en.delete(0, END) 

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
    pTime = time.strftime('%H:%M:%S : ', time.localtime())
    text = pTime + str(name) + " -> " + str(text)
    textLabel.config(state = NORMAL)
    textLabel.insert(0.0, text + "\n")
    textLabel.tag_configure(color, foreground = color)
    textLabel.tag_add(color, "1." + str(len(pTime + str(name) + " -> ")), "1." + str(len(text)))
    color_user = "black"
    if(user == "player"): color_user = color_player
    elif(user == "system"): color_user = "red"
    else: color_user = "black"
    textLabel.tag_configure("name", foreground = color_user)
    textLabel.tag_add("name", "1." + str(len(pTime)), "1." + str(len(pTime + name)))
    textLabel.config(state = DISABLED)

def connexion():
    """
    Permet d'initialiser la connexion
    """
    Label(Can2, text = str(ps.get()), bg = colorVert, fg = 'red').place(x = 50, y = 2)
    ps.place_forget()
    co.place_forget()
    textLabel.config(state = NORMAL)
    textLabel.config(fg = "red")
    textTraitment("Vous " + e_circonflexe() + "tes connect" + e_grave() + " en tant que " + str(ps.get()), "system", "Syst" + e_grave() + "me", "orange")
    
fen = Tk()
fen.title("Othello")
fen.geometry("800x450")
fen.resizable(0, 0)

menubar = Menu(fen)
     
menufichier = Menu(menubar, tearoff = 0)
menufichier.add_command(label = "Nouvelle partie", command = initialisation)
menufichier.add_command(label = "Pr" + e_aigu() + "f" + e_aigu() + "rences", command = preferences)
menufichier.add_command(label = "Quitter", command = fen.destroy)

menuaide= Menu(menubar,tearoff=0)
menuaide.add_command(label = "R" + e_grave() + "gles du jeu", command = regles)
menuaide.add_command(label = a_accent_maj() + " propos de", command = a_propos)

menubar.add_cascade(label = "Fichier", menu = menufichier)
menubar.add_cascade(label = "Aide", menu = menuaide)

fen.config(menu = menubar)
Can2 = Canvas(fen, bg = colorVert, height = 450, width = 365)
Can2.place(x = 435, y =0)
Can = Canvas(fen, bg = colorVert, height = 450, width = 435)
Can.place(x = 0, y = 0)
Can.bind("<Button-1>", mettre_pion) 
Label(Can, text = "A", font = Comic, bg = colorVert).place(x = 45, y = yOffsetCanvas)
Label(Can, text = "B", font = Comic, bg = colorVert).place(x = 95, y = yOffsetCanvas)
Label(Can, text = "C", font = Comic, bg = colorVert).place(x = 145, y = yOffsetCanvas)
Label(Can, text = "D", font = Comic, bg = colorVert).place(x = 195, y = yOffsetCanvas)
Label(Can, text = "E", font = Comic, bg = colorVert).place(x = 245, y = yOffsetCanvas)
Label(Can, text = "F", font = Comic, bg = colorVert).place(x = 295, y = yOffsetCanvas)
Label(Can, text = "G", font = Comic, bg = colorVert).place(x = 345, y = yOffsetCanvas)
Label(Can, text = "H", font = Comic, bg = colorVert).place(x = 395, y = yOffsetCanvas)
Label(Can, text = "1", font = Comic, bg = colorVert).place(x = xOffsetCanvas, y = 40)
Label(Can, text = "2", font = Comic, bg = colorVert).place(x = xOffsetCanvas, y = 90)
Label(Can, text = "3", font = Comic, bg = colorVert).place(x = xOffsetCanvas, y = 140)
Label(Can, text = "4", font = Comic, bg = colorVert).place(x = xOffsetCanvas, y = 190)
Label(Can, text = "5", font = Comic, bg = colorVert).place(x = xOffsetCanvas, y = 240)
Label(Can, text = "6", font = Comic, bg = colorVert).place(x = xOffsetCanvas, y = 290)
Label(Can, text = "7", font = Comic, bg = colorVert).place(x = xOffsetCanvas, y = 340)
Label(Can, text = "8", font = Comic, bg = colorVert).place(x = xOffsetCanvas, y = 390)
Label(fen, text = "Othello", font = Comic2, bg = colorVert).place(x = 570, y = 35)
Label(Can2, text = "Psuedo:", font = Comic, bg = colorVert).place(x = 5, y = 2)
ps=Entry(Can2)
ps.place(x = 50, y = 2)
co=Button(Can2, text = "Connexion", command = connexion)
co.place(x = 185, y = 2)
count1Var = StringVar()
count2Var = StringVar()
count1 = Label(Can2, textvariable = count1Var, font = Comic3, fg = 'white', bg = colorVert)
count2 = Label(Can2, textvariable = count2Var, font = Comic3, bg = colorVert)
count1.place(x = 115, y = 70)
count2.place(x = 240, y = 70)
x1, x2, y1, y2 = gridOffsetCanvas, gridOffsetCanvas, gridOffsetCanvas, gridOffsetCanvas

for i in range(0, 9):
    Can.create_line(x1, y1, x1 + 400, y1)
    Can.create_line(x2, y2, x2, y2 + 400)
    y1 += tailleCase
    x2 += tailleCase
    
Button(fen, text = "Nouvelle partie", command = initialisation).place(x = 710, y = 1)
en = Entry(Can2, width = 35)
en.bind("<Return>", parler)
en.place(x = 40, y = 400)
textLabel = Text(Can2, state = DISABLED, width = 35, height = 8, font = ("comic sans ms", 10))
textLabel.config(fg = "black")
textLabel.place(x = 40, y = 200)
Button(fen, text = "Envoyer", command = parler).place(x = 710, y = 400)
fen.mainloop()
