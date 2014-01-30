'''
@author: Thomas Couchoud
'''

from math import copysign

def init():
    """
    Permet d'initialiser la grille du jeu
    """
    for y in range(8):
        for x in range(8):
            grille[y][x] = 0
    grille[3][3] = 1
    grille[4][3] = 2
    grille[4][4] = 1
    grille[3][4] = 2

def getNumberColor(color):
    """
    Permet de compter le nombre de pions sur la grille (Couleur 0 pour savoir le nombre de cases vides)
    Arguments:
        color -> La couleur du pion a compter
    Return:
        Le nombre de pions de la couleur demmandee presents sur la grille
    """
    count = 0
    for y in range(0, 8):
        for x in range(0, 8):
            if(getColor(x, y) == color): count += 1
    return count

def getColor(x , y):
    """
    Permet de connaitre le pion sur la case
    Arguments:
        x -> La position x du pion (horizontale)
        y -> La position y du pion (verticale)
    Return:
        0 -> Case vide
        1 -> Couleur 1
        2 -> Couleur 2
        3 -> Hors de la grille
    """
    if(x < 0 or x > 7 or y < 0 or y > 7): return 3 #Hors de la grille
    return grille[y][x]

def detectPawn(color, x, y):
    """
    Permet de connaitre les pions de meme couleur qui sont sur les memes lignes
        Arguments:
        color -> La couleur du pion
        x -> La position x du pion (horizontale)
        y -> La position y du pion (verticale)
    Return:
        Une liste de tableaux bi-dimensionnels contenant les positions des pions trouves
    """
    pawnList = []
    isEating = False
    for temporaryY in range(y, 8):
        if(getColor(x, temporaryY) == color and temporaryY != y and isEating): #Verifie dans la ligne horizontale en dessous
            pawnList.append((x, temporaryY))
            break
        elif(getColor(x, temporaryY) == color and temporaryY != y and not isEating): break
        elif(getColor(x, temporaryY) == 0 and temporaryY != y): break
        elif(getColor(x, temporaryY) != color and getColor(x, temporaryY) != 0 and getColor(x, temporaryY) != 3): isEating = True
    isEating = False
    for temporaryY in range(0, y + 1):
        if(getColor(x, y - temporaryY) == color and (y - temporaryY) != y and isEating): #Verifie dans la ligne horizontale au dessus
            pawnList.append((x, y - temporaryY))
            break
        elif(getColor(x, y - temporaryY) == color and (y - temporaryY) != y and not isEating): break
        elif(getColor(x, y - temporaryY) == 0 and (y - temporaryY) != y): break
        elif(getColor(x, y - temporaryY) != color and getColor(x, y - temporaryY) != 0 and getColor(x, y - temporaryY) != 3): isEating = True
    isEating = False
    for temporaryX in range(x, 8):
        if(getColor(temporaryX, y) == color and temporaryX != x and isEating): #Verifie dans la ligne verticale a droite
            pawnList.append((temporaryX, y))
            break
        elif(getColor(temporaryX, y) == color and temporaryX != x and not isEating):break
        elif(getColor(temporaryX, y) == 0 and temporaryX != x):break
        elif(getColor(temporaryX, y) != color and getColor(temporaryX, y) != 0 and getColor(temporaryX, y) != 3): isEating = True
    isEating = False
    for temporaryX in range(0, x + 1):
        if(getColor(x - temporaryX, y) == color and (x - temporaryX) != x and isEating): #Verifie dans la ligne verticale a gauche
            pawnList.append((x - temporaryX, y))
            break
        elif(getColor(x - temporaryX, y) == color and (x - temporaryX) != x and not isEating):break
        elif(getColor(x - temporaryX, y) == 0 and (x - temporaryX) != x):break
        elif(getColor(x - temporaryX, y) != color and getColor(x - temporaryX, y) != 0 and getColor(x - temporaryX, y) != 3): isEating = True
    isEating = False
    diagonal1, diagonal2, diagonal3, diagonal4 = getNextPawnDiagonal(color, 1, 1, x, y), getNextPawnDiagonal(color, 1, -1, x, y), getNextPawnDiagonal(color, -1, 1, x, y), getNextPawnDiagonal(color, -1, -1, x, y)
    if(diagonal1 != None):pawnList.append(diagonal1) #Diagonale + +
    if(diagonal2 != None):pawnList.append(diagonal2) #Diagonale + -
    if(diagonal3 != None):pawnList.append(diagonal3) #Diagonale - +
    if(diagonal4 != None):pawnList.append(diagonal4) #Diagonale - -
    print(pawnList)
    return pawnList

