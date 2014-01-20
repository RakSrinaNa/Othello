'''
@author: Olivier Froger
'''
from tkinter import Tk, Label, Button, Menu, Canvas, StringVar, Entry, Text, NORMAL, DISABLED, END
from Game import init, getColor, place, getNumberColor
import time


colorVert, blanc, noir, yOffsetCanvas, xOffsetCanvas, gridOffsetCanvas, tailleCase , Comic, Comic2, Comic3, tourdejeu = "#086126", 1, 2, 2, 8, 25, 50, ("Comic sans MS", "9"), ("Comic sans MS", "25"), ("Comic sans MS", "35"), 1

def initialisation():
    init()
    refresh()

def refresh():
    for x in range(0, 8):
        for y in range(0, 8):
            placer_pion(getColor(x, y), x, y)
    count1Var.set(getNumberColor(blanc))
    count2Var.set(getNumberColor(noir))

def placer_pion(color, x, y):
    offsetGrid, backgroundColor, borderLineColor = 5, colorVert, "black"
    if color == blanc: backgroundColor = "white"
    elif color == noir: backgroundColor = "black"
    else: borderLineColor = colorVert
    Can.create_oval(gridOffsetCanvas + (x * tailleCase) + offsetGrid, gridOffsetCanvas + (y * tailleCase) + offsetGrid, gridOffsetCanvas + (tailleCase * (x + 1)) - offsetGrid, gridOffsetCanvas + (tailleCase * (y + 1)) - offsetGrid, fill = backgroundColor, outline = borderLineColor)

def mettre_pion(event):
    global tourdejeu
    if(place(1 + (tourdejeu % 2), ((event.x) - gridOffsetCanvas) // tailleCase, ((event.y) - gridOffsetCanvas) // tailleCase) == 0):
        tourdejeu += 1
    refresh()

def regles():
    fen1 = Tk()
    fen1.title("Regles du jeu")
    fen1.geometry("500x500")
    fen1.resizable(0, 0)
    fen1.mainloop()

def preferences():
    fen2 = Tk()
    fen2.title("Preferences")
    fen2.geometry("500x500")
    fen2.resizable(0, 0)
    fen2.mainloop()

def a_propos():
    fen3 = Tk()
    fen3.title("A propos de")
    fen3.geometry("500x500")
    fen3.resizable(0, 0)
    fen3.mainloop()

def parler():
    textTraitment(en.get())
    en.delete(0, END) 

def textTraitment(text):
    if(str(text) == "" or len(text) == text.count(" ")): return
    textLabel.config(state = NORMAL)
    #textLabel.insert(0.0, time.strftime('%H:%M:%S : ',time.localtime()) +  str(text) + "\n")
    textLabel.insert(0.0, time.strftime('%H:%M:%S : ',time.localtime()) + str(ps.get()) + " : " + str(text) + "\n")
    textLabel.config(state = DISABLED)

def connexion():
    Label(Can2, text = str(ps.get()), bg = colorVert).place(x = 50, y = 2)
    ps.place_forget()
    co.place_forget()
    
    
    
fen = Tk()
fen.title("Othello")
fen.geometry("800x450")
fen.resizable(0, 0)


menubar = Menu(fen)
     
menufichier = Menu(menubar, tearoff = 0)
menufichier.add_command(label = "Nouvelle partie", command = initialisation)
menufichier.add_command(label = "Préférences", command = preferences)
menufichier.add_command(label = "Quitter", command = fen.destroy)

menuaide= Menu(menubar,tearoff=0)
menuaide.add_command(label = "Regles du jeu", command = regles)
menuaide.add_command(label = "A propos de", command = a_propos)

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
en.place(x = 40, y = 400)
textLabel = Text(Can2, state = DISABLED, width = 35, height = 8, font = ("comic sans ms", 10))
textLabel.place(x = 40, y = 200)
Button(fen, text = "Envoyer", command = parler).place(x = 710, y = 400)
fen.bind("<Entree>", parler())
fen.mainloop()
