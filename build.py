def has_unique_chars(string):
    if string is None:
        return False
    elif len(string) < 1:
        return True
    else:
        chars = set()
        for char in string:
            chars.add(char)

        if len(string) == len(chars):
            return True
        else:
            return False
