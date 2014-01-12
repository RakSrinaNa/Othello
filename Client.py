'''
@author: Johann Jacques
'''

import socket
 
hote = "localhost"
port = ""
 
connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
 
adv_test = "Connexion etablie avec le serveur sur le port {}".format(port)
 
print("\n" + adv_test.upper().center(85))
msg_a_envoyer = b""
while msg_a_envoyer != b"fin":
    msg_a_envoyer = input("> ").encode()
    connexion_avec_serveur.send(msg_a_envoyer)
    msg_recu = connexion_avec_serveur.recv(1024).decode()
    print("Notre serveur à bien reçu {}".format(msg_recu)) 
print("Fermeture de la connexion")
connexion_avec_serveur.close()