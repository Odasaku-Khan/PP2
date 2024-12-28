import re
def replace(text):
    p = r'[ ,.]'
    replaced = re.sub(p, ':', text)
    return replaced
q= input()
w= replace(q)
print(w)
