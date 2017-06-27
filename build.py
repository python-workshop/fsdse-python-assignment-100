def has_unique_chars(s):
    try :
        if len(set(s)) == len(s):
            return True
        else :
            return False
    except :
        return False



has_unique_chars('AbkLCsfjXwZmpdFEo')
