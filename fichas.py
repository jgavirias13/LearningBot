class peon(object):
    movimientos = [1]
    direccion = [0]
    come = [1,7]
    color = ""
    def __init__(self, pos, color):
        self.color = color
        if(pos == 1 or pos == 6):
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
        return "Torre"
class caballo(object):
    direccion = [0,2,4,6]
    def tostring():
        return "Caballo"
class alfil(object):
    movimientos = [1,2,3,4,5,6,7,8]
    direccion = [1,3,5,7]
    def tostring():
        return "Alfil"
class rey(object):
    movimientos = [1]
    direccion = [0,1,2,3,4,5,6,7]
    def tostring():
        return "Rey"
class reina(object):
    movimientos = [1,2,3,4,5,6,7,8]
    direccion = [0,1,2,3,4,5,6,7]
    def tostring():
        return "Reina"
