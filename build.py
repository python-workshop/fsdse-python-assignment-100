def has_unique_chars(ip):
    if ip == '':
        return True
    if ip == None:
        return False
    seen = set(ip)
    if len(seen) == len(ip):
        return True
    else:
        return False


has_unique_chars('AbkLCsfjXwZmpdFEoOO')
