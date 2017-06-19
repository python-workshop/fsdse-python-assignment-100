def has_unique_chars(string):
    matches = 0
    if string is not None:
        for char1 in string:
            for char2 in string:
                if char1 == char2:
                    matches +=1
    else:
        return False
    return True if matches == len(string) else False
