class Pointclass:
    def __init__(self):
        self.x=int(input())
        self.y=int(input())
    def show(self):
        print("coordinates : ",self.x," ",self.y)
    def move(self):
        c=int(input())
        v=int(input())
        self.x=c
        self.y=v
    def dist(self):
        x2=int(input())
        y2=int(input())
        distance=((self.x-x2)**2+(self.y-y2)**2)**(1/2)
        print(distance)
z=Pointclass()
z.show()
z.move()
z.dist()