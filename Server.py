'''
@author: Johann Jacques
'''
import socket
import select
 
hote, port = "192.168.228.177", 50000
 
connexionPrincipale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexionPrincipale.bind((hote, port))
connexionPrincipale.listen(5)

server = "Bienvenue sur le serveur OTEHLLO(port : {})".format(port)

print("\n" + server.upper().center(85) + "\nTraitement des donnees :\n")
serveurLance = True
clientsConnectes = []
while serveurLance:
    connexionsEntrantes, wlist, xlist = select.select([connexionPrincipale], [], [], 0.05)
    for connexion in connexionsEntrantes:
        connexionClient, infosConnexion = connexion.accept()
        clientsConnectes.append(connexionClient)
    clientsALire = []
    try:
        clientsALire, wlist, xlist = select.select(clientsConnectes, [], [], 0.05)
    except select.error:
        pass
    else:
        for client in clientsALire:
            messageRecu = client.recv(1024)
            messageRecu = messageRecu.decode()
            if str(messageRecu) == "fin":
                serveurLance = False
            print("> " + messageRecu)
            messageRecu = messageRecu.encode()
            client.send(messageRecu)  
print("Fermeture des connexions")
for client in clientsConnectes:
    client.close()
connexionPrincipale.close()
