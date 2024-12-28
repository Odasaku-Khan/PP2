from itertools import permutations
def permutation(str):
    n=len(str)
    per=permutations(str,n)
    for p in per:
        print(''.join(p))

str=input()
permutation(str)
