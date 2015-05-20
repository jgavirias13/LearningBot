import chess
import fichas
import random

grafo = []
aristas = []
tabs = {}
actual = []

#Define la funcion del color que debe de ir la casilla cuando esta vacia el tablero
def colorCasilla(pos):
    div = pos/8
    mod = pos%2
    moddiv = div%2
    if moddiv == 0:
        if mod == 0:
            return "b"
        return "B"
    if mod == 0:
        return "B"
    return "b"

def jaque(tab):
    a = 0
    jug = 0
    if (tab.strTab[64] == '0'):
        a = tab.strTab.find('K')
        jug = 1
    else:
        a = tab.strTab.find('k')
    seg = 1
    mov = 1
    #Verifica si hay jaque al rey hacia arriba.
    while seg:
        aux = a + 8*mov
        if (aux < 64):
            if (tab.tablero[aux].jugador == "n"): #Verifica si esta vacia la casilla
                mov = mov + 1
            elif (tab.tablero[aux].jugador == jug): #Verifica si en la casilla hay una pieza propia
                seg = 0
            else:
                if (-8) in tab.tablero[aux].come and mov in tab.tablero[aux].movimientos: #Verifica si la casilla que hace el jaque si puede
                    print "jaque"                                                         #hacer el movimiento para comer
                    return 1
                else:
                    seg = 0
        else:
            seg = 0
    seg = 1
    mov = 1
    #Verifica si hay jaque al rey hacia abajo.
    while seg:
        aux = a - 8*mov
        if(aux > 0):
            if (tab.tablero[aux].jugador == "n"):
                mov = mov + 1
            elif (tab.tablero[aux].jugador == jug):
                seg = 0
            else:
                if (8) in tab.tablero[aux].come and mov in tab.tablero[aux].movimientos:
                    print "jaque"
                    return 1
                else:
                    seg = 0
        else:
            seg = 0
    seg = 1
    mov = 1
    #Verifica si hay jaque desde la derecha.
    while seg:
        aux = a + 1*mov
        #Condiciona si el jaque es en la misma fila
        if (a/8 == aux/8):
            if (tab.tablero[aux].jugador == "n"):
                mov = mov + 1
            elif (tab.tablero[aux].jugador == jug):
                seg = 0
            else:
                if (-1) in tab.tablero[aux].come and mov in tab.tablero[aux].movimientos:
                    print "jaque"
                    return 1
                else:
                    seg = 0
        else:
            seg = 0
    seg = 1
    mov = 1
    #Verifica si hay jaque desde la izquierda.
    while seg:
        aux = a - 1*mov
        if (a/8 == aux/8):
            if (tab.tablero[aux].jugador == "n"):
                mov = mov + 1
            elif (tab.tablero[aux].jugador == jug):
                seg = 0
            else:
                if (1) in tab.tablero[aux].come and mov in tab.tablero[aux].movimientos:
                    print "jaque"
                    return 1
                else:
                    seg = 0
        else:
            seg = 0
    seg = 1
    mov = 1
    #Verifica el jaque desde la diagonal abajo derecha
    while seg:
        aux = a + 9*mov
        if (aux < 64 and a/8 == aux/8 - mov):
            if (tab.tablero[aux].jugador == "n"):
                mov = mov + 1
            elif (tab.tablero[aux].jugador == jug):
                seg = 0
            else:
                if (-9) in tab.tablero[aux].come and mov in tab.tablero[aux].movimientos:
                    print "jaque"
                    return 1
                else:
                    seg = 0
        else:
            seg = 0
    seg = 1
    mov = 1
    #Verifica el jaque desde la diagonal arriba izquierda
    while seg:
        aux = a - 9*mov
        if (aux > 0 and a/8 == aux/8 + mov):
            if (tab.tablero[aux].jugador == "n"):
                mov = mov + 1
            elif (tab.tablero[aux].jugador == jug):
                seg = 0
            else:
                if (9) in tab.tablero[aux].come and mov in tab.tablero[aux].movimientos:
                    print "jaque"
                    return 1
                else:
                    seg = 0
        else:
            seg = 0
    seg = 1
    mov = 1
    #Verifica el jaque desde la diagonal abajo a la izquierda
    while seg:
        aux = a + 7*mov
        if (aux < 64 and a/8 == aux/8 - mov):
            if (tab.tablero[aux].jugador == "n"):
                mov = mov + 1
            elif (tab.tablero[aux].jugador == jug):
                seg = 0
            else:
                if (-7) in tab.tablero[aux].come and mov in tab.tablero[aux].movimientos:
                    print "jaque"
                    return 1
                else:
                    seg = 0
        else:
            seg = 0
    seg = 1
    mov = 1
    #Verifica el jaque desde la diagonal derecha arriba
    while seg:
        aux = a - 7*mov
        if (aux > 0 and a/8 == aux/8 + mov):
            if (tab.tablero[aux].jugador == "n"):
                mov = mov + 1
            elif (tab.tablero[aux].jugador == jug):
                seg = 0
            else:
                if (7) in tab.tablero[aux].come and mov in tab.tablero[aux].movimientos:
                    print "jaque"
                    return 1
                else:
                    seg = 0
        else:
            seg = 0

    #Verifica los jaques para el caballo
    aux = a - 17
    if (aux > 0 and a/8 == aux/8 + 2 and tab.tablero[aux].jugador == tab.strTab[64] and tab.tablero[aux].type().lower() == 'c'):
        print "jaque"
        return 1
    aux = a - 15
    if (aux > 0 and a/8 == aux/8 + 2 and tab.tablero[aux].jugador == tab.strTab[64] and tab.tablero[aux].type().lower() == 'c'):
        print "jaque"
        return 1
    aux = a - 10
    if (aux > 0 and a/8 == aux/8 + 1 and tab.tablero[aux].jugador == tab.strTab[64] and tab.tablero[aux].type().lower() == 'c'):
        print "jaque"
        return 1
    aux = a - 6
    if (aux > 0 and a/8 == aux/8 + 1 and tab.tablero[aux].jugador == tab.strTab[64] and tab.tablero[aux].type().lower() == 'c'):
        print "jaque"
        return 1
    aux = a + 6
    if (aux < 64 and a/8 == aux/8 - 1 and tab.tablero[aux].jugador == tab.strTab[64] and tab.tablero[aux].type().lower() == 'c'):
        print "jaque"
        return 1
    aux = a + 10
    if (aux < 64 and a/8 == aux/8 - 1 and tab.tablero[aux].jugador == tab.strTab[64] and tab.tablero[aux].type().lower() == 'c'):
        print "jaque"
        return 1
    aux = a + 17
    if (aux < 64 and a/8 == aux/8 - 2 and tab.tablero[aux].jugador == tab.strTab[64] and tab.tablero[aux].type().lower() == 'c'):
        print "jaque"
        return 1
    aux = a + 15
    if (aux <64 and a/8 == aux/8 - 2 and tab.tablero[aux].jugador == tab.strTab[64] and tab.tablero[aux].type().lower() == 'c'):
        print "jaque"
        return 1
    return 0



