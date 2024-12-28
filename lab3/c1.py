class Task1:
    def __init__(self):
        self.string="Its very long to understand"
    def printStrings(self):
        self.string="qwsdfvbnmzxdfgyuio"
        print(self.string.upper())
    def getString(self):
        self.string=input("")
        print(self.string)
t=Task1()
t.getString()
t.printStrings()