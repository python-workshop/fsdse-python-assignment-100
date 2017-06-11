def has_unique_chars(str):
    flag = False
    strUnique = []
    if str is not None:
        flag = True
        print str
        for i in str:
            if i.lower() in strUnique:
                flag = False
                break
            strUnique.append(i.lower())
        print strUnique
    return flag
#print has_unique_chars('AbkLCsfjXwZmpdFEo')
#print has_unique_chars(None)