#Funcion que imprime un tablero dado
def imprimirTablero(tab):
    for i in range (8):
        print 8-i,
        for j in range (8):
            aux = tab.tablero[i*8+j]
            print aux.tostring(),
        print
    print ("  a b c d e f g h")
    print ("-----------------")
    print ("-----------------")

#Agrega un tablero al grafo, una lista a sus aristas y lo agrega al diccionaro con su string del tablero y la posicion del grafo
def agregarGrafo(origen, destino, puntaje):
    if (destino.strTab in tabs):
        ax = tabs[destino.strTab]
        out = grafo[ax]
        if (ax not in aristas[tabs[origen.strTab]]):
            aristas[tabs[origen.strTab]].append(tabs[out.strTab])
    else:
        a = len(grafo)
        tabs[destino.strTab] = a
        destino.puntaje = puntaje
        grafo.append(destino)
        aristas[tabs[origen.strTab]].append(a)
        b = []
        aristas.append(b)

#Define la funcion para que juegue el humano
def juegaHM(origen):
    imprimirTablero(origen)
    a = 1
    cadAux = origen.strTab[:64] + '1'
    tbaux = chess.Tablero(cadAux)
    if (jaque(tbaux)):
        print ("Usted esta en jaque")
    while a: 
        x = raw_input('Su jugada a continuacion, use mayusculas: ')
        aux = ord(x[0]) - 65
        auxn = 8 - int(x[1])
        inp = auxn*8 + aux
        aux = ord(x[3]) - 65
        auxn = 8 - int(x[4])
        ops = auxn*8 + aux
        if(origen.tablero[inp].jugador == 0):
            if (origen.tablero[ops].jugador != 0):
                taux = 0
                if (inp < ops):
                    jugada = origen.strTab[:inp] + colorCasilla(inp) + origen.strTab[inp+1:ops] + origen.tablero[inp].type() + origen.strTab[ops+1:64] + '1'
                    taux = chess.Tablero(jugada)
                    score = 0
                    if (origen.tablero[ops].jugador == 1):
                        score = score - origen.tablero[ops].score
                    if (not jaque(taux)):
                        agregarGrafo(origen, taux, score)
                    else:
                        print ("No es posible su jugada, quedaria en jaque")
                        continue
                    
                else:
                    jugada = origen.strTab[:ops] + origen.tablero[inp].type() + origen.strTab[ops+1:inp] + colorCasilla(inp) + origen.strTab[inp+1:64] + '1'
                    taux = chess.Tablero(jugada)
                    taux = chess.Tablero(jugada)
                    score = 0
                    if (origen.tablero[ops].jugador == 1):
                        score = score - origen.tablero[ops].score
                    if (not jaque(taux)):
                        agregarGrafo(origen, taux, score)
                    else:
                        print ("No es posible su jugada, quedaria en jaque")
                        continue
                a = 0
                return taux
            else:
                print ("Error, no es posible moverse a esta posicion")
        else:
            print ("Error, no es posible mover esta ficha")
