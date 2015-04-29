# -*- coding: utf-8 -*-

empty_block = " "

class Tablero(object):
    tablero = []
    def __init__(self):
        peonB = u'\u2659'
        peonN = u'\u265F'
        torreB = u'\u2656'
        torreN = u'\u265C'
        caballoB = u'\u2658'
        caballoN = u'\u265E'
        alfilB = u'\u2657'
        alfilN = u'\u265D'
        reyB = u'\u2654'
        reyN = u'\u265A'
        reinaB = u'\u2655'
        reinaN = u'\u265B'
        self.tablero.append(torreN)
        self.tablero.append(caballoN)
        self.tablero.append(alfilN)
        self.tablero.append(reinaN)
        self.tablero.append(reyN)
        self.tablero.append(alfilN)
        self.tablero.append(caballoN)
        self.tablero.append(torreN)
        for i in range(8):
            self.tablero.append(peonN)
        for i in range(32):
            self.tablero.append(" ")
        for i in range (8):
            self.tablero.append(peonB)
        self.tablero.append(torreB)
        self.tablero.append(caballoB)
        self.tablero.append(alfilB)
        self.tablero.append(reinaB)
        self.tablero.append(reyB)
        self.tablero.append(alfilB)
        self.tablero.append(caballoB)
        self.tablero.append(torreB)

columnas = "a b c d e f g h".split(" ")


m = Tablero()
for i in range (8):
    for j in range (8):
        print m.tablero[i*8 + j],
    print
