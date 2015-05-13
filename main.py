import chess
import fichas
import random

grafo = []
aristas = []
tabs = {}

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

def agregarGrafo(origen, destino, puntaje):
    if (destino.strTab in tabs):
        ax = tabs[destino.strTab]
        out = grafo[ax]
        if (ax not in aristas[tabs[origen.strTab]]):
            aristas[tabs[origen.strTab]].append(tabs[out.strTab])
            punt = origen.puntaje + out.puntaje + puntaje
            origen.puntaje = punt
    else:
        origen.puntaje = origen.puntaje + puntaje
        a = len(grafo) - 1
        tabs[destino.strTab] = a
        grafo.append(destino)
        aristas[tabs[origen.strTab]].append(a)
        b = []
        aristas.append(b)

def juegaHM(origen):
    imprimirTablero(origen)
    a = 1
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
                    jugada = origen.strTab[:inp] + colorCasilla(inp) + origen.strTab[inp+1:ops] + origen.tablero[inp].type() + origen.strTab[ops+1:]
                    taux = chess.Tablero(jugada)
                    score = 0
                    if (origen.tablero[ops].jugador == 1):
                        score = score + origen.tablero[ops].score
                    agregarGrafo(origen, taux, score)
                    
                else:
                    jugada = origen.strTab[:ops] + origen.tablero[inp].type() + origen.strTab[ops+1:inp] + colorCasilla(inp) + origen.strTab[inp+1:]
                    taux = chess.Tablero(jugada)
                    taux = chess.Tablero(jugada)
                    score = 0
                    if (origen.tablero[ops].jugador == 1):
                        score = score + origen.tablero[ops].score
                    agregarGrafo(origen, taux, score)
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
                                    fin = cad[0:i] + colorCasilla(i) + cad[i+1:aux] + ficha.type() + cad[aux+1:]
                                    taux = chess.Tablero(fin)
                                    agregarGrafo(origen, taux, origen.tablero[aux].score)
                                    break
                                else:
                                    fin = cad[0:i] + colorCasilla(i) + cad[i+1:aux] + ficha.type() + cad[aux+1:]
                                    taux = chess.Tablero(fin)
                                    agregarGrafo(origen, taux, origen.tablero[aux].score)
                            else:
                                break
                        elif ((direc == -1 and aux/8 == i/8) or (direc == -8 and aux >= 0) or ((direc == -9 or direc == -7) and (aux >=0 and (aux/8 + movi == i/8)))):
                            posicion = origen.tablero[aux]
                            if (posicion.jugador != 1):
                                if (posicion.jugador == 0):
                                    fin = cad[0:aux] + ficha.type() + cad[aux+1:i] + colorCasilla(i) + cad[i+1:]
                                    taux = chess.Tablero(fin)
                                    agregarGrafo(origen, taux, origen.tablero[aux].score)
                                    break
                                else:
                                    fin = cad[0:aux] + ficha.type() + cad[aux+1:i] + colorCasilla(i) + cad[i+1:]
                                    taux = chess.Tablero(fin)
                                    agregarGrafo(origen, taux, origen.tablero[aux].score)
                            else:
                                break
                            
            elif (cad[i] == 'P'):
                auxc = i + 7
                if (auxc/8 + 1 == i/8 and origen.tablero[auxc].jugador == 0):
                    fin = cad [0:i] + colorCasilla(i) + cad[i+1:auxc] + ficha.type() + cad[auxc+1:]
                    taux = chess.Tablero(fin)
                    agregarGrafo(origen, taux, origen.tablero[auxc].score)
                auxc = i + 9
                if (auxc/8 + 1 == i/8 and origen.tablero[auxc].jugador == 0):
                    fin = cad [0:i] + colorCasilla(i) + cad[i+1:auxc] + ficha.type() + cad[auxc+1:]
                    taux = chess.Tablero(fin)
                    agregarGrafo(origen, taux, origen.tablero[auxc].score)
                auxc = i + 16
                if (i > 7 and i < 16 and origen.tablero[auxc].jugador == "n"):
                    fin = cad [0:i] + colorCasilla(i) + cad[i+1:auxc] + ficha.type() + cad[auxc+1:]
                    taux = chess.Tablero(fin)
                    agregarGrafo(origen, taux, origen.tablero[auxc].score)
                auxc = i + 8
                if (auxc < 56 and origen.tablero[auxc].jugador == "n"):
                    fin = cad [0:i] + colorCasilla(i) + cad[i+1:auxc] + ficha.type() + cad[auxc+1:]
                    taux = chess.Tablero(fin)
                    agregarGrafo(origen, taux, origen.tablero[auxc].score)
                if (auxc > 55 and auxc < 64 and origen.tablero[auxc].jugador == "n"):
                    arr = ['c', 'a', 't', 'r']
                    for j in range(len(arr)):
                        fin = cad [0:i] + colorCasilla(i) + cad[i+1:auxc] + arr[j] + cad[auxc+1:]
                        taux = chess.Tablero(fin)
                        agregarGrafo(origen, taux, taux.tablero[auxc].score)
            elif (cad[i] == 'C'):
                    def compar(aux, mi):
                        if (aux/8 - mi == i/8 and aux < 64 and origen.tablero[aux].jugador == "n"):
                            fin = cad [0:i] + colorCasilla(i) + cad[i+1:aux] + ficha.type() + cad[aux+1:]
                            taux = chess.Tablero(fin)
                            agregarGrafo(origen, taux, origen.tablero[aux].score)
                        if (aux/8 - mi == i/8 and aux < 64 and origen.tablero[aux].jugador == 0):
                            fin = cad [0:i] + colorCasilla(i) + cad[i+1:aux] + ficha.type() + cad[aux+1:]
                            taux = chess.Tablero(fin)
                            agregarGrafo(origen, taux, origen.tablero[aux].score)
                    def commin(aux, mi):
                        if (aux/8 + mi == i/8 and aux >= 0 and origen.tablero[aux].jugador == "n"):
                            fin = cad [0:aux] + ficha.type() + cad[aux+1:i] + colorCasilla(i) + cad[i+1:]
                            taux = chess.Tablero(fin)
                            agregarGrafo(origen, taux, origen.tablero[aux].score)
                        if (aux/8 + mi == i/8 and aux >= 0 and origen.tablero[aux].jugador == "0"):
                            fin = cad [0:aux] + ficha.type() + cad[aux+1:i] + colorCasilla(i) + cad[i+1:]
                            taux = chess.Tablero(fin)
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
    m = chess.Tablero(st)
    tabs[st] = 0
    grafo.append(m)
    a = []
    aristas.append(a)
    b = 1
    while b:
        juego = juegaHM(m)
        posiblesNegra(juego)
        pos = tabs[juego.strTab]
        posibles = []
        maximo = 0
        for i in range(len(aristas[pos])):
            tabAux = grafo[aristas[pos][i]]
            if (tabAux.puntaje == maximo):
                posibles.append(tabAux)
            elif (tabAux.puntaje > maximo):
                posibles = []
                posibles.append(tabAux)
        ran = random.randrange(len(posibles))
        m = posibles[ran]
        imprimirTablero(m)
main()
