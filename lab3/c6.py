def is_prime(n):
    if n < 2:
        return False
    elif n == 3 or n==2:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def filter(numb):
    num= input().split()
    num=list(map(int, num))
    prime=filter(numb)
    return prime