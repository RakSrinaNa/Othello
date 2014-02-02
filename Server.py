'''
@author: Johann Jacques
'''

import socket
import select
import threading

class ThreadServer(threading.Thread):
    def __init__(self ,tHote, tPort):
        threading.Thread.__init__(self)
        self.hote = thote
        self.port = tPort
        self.nom = "TServer"
        self.Terminated = False
        self.start()
        
    def run(self):
        connexionPrincipale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connexionPrincipale.bind((self.hote, self.port))
        connexionPrincipale.listen(5)
        server = "Bienvenue sur le serveur OTHELLO(port : {})".format(self.port)
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
                messageRecu = messageRecu.encode()
                client.send(messageRecu)  
        print("Fermeture des connexions")
        for client in clientsConnectes:
            client.close()
        connexionPrincipale.close()
        
    def stop(self):
        self.Terminated = True

def lancement(hote = gethostbyname(gethostname()), port = 50000):
    global serverThread
    serverThread = ThreadServer(hote, port)

def arret():
    global serverThread
    serverThread.stop()
    
global serverThread
serverThread = None
lancement()