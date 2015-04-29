# -*- coding: utf-8 -*-

import fichas

class Tablero(object):
    tablero = []
    def __init__(self, tab):
        options = {'b': casillaBlanca,
                    'B': casillaNegra,
                    'p': peonBlanco,
                    'P': peonNegro,
                    't': torreBlanca,
                    'T': torreNegra,
                    'a': alfilBlanco,
                    'A': alfilNegro,
                    'c': caballoBlanco,
                    'C': caballoNegro,
                    'r': reinaBlanca,
                    'R': reinaNegra,
                    'k': reyBlanco,
                    'K': reyNegro,
        }
        def casillaBlanca():
            self.tablero.append(casilla("blanco"))
        def casillaNegra():
            self.tablero.append(casilla("negro"))
        def peonBlanco():
            self.tablero.append(peon(i,"blanco"))
        def peonNegro():
            self.tablero.append(peon(i,"negro"))
        def torreBlanca():
            self.tablero.append(torre("blanco"))
        def torreNegra():
            self.tablero.append(torre("negro"))
        def alfilBlanco():
            self.tablero.append(alfil("blanco"))
        def alfilNegro():
            self.tablero.append(alfil("negro"))
        def caballoBlanco():
            self.tablero.append(caballo("blanco"))
        def caballoNegro():
            self.tablero.append(caballo("negro"))
        def reinaBlanca():
            self.tablero.append(reina("blanco"))
        def reinaNegra():
            self.tablero.append(reina("negro"))
        def reyBlanco():
            self.tablero.append(rey("blanco"))
        def reyNegro():
            self.tablero.append(rey("negro"))
        for i in tab:
            options[tab[i]]

m = Tablero("tcarkactppppppppBbBbBbBbbBbBbBbBBbBbBbBbbBbBbBbBPPPPPPPPTCARKACT")
for i in range (8):
    for j in range (8):
        print m.tablero[i*8 + j].tostring,
    print