def posiblesNegra(origen):
    #Funciones que crean las fichas y las agregan a tablero
    cad = origen.strTab
    for i in range (len(cad)-1):
        ficha = origen.tablero[i]
        if (cad[i] != 'b' and cad[i] != 'B' and ficha.color == "Negro"):
            if (ficha.type() != 'C' and ficha.type() != 'P'):
                for j in range (len(ficha.direccion)):
                    for k in range (len(ficha.movimientos)):
                        direc = ficha.direccion[j]
                        movi = ficha.movimientos[k]
                        aux = i+(direc*movi)
                        if ((direc == 8 and aux < 64) or ((direc == 7 or direc == 9) and (aux < 64 and (aux/8 - movi == i/8)))):
                            posicion = origen.tablero[aux]
                            if (posicion.jugador != 1):
                                if (posicion.jugador == 0):
                                    fin = cad[0:i] + colorCasilla(i) + cad[i+1:aux] + ficha.type() + cad[aux+1:64] + '0'
                                    taux = chess.Tablero(fin)
                                    if (jaque(taux) == 1):
                                        agregarGrafo(origen, taux, origen.tablero[aux].score)
                                    break
                                else:
                                    fin = cad[0:i] + colorCasilla(i) + cad[i+1:aux] + ficha.type() + cad[aux+1:64] + '0'
                                    taux = chess.Tablero(fin)
                                    if (jaque(taux) == 1):
                                        agregarGrafo(origen, taux, origen.tablero[aux].score)
                            else:
                                break
                        elif ((direc == -1 and aux/8 == i/8) or (direc == -8 and aux >= 0) or ((direc == -9 or direc == -7) and (aux >=0 and (aux/8 + movi == i/8)))):
                            posicion = origen.tablero[aux]
                            if (posicion.jugador != 1):
                                if (posicion.jugador == 0):
                                    fin = cad[0:aux] + ficha.type() + cad[aux+1:i] + colorCasilla(i) + cad[i+1:64] + '0'
                                    taux = chess.Tablero(fin)
                                    if (jaque(taux) == 1):
                                        agregarGrafo(origen, taux, origen.tablero[aux].score)
                                    break
                                else:
                                    fin = cad[0:aux] + ficha.type() + cad[aux+1:i] + colorCasilla(i) + cad[i+1:64] + '0'
                                    taux = chess.Tablero(fin)
                                    if (jaque(taux) == 1):
                                        agregarGrafo(origen, taux, origen.tablero[aux].score)
                            else:
                                break
                            
            elif (cad[i] == 'P'):
                auxc = i + 7
                if (auxc/8 - 1 == i/8 and origen.tablero[auxc].jugador == 0):
                    fin = cad [0:i] + colorCasilla(i) + cad[i+1:auxc] + ficha.type() + cad[auxc+1:64] + '0'
                    taux = chess.Tablero(fin)
                    if (jaque(taux) == 1):
                        agregarGrafo(origen, taux, origen.tablero[auxc].score)
                auxc = i + 9
                if (auxc/8 - 1 == i/8 and origen.tablero[auxc].jugador == 0):
                    fin = cad [0:i] + colorCasilla(i) + cad[i+1:auxc] + ficha.type() + cad[auxc+1:64] + '0'
                    taux = chess.Tablero(fin)
                    if (jaque(taux) == 1):
                        agregarGrafo(origen, taux, origen.tablero[auxc].score)
                auxc = i + 8
                if (auxc < 56 and origen.tablero[auxc].jugador == "n"):
                    fin = cad [0:i] + colorCasilla(i) + cad[i+1:auxc] + ficha.type() + cad[auxc+1:]
                    taux = chess.Tablero(fin)
                    if (jaque(taux) == 1):
                        agregarGrafo(origen, taux, origen.tablero[auxc].score)
                else:
                    break
                if (auxc > 55 and auxc < 64 and origen.tablero[auxc].jugador == "n"):
                    arr = ['c', 'a', 't', 'r']
                    for j in range(len(arr)):
                        fin = cad [0:i] + colorCasilla(i) + cad[i+1:auxc] + arr[j] + cad[auxc+1:64] + '0'
                        taux = chess.Tablero(fin)
                        if (jaque(taux) == 1):
                            agregarGrafo(origen, taux, taux.tablero[auxc].score)
                auxc = i + 16
                if (i > 7 and i < 16 and origen.tablero[auxc].jugador == "n"):
                    fin = cad [0:i] + colorCasilla(i) + cad[i+1:auxc] + ficha.type() + cad[auxc+1:64] + '0'
                    taux = chess.Tablero(fin)
                    if (not jaque(taux)):
                        agregarGrafo(origen, taux, origen.tablero[auxc].score)
            elif (cad[i] == 'C'):
                    def compar(aux, mi):
                        if (aux/8 - mi == i/8 and aux < 64 and origen.tablero[aux].jugador == "n"):
                            fin = cad [0:i] + colorCasilla(i) + cad[i+1:aux] + ficha.type() + cad[aux+1:64] + '0'
                            taux = chess.Tablero(fin)
                            if (not jaque(taux)):
                                agregarGrafo(origen, taux, origen.tablero[aux].score)
                        if (aux/8 - mi == i/8 and aux < 64 and origen.tablero[aux].jugador == 0):
                            fin = cad [0:i] + colorCasilla(i) + cad[i+1:aux] + ficha.type() + cad[aux+1:64] + '0'
                            taux = chess.Tablero(fin)
                            if (not jaque(taux)):
                                agregarGrafo(origen, taux, origen.tablero[aux].score)
                    def commin(aux, mi):
                        if (aux/8 + mi == i/8 and aux >= 0 and origen.tablero[aux].jugador == "n"):
                            fin = cad [0:aux] + ficha.type() + cad[aux+1:i] + colorCasilla(i) + cad[i+1:64] + '0'
                            taux = chess.Tablero(fin)
                            if (not jaque(taux)):
                                agregarGrafo(origen, taux, origen.tablero[aux].score)
                        if (aux/8 + mi == i/8 and aux >= 0 and origen.tablero[aux].jugador == "0"):
                            fin = cad [0:aux] + ficha.type() + cad[aux+1:i] + colorCasilla(i) + cad[i+1:64] + '0'
                            taux = chess.Tablero(fin)
                            if (not jaque(taux)):
                                agregarGrafo(origen, taux, origen.tablero[aux].score)
                    aux = i + 15
                    compar(aux, 2)
                    aux = i + 17
                    compar(aux,2)
                    aux = i + 10
                    compar(aux,1)
                    aux = i + 6
                    compar(aux,1)
                    aux = i - 10
                    commin(aux, 1)
                    aux = i - 6
                    commin(aux, 1)
                    aux = i - 17
                    commin(aux, 2)
                    aux = i - 15
                    commin(aux, 2)

