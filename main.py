import chess
import fichas

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
        print i+1,
        for j in range (8):
            aux = tab.tablero[i*8+j]
            print aux.tostring(),
        print
    print ("  a b c d e f g h")
    print ("-----------------")
    print ("-----------------")

def posiblesNegra(origen):
    posibles = []
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
                                    posibles.append(taux)
                                    break
                                else:
                                    print colorCasilla(i)
                                    print i
                                    fin = cad[0:i] + colorCasilla(i) + cad[i+1:aux] + ficha.type() + cad[aux+1:]
                                    taux = chess.Tablero(fin)
                                    posibles.append(taux)
                            else:
                                break
                        elif ((direc == -1 and aux/8 == i/8) or (direc == -8 and aux >= 0) or ((direc == -9 or direc == -7) and (aux >=0 and (aux/8 + movi == i/8)))):
                            posicion = origen.tablero[aux]
                            if (posicion.jugador != 1):
                                if (posicion.jugador == 0):
                                    fin = cad[0:aux] + ficha.type() + cad[aux+1:i] + colorCasilla(i) + cad[i+1:]
                                    taux = chess.Tablero(fin)
                                    posibles.append(taux)
                                    break
                                else:
                                    fin = cad[0:aux] + ficha.type() + cad[aux+1:i] + colorCasilla(i) + cad[i+1:]
                                    taux = chess.Tablero(fin)
                                    posibles.append(taux)
                            else:
                                break
                            
            elif (cad[i] == 'P'):
                auxc = i + 7
                if (auxc/8 + 1 == i/8 and origen.tablero[auxc].jugador == 0):
                    fin = cad [0:i] + colorCasilla(i) + cad[i+1:auxc] + ficha.type() + cad[auxc+1:]
                    taux = chess.Tablero(fin)
                    posibles.append(taux)
                auxc = i + 9
                if (auxc/8 + 1 == i/8 and origen.tablero[auxc].jugador == 0):
                    fin = cad [0:i] + colorCasilla(i) + cad[i+1:auxc] + ficha.type() + cad[auxc+1:]
                    taux = chess.Tablero(fin)
                    posibles.append(taux)
                auxc = i + 16
                if (i > 7 and i < 16 and origen.tablero[auxc].jugador == "n"):
                    fin = cad [0:i] + colorCasilla(i) + cad[i+1:auxc] + ficha.type() + cad[auxc+1:]
                    taux = chess.Tablero(fin)
                    posibles.append(taux)
                auxc = i + 8
                if (auxc < 56 and origen.tablero[auxc].jugador == "n"):
                    fin = cad [0:i] + colorCasilla(i) + cad[i+1:auxc] + ficha.type() + cad[auxc+1:]
                    taux = chess.Tablero(fin)
                    posibles.append(taux)
                if (auxc > 55 and auxc < 65 and origen.tablero[auxc].jugador == "n"):
                    arr = ['c', 'a', 't', 'r']
                    for j in range(len(arr)):
                        fin = cad [0:i] + colorCasilla(i) + cad[i+1:auxc] + arr[j] + cad[auxc+1:]
                        taux = chess.Tablero(fin)
                        posibles.append(taux)
            elif (cad[i] == 'C'):
                    def compar(aux, mi):
                        if (aux/8 - mi == i/8 and aux < 65 and origen.tablero[aux].jugador == "n"):
                            fin = cad [0:i] + colorCasilla(i) + cad[i+1:aux] + ficha.type() + cad[aux+1:]
                            taux = chess.Tablero(fin)
                            posibles.append(taux)
                        if (aux/8 - mi == i/8 and aux < 65 and origen.tablero[aux].jugador == 0):
                            fin = cad [0:i] + colorCasilla(i) + cad[i+1:aux] + ficha.type() + cad[aux+1:]
                            taux = chess.Tablero(fin)
                            posibles.append(taux)
                    def commin(aux, mi):
                        if (aux/8 + mi == i/8 and aux >= 0 and origen.tablero[aux].jugador == "n"):
                            fin = cad [0:aux] + ficha.type() + cad[aux+1:i] + colorCasilla(i) + cad[i+1:]
                            taux = chess.Tablero(fin)
                            posibles.append(taux)
                        if (aux/8 + mi == i/8 and aux >= 0 and origen.tablero[aux].jugador == "0"):
                            fin = cad [0:aux] + ficha.type() + cad[aux+1:i] + colorCasilla(i) + cad[i+1:]
                            taux = chess.Tablero(fin)
                            posibles.append(taux)
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
                    
    return posibles

def main():
    st = "TCARKACTPPPPPPPPbBbBbBbBBbBbBbBbbBbBbBbBBbBbBbBbpppppppptcarkact0"
    #st = "bBbKbAbBBbBbBbBbbPbPbBbBBbtbBbBRbBbBbBbBBbBbBbBbPBbBbPbBBbBbBbBb1"
    #st = "bBbBbBbBBbBbBbBbbBbBbBbBBbBbBbBBbBbBbBbBBbBbBbBbPBbBbPbBBbBbBbBb1"
    #st = "bBbBbBbBBbBbBbBbbBbBbBbBBbBbBbBbbBbBbBbBBbBbBbBbbBbBbBbRBbBbBbBb1"
    #st = "bBbBbBbBBbBbBbBbbBbBbBbBCbBbBbBbbBbBbBbBBbBbBbBbbBbBbBbCBbBbBbBb1"
    m = chess.Tablero(st)
    tabs[st] = m
    sol = posiblesNegra(m)
    imprimirTablero(m)
    for i in range (len(sol)):
        imprimirTablero(sol[i])
main()
