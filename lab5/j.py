import re
def snake(c):
    s = re.sub(r'(?<!^)(?=[A-Z])', '_', c).lower()
    return s
i = input()
sn =snake(i)
print(sn)
