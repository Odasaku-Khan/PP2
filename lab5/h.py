import re
def split(s):
    return re.findall('[A-Z][^A-Z]*', s)
i= input()
result = split(i)
print( result)
