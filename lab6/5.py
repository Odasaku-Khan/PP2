def checking(z):
    for i in range(len(z)):
        if z[i] == True:
            return True
    return False
q = tuple(input())
result = checking(q)
print(result)
