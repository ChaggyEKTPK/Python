"""
Polygon Area Calculator - FreeCodeCamp
======================================
Clases Rectangle y Square con métodos de área, perímetro,
diagonal, dibujo ASCII y cálculo de figuras contenidas.
Mejoras respecto a la versión original:
  - Atributos en inglés (width/height), coherentes con FCC.
  - Validación acepta int y float (no solo int).
  - set_* devuelven self.width/self.height de forma consistente.
"""

import math


class Rectangle:
    def __init__(self, width, height):
        self.set_width(width)
        self.set_height(height)

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        if not isinstance(width, (int, float)) or width <= 0:
            raise ValueError('width must be a positive number')
        self.width = width
        return self.width

    def set_height(self, height):
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError('height must be a positive number')
        self.height = height
        return self.height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return math.sqrt(self.width ** 2 + self.height ** 2)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        return ('*' * self.width + '\n') * self.height

    def get_amount_inside(self, shape):
        return (self.height // shape.height) * (self.width // shape.width)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, side):
        if not isinstance(side, (int, float)) or side <= 0:
            raise ValueError('side must be a positive number')
        self.width = side
        self.height = side
        return self.width

    def set_width(self, width):
        return self.set_side(width)

    def set_height(self, height):
        return self.set_side(height)


if __name__ == '__main__':
    rect = Rectangle(10, 5)
    print(rect.get_area())        # 50
    rect.set_height(3)
    print(rect.get_perimeter())   # 26
    print(rect)                   # Rectangle(width=10, height=3)
    print(rect.get_picture())     # 3 filas de 10 '*'

    sq = Square(9)
    print(sq.get_area())          # 81
    sq.set_side(4)
    print(sq.get_diagonal())      # ~5.66
    print(sq)                     # Square(side=4)

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))  # 8
