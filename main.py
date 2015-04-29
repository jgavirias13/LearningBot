import tablero
import fichas

grafo = []
aristas = []

def main():
    m = tablero.Tablero("TCARKACTPPPPPPPPbBbBbBbBBbBbBbBbbBbBbBbBBbBbBbBbpppppppptcarkact")
    for i in range (8):
        print i+1,
        for j in range (8):
            aux = m.tablero[i*8+j]
            print aux.tostring(),
        print
    print ("  a b c d e f g h")
main()
