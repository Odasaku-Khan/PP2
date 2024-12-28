import re
def find(t):
    p = r'[A-Z][a-z]+'
    s = re.findall(p, t)
    return s