nbMines = 2
EstPremierClic = True

def genererTableau():
    global mineTab
    
    mineTab = []
    
    for i in range(globLargeur):
        mineTab.append([])
        
        for j in range(globHauteur):
            mineTab[i].append([False, 0, "blank"])
            
def melanger(nbElem):    
    resultat = []
    
    for i in range(nbElem):
        resultat.append(i)
        
    n = nbElem - 1
        
    while n > 0: # Fisher-Yates
        index = math.floor((n + 1) * random())
        
        temp = resultat[n]
        resultat[n] = resultat[index]
        resultat[index] = temp
        
        n -= 1
    
    return resultat
    
def genererMines(x,y):
    global nbMines
    premierClic = [x,y]
    
    positions = melanger(globLargeur * globHauteur)
    
    positions.pop(positions.index(premierClic[0]*globHauteur + premierClic[1]))
    
    for pos in positions[:nbMines]:
        mineTab[pos // globHauteur][pos % globHauteur][0] = True
        
def calculerProximite(posX, posY):
    
    if   posX == 0:             rangeX = [0, 1]
    elif posX == globLargeur-1: rangeX = [-1, 0]
    else:                       rangeX = [-1, 0, 1]
        
    if   posY == 0:             rangeY = [0, 1]
    elif posY == globHauteur-1: rangeY = [-1, 0]
    else:                       rangeY = [-1, 0, 1]
    
    for i in rangeX:
        for j in rangeY:
            mineTab[posX][posY][1] += mineTab[posX + i][posY + j][0]
            
def chaineDevoiler(inX, inY):
    global globLargeur
    global globHauteur
    if mineTab[inX][inY][0] == False and mineTab[inX][inY][2] == "blank":
        mineTab[inX][inY][2] = "open"
        if mineTab[inX][inY][1] == 0:
            if (inX-1) >= 0:
                chaineDevoiler((inX-1), (inY))
                if (inY-1) >= 0:
                    chaineDevoiler((inX-1), (inY-1))
                    
                if (inY+1) < globHauteur:
                    chaineDevoiler((inX-1), (inY+1))
                    
            if (inY-1) >= 0:
                chaineDevoiler((inX), (inY-1))
                    
            if (inY+1) < globHauteur:
                chaineDevoiler((inX), (inY+1))
                    
            if (inX+1) < globLargeur:
                chaineDevoiler((inX+1), (inY))
                
                if (inY-1) >= 0:
                    chaineDevoiler((inX+1), (inY-1))
                    
                if (inY+1) < globHauteur:
                    chaineDevoiler((inX+1), (inY+1))
            
def devoiler(posX, posY, shift):
    global nbBlanks
    global echec  #NEW
    if shift == True:
        if mineTab[posX][posY][2] == "blank":
            mineTab[posX][posY][2]= "flag"
            afficherEcran()
            return
        if mineTab[posX][posY][2] == "flag":
            mineTab[posX][posY][2] = "blank"
            afficherEcran()
            return
            
 
    if shift == False:
        if mineTab[posX][posY][2] == "blank":
            if mineTab[posX][posY][0] == True:
                mineTab[posX][posY][2] = "mine-red"
                echec=True #NEW
                
            if mineTab[posX][posY][0] == False:
                chaineDevoiler(posX, posY)
            
def afficherCase(tab):
    resultat = '<img src="http://codeboot.org/images/minesweeper/'
    
    if tab[2] in ["blank", "flag", "mine", "mine-red", "mine-red-x"]:
        resultat += tab[2]
        
    elif tab[2] == "open":
        resultat += str(tab[1])
        
    return resultat + '.png">'

def afficherEcran():
    global nbBlanks
    tempNbBlanks = 0
    tuiles = []
    
    for i in range(globLargeur):
        tuiles.append([])
        for j in range(globHauteur):
            tuiles[i].append(document.querySelector("#tuile" +\
                                                    str(i * globHauteur + j)))
            tuiles[i][j].innerHTML = afficherCase(mineTab[i][j])
            if mineTab[i][j][2] == "blank":
                tempNbBlanks +=1
            nbBlanks = tempNbBlanks

#Procédure qui prend en charge toutes les actions en lien avec un click sur
#une tuile du démineur. Par défaut, la variable isPremierClick sera True, 
#ce qui veut dire que la partie else de la fonction sera exécutée la première
#fois (ensuite isPremierClick deviendra False et la partie if sera utilisée).
def click(x ,y , shift):
    global globLargeur
    global globHauteur
    global EstPremierClic
    global mineTab
    global echec #NEW?
    global nbBlanks
       
    if (EstPremierClic == False) and mineTab[x][y][2] in ["blank", "flag"]:
        devoiler(x,y,shift)
        afficherEcran()
        
    if (EstPremierClic == True) and mineTab[x][y][2] == "blank":
        EstPremierClic = False
        genererMines(x,y)
        for i in range(globLargeur):
            for j in range(globHauteur):
                calculerProximite(i,j)
        devoiler(x,y,shift)
        afficherEcran()
    
    if echec==True:   #NEWWWWWWW ALL THE WAY
        return (fin(False))
    if nbBlanks == 0:
        return (fin(True))
                
def fin(victoire):
    global globLargeur
    global globHauteur
    for i in range(globLargeur):
        for j in range(globHauteur):
            if mineTab[i][j][2] == "blank":
                if mineTab[i][j][0] == True:
                    mineTab[i][j][2] = "mine"
            if mineTab[i][j][2] == "flag":
                if mineTab[i][j][0] == True:
                    mineTab[i][j][2] = "mine-red-x"
    afficherEcran()
    if victoire == True:
        sleep(1)
        alert("Victoire, veuillez rafraichir le programme")
        
    elif victoire == False:
        sleep(1)
        alert("Partie terminée")
        
    init(globLargeur, globHauteur) #NEW. SLIGHTLY DIFFERENT ABOVE TOO
    
            
def init(largeur, hauteur):
    global globLargeur
    global globHauteur
    global EstPremierClic
    global nbBlanks
    global echec #NEW
    globLargeur = largeur
    globHauteur = hauteur
    echec=False #NEW AND IMPORTANT
    print("Chargement...")
    
    nomsImages = ["0", "1", "2", "3", "4", "5", "6", "7", "8",\
                  "blank", "flag", "mine", "mine-red", "mine-red-x"]
    
    main = document.querySelector('#main')
    main.innerHTML = ""
    
    for nom in nomsImages:
        main.innerHTML += '  <link rel="preload" href="http://codeboot.org/'\
        + 'images/minesweeper/' + nom + '.png">\n'

    main.innerHTML += """
      <style>
      #main table {
        border: 1px solid black;
        margin: 10px;
      }
      #main table td {
        width: 30px;
        height: 30px;
        border: none;
      }
      </style>
      <table id="grid">
      </table>"""
    
    txtGrid = ""
    
    genererTableau()
    
    for y in range(hauteur):
        txtGrid += "<tr>"
        
        for x in range(largeur):
            numeroDeTuile = x * hauteur + y
            
            txtGrid += '\n  <td onclick=click(' + str(x) + ',' + str(y) + ','\
            + 'event.shiftKey'  + ') id="tuile' + str(numeroDeTuile) +\
            '"></td>'
                        
        txtGrid += "\n</tr>"
        
    grid = document.querySelector("#grid")
    grid.innerHTML = txtGrid
    nbBlanks = largeur*hauteur
    afficherEcran()
    EstPremierClic = True
    print("Prêt")
    
init(5,5)


