def palinodrome(str):
    x=''.join(reversed(str))
    if x==str:
        print("palindrome")
    else:
        print("No")
