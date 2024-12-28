import re
def find(text):
    pat = r'[a-z]+_[a-z]+'
    s = re.findall(pat, text)
    return s
q=input()
z=find(q)
for x in z:
    print(x)
