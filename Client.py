'''
@author: Johann Jacques
'''

import socket
import threading
import time

class ThreadClient(threading.Thread):
    def __init__(self, tHote, tPort):
        threading.Thread.__init__(self)
        self.hote = tHote
        self.port = tPort
        self.nom = "TClient"
        self.aEnvoyer = ""
        self.st = time.time()
        self.Terminated = False
        self.traite = True
        self.start()
        
    def run(self):
        connexionServeur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connexionServeur.connect((self.hote, self.port))
        print("\nConnexion etablie avec le serveur sur le port " + str(self.port))
        message = ""
        while not self.Terminated:
            if time.time() > self.st + 0.1 :
                self.setAEnvoyer("")
                self.st = time.time()
            if not self.traite:
                self.traite = True
                message = self.aEnvoyer
                connexionServeur.send(message.encode())
                messageRecu = connexionServeur.recv(1024).decode()
                print("Reponse serveur: " + str(messageRecu))
        print("Fermeture de la connexion")
        connexionServeur.close()
        
    def stop(self):
        self.Terminated = True
        
    def setAEnvoyer(self, message):
        self.traite = False
        self.aEnvoyer = message

def envoi(messageType, *args):
    global clientThread
    message = str(messageType)
    for arg in args: message += str(arg)
    clientThread.setAEnvoyer(message)

def lancement(hote, port = 50000):
    global clientThread
    clientThread = ThreadClient(hote, port)

def arret():
    global clientThread
    clientThread.stop()
    
global clientThread
clientThread = None
lancement("192.168.228.177")
