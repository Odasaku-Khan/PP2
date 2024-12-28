class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, lenght):
        super().__init__()
        self.len=lenght
    def area(self):
        return self.len**2
class Rectangle(Shape):
    def __init__(self, len, w):
        super().__init__()
        self.len=len
        self.width=w
    def area(self):
        return self.len* self.width