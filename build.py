def  has_unique_chars(s):
    uniq_lst = set()
    if s == None:
        return False
    for c in s:
        if c in uniq_lst:
            return False
        uniq_lst.add(c)
    return True
