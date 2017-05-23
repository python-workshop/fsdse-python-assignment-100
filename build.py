def has_unique_chars(string):
    if string is None:
        return False
    chars_set = set()
    for char in string:
        if char in chars_set:
            return False
        else:
            chars_set.add(char)
    return True