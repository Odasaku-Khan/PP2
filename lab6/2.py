import re
q=input()
x=r'[A-Z]'
z=r'[a-z]'
m=len(re.findall(x,q))
n=len(re.findall(z,q))
print(m,"Upper")
print (n,"lower")