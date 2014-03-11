'''
@author: Johann Jacques
'''

import socket
import time
import threading

class ThreadClient(threading.Thread):
    def __init__(self, tHote, tPort):
        threading.Thread.__init__(self)
        self.hote = tHote
        self.port = tPort
        self.nom = "TClient"
        self.aEnvoyer = ""
        self.Terminated = False
        self.start()
        
    def run(self):
        self.timer = time.time()
        connexionServeur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connexionServeur.connect((self.hote, self.port))
        print("\nConnexion etablie avec le serveur sur le port " + str(self.port))
        message = ""
        while not self.Terminated:
            if message != self.aEnvoyer:
                message = self.aEnvoyer
                connexionServeur.send(message.encode())
                messageRecu = connexionServeur.recv(1024).decode()
                print("Reponse serveur: " + str(messageRecu))
            if time.time() - self.timer > 0.5:
                self.time = time.time()
                connexionServeur.send("9".encode())
                messageRecu = connexionServeur.recv(1024).decode()
                print("Reponse serveur: " + str(messageRecu))
        print("Fermeture de la connexion")
        connexionServeur.close()
        
    def stop(self):
        self.Terminated = True
        
    def setAEnvoyer(self, message):
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
