def has_unique_chars(string):
    if string is None:
        return False
    elif len(string) == len(set(string)):
        return True
    else:
        return False
