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
            return "B"
        return "b"
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

def posiblesNegra(origen):
    posibles = []
    #Funciones que crean las fichas y las agregan a tablero
    cad = origen.strTab
    for i in range (len(cad)-1):
        ficha = origen.tablero[i]
        if (cad[i] != 'b' and cad[i] != 'B' and ficha.color != "Blanco" and ficha.type() != 'C'):
            for j in range (len(ficha.direccion)):
                for k in range (len(ficha.movimientos)):
                    direc = ficha.direccion[j]
                    movi = ficha.movimientos[k]
                    aux = i+(direc*movi)
                    if (((direc == -1 or direc == 1) and (aux/8 == i/8)) or ((direc == 8) and (aux < 64)) or ((direc == -8) and (aux >= 0)) or ((direc == -9 or direc == -7) and (aux >= 0 and (aux/8 + movi == i/8))) or ((direc == 7 or direc == 9) and (aux < 64 and (aux/8 - movi == i/8)))):
                        posicion = origen.tablero[aux]
                        if (posicion.jugador != 1):
                            if (posicion.jugador == 0):
                                fin = cad[0:i] + colorCasilla(i) + cad[i+1:aux] + ficha.type() + cad[aux+1:]
                                taux = chess.Tablero(fin)
                                posibles.append(taux)
                                imprimirTablero(taux)
                                break
                            else:
                                fin = cad[0:i] + colorCasilla(i) + cad[i+1:aux] + ficha.type() + cad[aux+1:]
                                taux = chess.Tablero(fin)
                                posibles.append(taux)
                        else:
                            break
                        
    return posibles

def main():
    st = "TCARKACTPPBbBbBbbBbBbBbcBbBbBbptbBpBpBbBBaBbBbBbpppppppptcarkact0"
    m = chess.Tablero(st)
    tabs[st] = m
    sol = posiblesNegra(m)
    for i in range (len(sol)):
        imprimirTablero(sol[i])
main()
