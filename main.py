import tablero
import fichas

grafo = []
aristas = []
tabs = {}

def imprimirTablero(tablero):
    for i in range (8):
        print i+1,
        for j in range (8):
            aux = tablero.tablero[i*8+j]
            print aux.tostring(),
        print
    print ("  a b c d e f g h")

def main():
    st = "TCARKACTPPPPPPPPbBbBbBbBBbBbBbBbbBbBbBbBBbBbBbBbpppppppptcarkact0"
    m = tablero.Tablero(st)
    tabs[st] = m
    imprimirTablero(m)
main()
