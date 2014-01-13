'''
@author: Johann Jacques
'''

import socket
import binascii

def envoi(type, *args):
    message = str(type)
    for arg in args:
        message += str(arg)
    connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion_avec_serveur.connect((hote, port))
    print("\n" + "Connexion etablie avec le serveur sur le port {}".format(port).upper().center(85))
    while message != b"fin":
        message = input("> ").encode()
        connexion_avec_serveur.send(message)
        msg_recu = connexion_avec_serveur.recv(1024).decode()
        print("Notre serveur a bien recu {}".format(msg_recu))
    print("Fermeture de la connexion")
    connexion_avec_serveur.close()
    
hote = "192.168.228.177"
port = 28960
envoi(0, 1, 5, 7)