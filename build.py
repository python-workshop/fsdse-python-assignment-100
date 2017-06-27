def has_unique_chars(s):
    if s is not None:
        print s
        print set(s)
        if len(set(s)) == len(s):
            return True
        else :
            return False
    else :
        return False

has_unique_chars('AbkLCsfjXwZmpdFEo')
