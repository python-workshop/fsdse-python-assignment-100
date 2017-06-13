def has_unique_chars(user_string):
    if user_string == None:
        return False
    elif user_string == '':
        return True
    return len(set(user_string)) == len(user_string)
