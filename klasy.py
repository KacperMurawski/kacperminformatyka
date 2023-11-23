class Point: #klase piszemy zawsze z duzej litery
    def __init__(self, x, y): #od razu uruchamia czynnosc
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")
#print(type(point)) #daje nam klase instancji
#print(isinstance(print, Point)) #sprawdza, czy podana zmienna ma taka klase

point = Point(1, 2)
Point.z = 10
point.draw()

another = Point(3,4)
another.draw()
