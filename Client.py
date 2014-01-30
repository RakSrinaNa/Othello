'''
@author: Johann Jacques
'''

import socket
import threading
from tkinter import*

class ThreadClient(threading.Thread):
    def __init__(self, hh, pp):
        threading.Thread.__init__(self)
        self.hot = hh
        self.por = pp
        self.nom = "TClient"
        self.aenvoyer = ""
        self.Terminated = False
        self.start()
        
    def run(self):
        connexionServeur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connexionServeur.connect((self.hot, self.por))
        print("\nConnexion etablie avec le serveur sur le port " + str(self.por))
        message = ""
        while not self.Terminated:
            if message != self.aenvoyer:
                message = self.aenvoyer
                connexionServeur.send(message.encode())
                messageRecu = connexionServeur.recv(1024).decode()
                print("Reponse serveur: " + str(messageRecu))
        print("Fermeture de la connexion")
        connexionServeur.close()
        
    def stop(self):
        self.Terminated = True

    def envoyer(self, mess):
        self.aenvoyer=mess

def envoii():
    envoi(chatEntry.get(), "")

def envoi(mtype, *args):
    global t
    message = str(mtype)
    for arg in args:
        message += str(arg)
    t.envoyer(message)

def lancement(h,p=50000):
    global t
    t = ThreadClient(h, p)

def arret():
    global t
    t.stop()
    
global t
t = None
fenetre = Tk()
fenetre.title("Othello")
fenetre.geometry("800x450")
fenetre.resizable(0, 0)
lancement("192.168.229.132")
canvasInfos = Canvas(fenetre, bg = "green", height = 450, width = 365)
canvasInfos.place(x = 435, y =0)
chatEntry = Entry(canvasInfos, width = 35)
chatEntry.bind("<Return>", envoii)
chatEntry.place(x = 40, y = 400)
Button(fenetre, text = "Envoyer", command = envoii).place(x = 710, y = 400)
fenetre.mainloop()