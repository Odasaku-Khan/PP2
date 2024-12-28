import re
q = input()
s = q.split()
search=[]
for i in s:
    match=re.findall(r"ab*\B", i)  
    search.extend(match)
print(search)
