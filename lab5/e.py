import re
def matches(s):
    if re.match(r'a.*b$', s):
        print(f"'{s}' matches")
    else:
        print(f"'{s}'not match")
q= input()
matches(q)
