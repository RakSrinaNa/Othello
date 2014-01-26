'''
@author: Johann Jacques
'''

import socket

def envoi(type, *args):
    message = str(type)
    for arg in args:
        message += str(arg)
    connexionServeur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexionServeur.connect((hote, port))
    print("\nConnexion etablie avec le serveur sur le port " + str(port))
    while message != b"fin":
        message = input("> ").encode()
        connexionServeur.send(message)
        messageRecu = connexionServeur.recv(1024).decode()
        print("Reponse serveur: " + str(messageRecu))
    print("Fermeture de la connexion")
    connexionServeur.close()
    
hote = "192.168.228.177"
port = 50000
envoi(1, "")
