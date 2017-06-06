def has_unique_chars(string):
    if string is not None:
        if len(set(list(string))) == len(string):
            return True

    return False
