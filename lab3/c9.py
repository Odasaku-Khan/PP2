def has33(num):
    for i in range(len(num)-1):
        if num[i]==3 and num[i+1]==3:
            return True
        return False

def spygame(nums):
    found_0 = False
    found_00 = False

    for i in nums:
        if i == 0:
            if found_0:
                found_00 = True
            else:
                found_0 = True
        elif i == 7:
            if found_00:
                return True
    return False        