def getNextPawnDiagonal(color, directionX, directionY, x, y):
    """
    Permet d'avoir la position du pion le plus proche de l'autre couleur dans une diagonale
    Arguments:
        color -> La couleur du pion joue
        directionX -> Le sens de deplacement selon x (-1 ou 1)
        directionY -> Le sens de deplacement selon y (-1 ou 1)
        x -> La position x du pion (horizontale)
        y -> La position y du pion (verticale)
    Return:
        Un tableau bi-dimensionnel contenant la position du pion trouve
    """
    if(abs(directionX) != 1 or abs(directionY) != 1): return
    x += directionX
    y += directionY
    isEating = False
    while(getColor(x, y) != 3):
        if(getColor(x, y) == 0): return
        if(getColor(x, y) != color): isEating = True
        if(getColor(x, y) == color and isEating): return (x, y)
        elif(getColor(x, y) == color and not isEating): return
        x += directionX
        y += directionY
    return

def reverse(color, coordinateBase, coordinateTo):
    """
    Permet de savoir si le point 2 est sur une diagonale du point 1
    Arguments:
        color -> La couleur a mettre
        coordinateBase -> Les coordonnes du pion origine
        coordinateTo -> Les coordonnes du point d'arrive
    """
    deltaX = coordinateTo[0] - coordinateBase[0]
    deltaY = coordinateTo[1] - coordinateBase[1]
    temporaryX = coordinateBase[0]
    temporaryY = coordinateBase[1]
    while(temporaryX != coordinateTo[0] or temporaryY != coordinateTo[1]):
        grille[temporaryY][temporaryX] = color
        if(deltaX != 0): temporaryX = int(temporaryX + copysign(1, deltaX))
        if(deltaY != 0): temporaryY = int(temporaryY + copysign(1, deltaY))
    grille[coordinateTo[1]][coordinateTo[0]] = color
    
def hasPawnNext(color, x, y):
    """
    Permet de savoir si un pion est entoure d'autres pions d'une autre couleur
    Arguments:
        x -> La position x du pion (horizontale)
        y -> La position y du pion (vertivale)
    Return:
        True -> Le pion est entoure d'autres pions
        False -> Le pion n'est pas entoure d'autres pions
    """
    xMin = x - 1
    xMax = x + 1
    if(xMin < 0): xMin = 0
    if(xMax > 7): xMax = 7
    yMin = y - 1
    yMax = y + 1
    if(yMin < 0): yMin = 0
    if(yMax > 7): yMax = 7
    for temporaryY in range(yMin, yMax + 1):
        for temporaryX in range(xMin, xMax + 1):
            if(getColor(temporaryX, temporaryY) != 0 and getColor(temporaryX, temporaryY) != color and (temporaryX != x or temporaryY != y)): return True
    return False

def place(color, x , y):
    """
    Permet de placer un pion
    Arguments:
        color -> La couleur du pion joue (1 = blanc, 2 = noir)
        x -> La position x du pion (horizontale)
        y -> La position y du pion (vertivale)
    Return:
        0 -> Pas d'errur detectee
        1 -> Case deja occupee
        2 -> Impossible de placer le pion
    """
    if(getColor(x, y) == 3 or not hasPawnNext(color, x, y)): return 2
    elif(getColor(x, y) != 0): return 1
    try:
        pawnList = detectPawn(color, x, y)
        if(len(pawnList) < 1): return 2
        for l in pawnList:
            reverse(color, (x, y), l)
    except IndexError: return 2
    grille[y][x] = color
    return 0

def showGrid():
    for l in grille:
        print(l)
    print()
    
grille = [[0 for x in range (8)] for x in range (8)]
init()
