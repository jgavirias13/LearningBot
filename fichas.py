class peon(object):
    movimientos = [1]
    direccion = [0]
    come = [1,7]
    color = ""
    def __init__(self, pos, color):
        self.color = color
        if((pos >= 8 and pos <= 15) or (pos >= 48 and pos <= 55)):
            movimientos.append(2)
    def tostring():
        if (self.color == "Blanco"):
            return u'\u2659'
        else:
            return u'\u265F'

class torre(object):
    movimientos = [1,2,3,4,5,6,7,8]
    direccion =[0,2,4,6]
    def tostring():
        if (self.color == "Blanco"):
            return u'\u2656'
        else:
            return u'\u265C'

class caballo(object):
    direccion = [0,2,4,6]
    def tostring():
        if (self.color == "Blanco"):
            return u'\u2658'
        else:
            return u'\u265E'

class alfil(object):
    movimientos = [1,2,3,4,5,6,7,8]
    direccion = [1,3,5,7]
    def tostring():
        if (self.color == "Blanco"):
            return u'\u2657'
        else:
            return u'\u265D'

class rey(object):
    movimientos = [1]
    direccion = [0,1,2,3,4,5,6,7]
    def tostring():
        if (self.color == "Blanco"):
            return u'\u2654'
        else:
            return u'\u265A'

class reina(object):
    movimientos = [1,2,3,4,5,6,7,8]
    direccion = [0,1,2,3,4,5,6,7]
    def tostring():
        if (self.color == "Blanco"):
            return u'\u2655'
        else:
            return u'\u265B'

class casilla(object):
    def tostring():
        if(self.color == "Blanco"):
            return " "
        else:
            return u'\u25A1'
