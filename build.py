def has_unique_chars(x):
    if x == None:
        return False
    elif len(x) == len(set(x)):
        return True
    else:
        return False