def main():
    st = "TCARKACTPPPPPPPPbBbBbBbBBbBbBbBbbBbBbBbBBbBbBbBbpppppppptcarkact0"
    #st = "bBbKbAbBBbBbBbBbbPbPbBbBBbtbBbBRbBbBbBbBBbBbBbBbPBbBbPbBBbBbBbBb1"
    #st = "bBbBbBbBBbBbBbBbbBbBbBbBBbBbBbBBbBbBbBbBBbBbBbBbPBbBbPbBBbBbBbBb1"
    #st = "bBbBbBbBBbBbBbBbbBbBbBbBBbBbBbBbbBbBbBbBBbBbBbBbbBbBbBbRBbBbBbBb1"
    #st = "bBbBbBbBBbBbBbBbbBbBbBbBCbBbBbBbbBbBbBbBBbBbBbBbbBbBbBbCBbBbBbBb1"
    #st = "bbBbBbBbBCbBbBbBpppppppppppppppppppppppppppppCCCPPPppppPPPppPPppp0"
    jugar = 1
    m = chess.Tablero(st)
    tabs[st] = 0
    grafo.append(m)
    a = []
    aristas.append(a)
    while jugar:
        m = grafo[0]
        b = 1
        while b:
            actual.append(tabs[m.strTab])
            juego = juegaHM(m)
            posiblesNegra(juego)
            pos = tabs[juego.strTab]
            actual.append(pos)
            posibles = []
            maximo = 0
            if (len(aristas[pos]) == 0):
                print ("Juego terminado")
                b = 0
            for i in range(len(aristas[pos])):
                tabAux = grafo[aristas[pos][i]]
                if (tabAux.puntaje == maximo):
                    posibles.append(tabAux)
                elif (tabAux.puntaje > maximo):
                    posibles = []
                    posibles.append(tabAux)
                    maximo = tabAux.puntaje
            ran = random.randrange(len(posibles))
            m = posibles[ran]
        suma = 0
        for i in range(len(actual)):
            aux = len(actual) - i - 1
            punt = grafo[actual[aux]].puntaje
            suma = suma + punt
            grafo[actual[aux]].puntaje = suma
        rpta = raw_input('Desea un nuevo juego? (Y/N):')
        if rpta == "n" or rpta == "N":
            juegar = 0
main()
