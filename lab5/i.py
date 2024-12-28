import re

def insert(s):
    w= re.findall('[A-Z][a-z]*', s)
    for x in w:
        s = s.replace(x, ' ' + x)
    return s.strip()

i = input()
result = insert(i)
print(result)
