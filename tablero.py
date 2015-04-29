# -*- coding: utf-8 -*-

import fichas

class Tablero(object):
    tablero = []
    def __init__(self, tab):
        for i in tab:
            switch(tab[i])
                case '-1':   #Casilla blanca
                    self.tablero.append(casilla("blanco"))
                case '0':   #Casilla negra
                    self.tablero.append(casilla("negro"))
                case '1':   #Peon blanco
                    self.tablero.append(peon(i,"blanco")
                case '2':   #Torre blanca
                    self.tablero.append(torre("blanco"))
                case '3':   #Alfil blanco
                    self.tablero.append(alfil("blanco"))
                case '4':   #Caballo blanco
                    self.tablero.append(caballo("blanco"))
                case '5':   #Reina blanca
                    self.tablero.append(reina("blanco"))
                case '6':   #Rey blanco
                    self.tablero.append(rey("blanco"))
                case '7':   #Peon negro
                    self.tablero.append(peon(i,"negro"))
                case '8':   #Torre negra
                    self.tablero.append(torre("negro"))
                case '9':   #Alfil negro
                    self.tablero.append(alfil("negro"))
                case '10':   #Caballo negro
                    self.tablero.append(caballo("negro"))
                case '11':  #Reina negra
                    self.tablero.append(reina("negro"))
                case '12':
                    self.tablero.append(rey("negro"))

m = Tablero()
for i in range (8):
    for j in range (8):
        print m.tablero[i*8 + j].tostring,
    print
