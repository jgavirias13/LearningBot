# -*- coding: utf-8 -*-

empty_block = " "

class Tablero(object):
    def __init__(self):

        self.board = []
        peones = "P " * 8
        blancos = u'\u2656'
        print blancos
        peones_blancos = peones.strip()
        negros = blancos.lower()
        peones_negros = peones.lower()
        self.board.append(negros.split(" "))
        self.board.append(peones_negros.split(" "))
        for i in range(4):
            self.board.append([empty_block]*8)
        self.board.append(peones_blancos.split(" "))
        self.board.append(blancos.split(" "))

columnas = "a b c d e f g h".split(" ")

class Ver(object):
    def __init__(self):
        pass
    def display(self, board):
        print("%s: %s"%(" ", columnas))
        print ("-"*50)
        for i, row in enumerate(board):
            row_marker = 8-i
            print("%s: %s"%(row_marker, row))

m = Tablero()
v = Ver()
v.display(m.board)
