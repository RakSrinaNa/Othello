'''
@author: Johann Jacques
'''
from TransmissionDecrypter import decrypt
import socket
import select
import threading

class ThreadServer(threading.Thread):    
    def __init__(self , tHote = socket.gethostbyname(socket.gethostname()), tPort = 50000):
        threading.Thread.__init__(self)
        self.hote = tHote
        self.port = tPort
        self.nom = "TServer"
        self.Terminated = False
        self.start()
        
    def run(self):
        connexionPrincipale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connexionPrincipale.bind((self.hote, self.port))
        connexionPrincipale.listen(5)
        server = "Bienvenue sur le serveur OTHELLO ({}:{})".format(self.hote, self.port)
        print("\n" + server.upper().center(85) + "\nTraitement des donnees :\n")
        clientsConnectes = []
        while not self.Terminated:
            connexionsEntrantes, wlist, xlist = select.select([connexionPrincipale], [], [], 0.05)
            for connexion in connexionsEntrantes:
                connexionClient, infosConnexion = connexion.accept()
                clientsConnectes.append(connexionClient)
            clientsALire = []
            try:
                clientsALire, wlist, xlist = select.select(clientsConnectes, [], [], 0.05)
            except select.error:
                pass
            for client in clientsALire:
                messageRecu = client.recv(1024)
                messageRecu = messageRecu.decode()
                print("> " + messageRecu)
                client.send(decrypt(messageRecu).encode())
        print("Fermeture des connexions")
        for client in clientsConnectes:
            client.close()
        connexionPrincipale.close()
        
    def stop(self):
        self.Terminated = True

def lancement_serv():
    global serverThread
    serverThread = ThreadServer()

def arret_serv():
    global serverThread
    serverThread.stop()
    
global serverThread
serverThread = None
