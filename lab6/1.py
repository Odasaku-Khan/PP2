import math
q=input().split()
for z in range(len(q)):
    q[z]=int(q[z])
x=math.prod(q)
print(x)