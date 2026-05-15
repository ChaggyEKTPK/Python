import math

class Rectangle:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def __str__(self):
        return f'Rectangle(width={self.ancho}, height={self.alto})'


    def set_width(self, ancho):
        if not isinstance(ancho, int):
            raise ValueError('ancho debe ser un numero entero')
        else:
            self.ancho = ancho
        return self.ancho

    def set_height(self, alto):
        if not isinstance(alto, int):
            raise ValueError('alto debe ser un numero entero')
        else:
            self.alto = alto
        return self.alto

    def get_area(self):
        area = self.alto * self.ancho
        return area

    def get_perimeter(self):
        perimetro = 2 * (self.ancho + self.alto)
        return perimetro

    def get_diagonal(self):
        diagonal = math.sqrt((self.ancho ** 2) + (self.alto ** 2))
        return diagonal

    def get_picture(self):
        if self.ancho > 50 or self.alto > 50:
            return 'Too big for picture.'
        cadena = '*'
        ancho_cadena = cadena * self.ancho
        alto_cadena = (ancho_cadena + '\n') * self.alto
        return alto_cadena
    
    def get_amount_inside(self, figura):
        alto = self.alto // figura.alto
        ancho = self.ancho // figura.ancho
        return alto * ancho

class Square(Rectangle):

    def __init__(self, lado):
        super().__init__(lado, lado)
        self.ancho = lado
        self.alto = lado

    def __str__(self):
        return f'Square(side={self.ancho})'

    def set_width(self, lado):
        if not isinstance(lado, int):
            raise ValueError('lado debe ser un numero entero')
        else:
            self.ancho = lado
            self.alto = lado
        return self.ancho

    def set_height(self, lado):
        if not isinstance(lado, int):
            raise ValueError('lado debe ser un numero entero')
        else:
            self.alto = lado
            self.ancho = lado
        return self.alto
    
    def set_side(self, lado):
        if not isinstance(lado, int):
            raise ValueError('lado debe ser un numero entero')
        else:
            self.alto = lado
            self.ancho = lado
        return lado

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))