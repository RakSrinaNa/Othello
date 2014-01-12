'''
@author: Johann Jacques
'''
import socket
import select
 
hote = 'localhost'
port = 
 
connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)

#print("Bienvenue sur le serveur Area Online (port : {})".format(port))
serv_adv="Bienvenue sur le serveur OTEHLLO(port : {})".format(port)

print("\n")
print(serv_adv.upper().center(85))
print("\n")
print("Traitement des données :\n")
serveur_lance = True
clients_connectes = []

while serveur_lance:
    
	
    connexions_demandees, wlist, xlist = select.select([connexion_principale],
        [], [], 0.05)
     
    for connexion in connexions_demandees:
        connexion_avec_client, infos_connexion = connexion.accept()
        # On ajoute le socket connecté à la liste des clients
        clients_connectes.append(connexion_avec_client)

    clients_a_lire = []
    try:
        clients_a_lire, wlist, xlist = select.select(clients_connectes,
                [], [], 0.05)
    except select.error:
        pass
    else:
        # On parcourt la liste des clients à lire
        for client in clients_a_lire:
            # Client est de type socket
            msg_recu = client.recv(1024)
            msg_recu = msg_recu.decode()
            print("{} .....100%".format(msg_recu))
            msg_recu = msg_recu.encode()
            client.send(msg_recu)
            if msg_recu == "fin":
                serveur_lance = False      
 
print("Fermeture des connexions")
for client in clients_connectes:
    client.close()
 
connexion_principale.close()




//////////////// partie client qui teorie pas comme ca mais faut que j arrange ca///////////////
import socket
 
hote = "localhost"
port = 
 
connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
 
adv_test="Connexion etablie avec le serveur sur le port {}".format(port)
 
print("\n")
print(adv_test.upper().center(85))
msg_a_envoyer = b""
while msg_a_envoyer != b"fin":
    msg_a_envoyer = input("> ")
    msg_a_envoyer = msg_a_envoyer.encode()
    connexion_avec_serveur.send(msg_a_envoyer)
    msg_recu = connexion_avec_serveur.recv(1024)
    msg_recu=msg_recu.decode()
    print("Notre serveur à bien reçu {}".format(msg_recu)) 
                 
print("Fermeture de la connexion")
connexion_avec_serveur.close()