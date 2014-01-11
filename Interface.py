'''
@author: Olivier Froger
'''
from tkinter import*
from Game import*
def initialisation():
    init()
    for x in range (0,8):
        for y in range (0,8):
            placer_pion(getColor(x,y),x,y)
def règles():
    fen1=Tk()
    fen1.title("Règles du jeu")
    fen1.geometry("500x500")
    fen1.resizable(0,0)
    fen1.mainloop()

def préférences():
    fen2=Tk()
    fen2.title("Préférences")
    fen2.geometry("500x500")
    fen2.resizable(0,0)
    fen2.mainloop()

def placer_pion(color,x,y):
    tc=50
    dec=25
    dec2=5
    col=vert
    bl="black"
    if color==blanc: col="white"
    elif color==noir: col="black"
    else: bl=vert
    Can.create_oval(dec+x*tc+dec2,dec+y*tc+dec2,dec+tc*(x+1)-dec2,dec+tc*(y+1)-dec2,fill=col,outline=bl)
vert="#086126"
blanc=1
noir=2

fen=Tk()
fen.title("Othello")
fen.geometry("800x450")
fen.resizable(0,0)

menubar = Menu(fen)
     
menufichier= Menu(menubar,tearoff=0)
menufichier.add_command(label="Nouvelle partie",command=initialisation)
menufichier.add_command(label="Préférences",command=préférences)
menufichier.add_command(label="Quitter",command=fen.destroy)
menubar.add_cascade(label="Fichier",menu=menufichier)

menuaide= Menu(menubar,tearoff=0)
menuaide.add_command(label="Règles du jeu",command=règles)
menuaide.add_command(label="A propos de")
menubar.add_cascade(label="Aide",menu=menuaide)

fen.config(menu=menubar)

Can=Canvas(fen,bg=vert,height=435,width=435)
Can.place(x=10,y=10)
yo=2
xo=8
Comic=("Comic sans MS","9")
Label(Can,text="A",font=Comic,bg=vert).place(x=45,y=yo)
Label(Can,text="B",font=Comic,bg=vert).place(x=95,y=yo)
Label(Can,text="C",font=Comic,bg=vert).place(x=145,y=yo)
Label(Can,text="D",font=Comic,bg=vert).place(x=195,y=yo)
Label(Can,text="E",font=Comic,bg=vert).place(x=245,y=yo)
Label(Can,text="F",font=Comic,bg=vert).place(x=295,y=yo)
Label(Can,text="G",font=Comic,bg=vert).place(x=345,y=yo)
Label(Can,text="H",font=Comic,bg=vert).place(x=395,y=yo)
Label(Can,text="1",font=Comic,bg=vert).place(x=xo,y=40)
Label(Can,text="2",font=Comic,bg=vert).place(x=xo,y=90)
Label(Can,text="3",font=Comic,bg=vert).place(x=xo,y=140)
Label(Can,text="4",font=Comic,bg=vert).place(x=xo,y=190)
Label(Can,text="5",font=Comic,bg=vert).place(x=xo,y=240)
Label(Can,text="6",font=Comic,bg=vert).place(x=xo,y=290)
Label(Can,text="7",font=Comic,bg=vert).place(x=xo,y=340)
Label(Can,text="8",font=Comic,bg=vert).place(x=xo,y=390)
x1,x2,y1,y2=25,25,25,25


for i in range (0,9):
    Can.create_line(x1,y1,x1+400,y1)
    y1+=50
    Can.create_line(x2,y2,x2,y2+400)
    x2+=50
initialisation()

Label(fen,text="Othello",font=Comic).place(x=610,y=5)
fen.mainloop()
