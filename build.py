def  has_unique_chars(string):
    unique = []
    if string == None:
        return False
    else:
        for char in string:
            if char not in unique:
                unique.append(char)
        if len(unique) == len(string):
            return True
        else:
            return False
