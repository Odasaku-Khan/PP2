import re
def match(text):
    p = r'a(bb?){2,3}'
    if re.search(p, text):
        return True
    else:
        return False
test=["ab", "abb", "abbb", "abbbb", "aab", "abab", "abbbbcc"]

for x in test:
    if match(x)==True:
        print("match")
    else:
        print("not")

