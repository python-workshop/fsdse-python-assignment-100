def has_unique_chars(string):
    unique_chars = {}
    count = 0
    if string == None:
        return False
    else:
        for letter in string:
            if letter in unique_chars.keys():
                unique_chars[letter] += 1
            else:
                unique_chars[letter] = 1
        for key in unique_chars:
            if unique_chars[key] > 1:
                count += 1
        for value in unique_chars.values():
            if value > 1:
                count += 1
            else:
                pass
        if count > 0:
            return False
        else:
            return True
