def has_unique_chars(strings1):
    if strings1 == None:
        return False
    list1 = sorted(set(strings1), key=strings1.index)
    return strings1 == "".join(str(x) for x in list1) 
