'''
@author: Johann Jacques
'''
import socket
import select
 
hote = "localhost"
port = "" 
 
connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)

serv_adv = "Bienvenue sur le serveur OTEHLLO(port : {})".format(port)

print("\n" + serv_adv.upper().center(85) + "\nTraitement des données :\n")
serveur_lance = True
clients_connectes = []

while serveur_lance:
    connexions_demandees, wlist, xlist = select.select([connexion_principale], [], [], 0.05)
    for connexion in connexions_demandees:
        connexion_avec_client, infos_connexion = connexion.accept()
        clients_connectes.append(connexion_avec_client)
    clients_a_lire = []
    try:
        clients_a_lire, wlist, xlist = select.select(clients_connectes, [], [], 0.05)
    except select.error:
        pass
    else:
        for client in clients_a_lire:
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