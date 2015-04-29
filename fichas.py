class ficha(object):
    color = ""
    def __init__(self,color):
        self.color = color;
    def tostring(self):
        pass

class peon(ficha):
    movimientos = [1]
    direccion = [0]
    come = [1,7]
    def __init__(self, pos, color):
        ficha.__init__(self,color)
        if((pos >= 8 and pos <= 15) or (pos >= 48 and pos <= 55)):
            self.movimientos.append(2)
    def tostring(self):
        if (self.color == "Blanco"):
            return u'\u2659'
        else:
            return u'\u265F'

class torre(ficha):
    movimientos = [1,2,3,4,5,6,7,8]
    direccion =[0,2,4,6]
    def __init__(self,color):
        ficha.__init__(self,color)
    def tostring(self):
        if (self.color == "Blanco"):
            return u'\u2656'
        else:
            return u'\u265C'

class caballo(ficha):
    direccion = [0,2,4,6]
    def __init__(self,color):
        ficha.__init__(self,color)
    def tostring(self):
        if (self.color == "Blanco"):
            return u'\u2658'
        else:
            return u'\u265E'

class alfil(ficha):
    movimientos = [1,2,3,4,5,6,7,8]
    direccion = [1,3,5,7]
    def __init__(self,color):
        ficha.__init__(self,color)
    def tostring(self):
        if (self.color == "Blanco"):
            return u'\u2657'
        else:
            return u'\u265D'

class rey(ficha):
    movimientos = [1]
    direccion = [0,1,2,3,4,5,6,7]
    def __init__(self,color):
        ficha.__init__(self,color)
    def tostring(self):
        if (self.color == "Blanco"):
            return u'\u2654'
        else:
            return u'\u265A'

class reina(ficha):
    movimientos = [1,2,3,4,5,6,7,8]
    direccion = [0,1,2,3,4,5,6,7]
    def __init__(self,color):
        ficha.__init__(self,color)
    def tostring(self):
        if (self.color == "Blanco"):
            return u'\u2655'
        else:
            return u'\u265B'

class casilla(ficha):
    def __init__(self,color):
        ficha.__init__(self,color)
    def tostring(self):
        if(self.color == "Blanco"):
            return " "
        else:
            return u'\u25A1'
