def has_unique_chars(user_string):
    if user_string == None:
        return False
    elif user_string == '':
        return True
    elif len(set(user_string)) == len(user_string):
            return True
    else:
        return False
