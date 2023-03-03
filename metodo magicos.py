class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x and self.y != other.y

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return (self.x, self.y)

    def __sub__(self, other):
        return (self.x - other.x, self.y - other.y)


    def __mul__(self, other):
        self.x *= other.x
        self.y *= other.y
        return (self.x, self.y)

    def __truediv__(self, other):
        return (self.x / other.x, self.y / other.y)

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}: O valor de x é:{self.x} e o valor de y é:{self.y}"



if __name__=="__main__":
    coordenada1 = Coordenada(10, 15)
    coordenada2 = Coordenada(5, 5)

    print(coordenada1 < coordenada2)
    print(coordenada1 <= coordenada2)
    print(coordenada1 > coordenada2)
    print(coordenada1 >= coordenada2)
    print(coordenada1 == coordenada2)
    print(coordenada1 != coordenada2)
    print(coordenada1 + coordenada2)
    print(coordenada1 - coordenada2)
    print(coordenada1 * coordenada2)
    print(coordenada1 / coordenada2)
    print(coordenada1)
    print(coordenada2)
