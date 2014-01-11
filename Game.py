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
    for y2 in range(0, 8):
        if(getColor(x, y2) == color and y2 != y): pawnList.append((x, y2)) #Verifie dans la ligne horizontale
    for x2 in range(0, 8):
        if(getColor(x2, y) == color and x2 != x): pawnList.append((x2, y)) #Verifie dans la ligne verticale
    for y2 in range(0, 8):
        for x2 in range(0, 8):
            if(isDiagonal(x, y, x2, y2) and getColor(x2, y2) == color and x2 != x and y2 != y): pawnList.append((x2, y2)) #Verifie les diagonales
    return pawnList

def isDiagonal(x, y, x2, y2):
    """
    Permet de savoir si le point 2 est sur une diagonale du point 1
    Arguments:
        x -> La position x du pion (horizontale)
        y -> La position y du pion (vertivale)
        x2 -> La position x du pion 2 (horizontale)
        y2 -> La position y du pion 2 (vertivale)
    Return:
        True -> Le pion est sur une diagonale
        False -> Le pion n'est pas sur une diagonale
    """
    if(abs(x2 - x) == abs(y2 - y)): return True
    return False
      
def hasGoodEnd(color, coordBase, coordTo):
    """
    Permet de savoir si cette ligne a une fin possible
    Arguments:
        color -> La a verifier
        coordBase -> Les coordonnes du pion origine
        coordTo -> Les coordonnes du point d'arrive
    Return:
        True -> Si la fin est possible
        False -> Si la fin n'est pas possible
    """
    dx = coordTo[0] - coordBase[0]
    dy = coordTo[1] - coordBase[1]
    tx = coordBase[0]
    ty = coordBase[1]
    while(tx != coordTo[0] or ty != coordTo[1]):
        if(grid[ty][tx] == 0): return False
        if(grid[ty][tx] == color):
            if(abs(tx - coordBase[0]) < 2 or abs(ty - coordBase[1]) < 2): return False
            else: return True
        if(dx != 0): tx = int(tx + copysign(1, dx))
        if(dy != 0): ty = int(ty + copysign(1, dy))
    return False

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
        if(grid[ty][tx] == color and (tx != coordBase[0] or ty != coordBase[1])): return
        grid[ty][tx] = color
        if(dx != 0): tx = int(tx + copysign(1, dx))
        if(dy != 0): ty = int(ty + copysign(1, dy))
    grid[coordTo[1]][coordTo[0]] = color
    
def hasPawnNext(color, x, y):
    """
    Permet de savoir si un pion est entoure d'autres pions
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
        -1 -> Pas d'errur detectee
        0 -> Case deja occupee
        1 -> Impossible de placer le pion
    """
    if(getColor(x, y) == 3 or not hasPawnNext(color, x, y)): return 1
    elif(getColor(x, y) != 0): return 0
    grid[y][x] = color
    try:
        for l in detectPawn(color, x, y):
            if(hasGoodEnd(color, (x, y), l)): reverse(color, (x, y), l)
    except IndexError: return 1
    showGrid()
    return -1
    
def showGrid():
    """
    Permet d'afficher la grille dans la console
    """
    for l in grid: print(l)
    print()
    
grid = [[0 for x in range (8)] for x in range (8)]
init()
place(2, 3, 2)
place(1, 4, 2)
place(2, 5, 2)
place(1, 4, 1)
place(2, 5, 4)