def recipe(grams):
    ounces = 28.3495231 * grams

def Temp(F):
    C = (5/9)*(F-32)

def Puzzle(numheads, numlegs):
    i=0
    while(i<numheads):
        j=numheads-i
        if (2*i+4*j==numlegs):
            print("Number of chickens:", i, "Number of rabbits:", j)
        i+=1


        

