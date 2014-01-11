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
            grid[y][x] = 0
    grid[3][3] = 1
    grid[4][3] = 2
    grid[4][4] = 1
    grid[3][4] = 2
    showGrid()

def getnumberColor(color):
    """
    Permet de compter le nombre de pions sur la grille (Couleur 0 pour savoir le nombre de cases vides)
    Arguments:
        color -> La couleur du pion a compter
    Return:
        Le nombre de pions de la couleur demmandee presents sur la grille
    """
    number = 0
    for y in range(0, 8):
        for x in range(0, 8):
            if(getColor(x, y) == color): number += 1
    return number

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
    return grid[y][x]

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
    for y2 in range(y, 8):
        if(getColor(x, y2) == color and y2 != y and isEating): #Verifie dans la ligne horizontale en dessous
            pawnList.append((x, y2))
            break
        elif(getColor(x, y2) == color and y2 != y and not isEating): break
        elif(getColor(x, y2) != color and getColor(x, y2) != 0 and getColor(x, y2) != 3): isEating = True
    isEating = False
    for y2 in range(0, y + 1):
        if(getColor(x, y - y2) == color and (y - y2) != y and isEating): #Verifie dans la ligne horizontale au dessus
            pawnList.append((x, y - y2))
            break
        elif(getColor(x, y - y2) == color and (y - y2) != y and not isEating): break
        elif(getColor(x, y - y2) != color and getColor(x, y - y2) != 0 and getColor(x, y - y2) != 3): isEating = True
    isEating = False
    for x2 in range(x, 8):
        if(getColor(x2, y) == color and x2 != x and isEating): #Verifie dans la ligne verticale a droite
            pawnList.append((x2, y))
            break
        elif(getColor(x2, y) == color and x2 != x and not isEating):break
        elif(getColor(x2, y) != color and getColor(x2, y) != 0 and getColor(x2, y) != 3): isEating = True
    isEating = False
    for x2 in range(0, x + 1):
        if(getColor(x - x2, y) == color and (x - x2) != x and isEating): #Verifie dans la ligne verticale a gauche
            pawnList.append((x - x2, y))
            break
        elif(getColor(x - x2, y) == color and (x - x2) != x and not isEating):break
        elif(getColor(x - x2, y) != color and getColor(x - x2, y) != 0 and getColor(x - x2, y) != 3): isEating = True
    isEating = False
    d1, d2, d3, d4 = getNextPawnDiagonal(color, 1, 1, x, y), getNextPawnDiagonal(color, 1, -1, x, y), getNextPawnDiagonal(color, -1, 1, x, y), getNextPawnDiagonal(color, -1, -1, x, y)
    if(d1 != None):pawnList.append(d1) #Diagonale + +
    if(d2 != None):pawnList.append(d2) #Diagonale + -
    if(d3 != None):pawnList.append(d3) #Diagonale - +
    if(d4 != None):pawnList.append(d4) #Diagonale - -
    return pawnList

def getNextPawnDiagonal(color, sx, sy, x, y):
    """
    Permet d'avoir la position du pion le plus proche de l'autre couleur dans une diagonale
    Arguments:
        color -> La couleur du pion joue
        sx -> Le sens de deplacement selon x (-1 ou 1)
        sy -> Le sens de deplacement selon y (-1 ou 1)
        x -> La position x du pion (horizontale)
        y -> La position y du pion (verticale)
    Return:
        Un tableau bi-dimensionnel contenant la position du pion trouve
    """
    if(abs(sx) != 1 or abs(sy) != 1): return
    x += sx
    y += sy
    isEating = False
    while(getColor(x, y) != 3):
        if(getColor(x, y) == 0): return
        if(getColor(x, y) != color): isEating = True
        if(getColor(x, y) == color and isEating): return (x, y)
        elif(getColor(x, y) == color and not isEating): return
        x += sx
        y += sy
    return

def reverse(color, coordBase, coordTo):
    """
    Permet de savoir si le point 2 est sur une diagonale du point 1
    Arguments:
        color -> La couleur a mettre
        coordBase -> Les coordonnes du pion origine
        coordTo -> Les coordonnes du point d'arrive
    """
    dx = coordTo[0] - coordBase[0]
    dy = coordTo[1] - coordBase[1]
    tx = coordBase[0]
    ty = coordBase[1]
    while(tx != coordTo[0] or ty != coordTo[1]):
        grid[ty][tx] = color
        if(dx != 0): tx = int(tx + copysign(1, dx))
        if(dy != 0): ty = int(ty + copysign(1, dy))
    grid[coordTo[1]][coordTo[0]] = color
    
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
    x2 = x - 1
    x3 = x + 1
    if(x2 < 0): x2 = 0
    if(x3 > 7): x3 = 7
    y2 = y - 1
    y3 = y + 1
    if(y2 < 0): y2 = 0
    if(y3 > 7): y3 = 7
    for y4 in range(y2, y3 + 1):
        for x4 in range(x2, x3 + 1):
            if(getColor(x4, y4) != 0 and getColor(x4, y4) != color and (x4 != x or y4 != y)): return True
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
        list = detectPawn(color, x, y)
        if(len(list) < 1): return 2
        for l in list:
            reverse(color, (x, y), l)
    except IndexError: return 2
    grid[y][x] = color
    #showGrid()
    print()
    return 0
    
def showGrid():
    """
    Permet d'afficher la grille dans la console
    """
    for l in grid: print(l)
    print()
    
grid = [[0 for x in range (8)] for x in range (8)]
init()