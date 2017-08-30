def has_unique_chars(str):
    if str == None:
        return False
    l1 = len(str)
    s = set(str)
    l2 = len(s)
    if l1 == l2:
        return True
    else:
        return False


a = None
print has_unique_chars(a)
