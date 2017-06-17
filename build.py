def has_unique_chars(str):
    if(str==None):
        return False
    if(str==""):
        return True
    char_set={str[0]}
    for i in range(1,len(str)):
        char_set.add(str[i])
    if(len(str)==len(char_set)):
        return True
    else:
        return False
