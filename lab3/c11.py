def uniqueitem(list):
    uniquelist=[]
    for i in list:
        if i not in uniquelist:
            uniquelist.append(i)
    return uniquelist
