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

def posibles(tablero):
    #Funciones que crean las fichas y las agregan a tablero
    def casillaBlanca(i):
        pass
    def casillaNegra(i):
        pass
    def peonBlanco(i):
        pass
    def peonNegro(i):
    def torreBlanca(i):
        pass
    def torreNegra(i):
    def alfilBlanco(i):
        pass
    def alfilNegro(i):
    def caballoBlanco(i):
        pass
    def caballoNegro(i):
    def reinaBlanca(i):
        pass
    def reinaNegra(i):
    def reyBlanco(i):
        pass
    def reyNegro(i):
    def juegaBlanco(i):
        self.turno = 0
    def juegaNegro(i):
        self.turno = 1
    #"Switch case" para los caracteres de cada ficha con su respectivo codigo ASCII
    options = {98: casillaBlanca,   #b
                66: casillaNegra,   #B
                112: peonBlanco,    #p
                80: peonNegro,      #P
                116: torreBlanca,   #t
                84: torreNegra,     #T
                97: alfilBlanco,    #a
                65: alfilNegro,     #A
                99: caballoBlanco,  #c
                67: caballoNegro,   #C
                114: reinaBlanca,   #r
                82: reinaNegra,     #R
                107: reyBlanco,     #k
                75: reyNegro,       #K
                48: juegaBlanco,    #0
                49: juegaNegro,     #1
        }
    cad = tablero.strTab
    a = jaque(tablero)
    if (jaque == 0):
        for i in range(len(cad)):
            aux = ord(cad[i])
            options[aux](i)
    else if(jaque == 1):
        options[cad[75]](i)

def main():
    st = "TCARKACTPPPPPPPPbBbBbBbBBbBbBbBbbBbBbBbBBbBbBbBbpppppppptcarkact0"
    m = tablero.Tablero(st)
    tabs[st] = m
    imprimirTablero(m)
main()
