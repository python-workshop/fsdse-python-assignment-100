def has_unique_chars(sr):

    if sr == None:
        return False
    elif sr == '':
        return True
    elif len(set(sr)) == len(sr):
        return True
    else:
        return False

# has_unique_chars("abcd")
# Output : True

# has_unique_chars('')
#Output : True

# has_unique_chars("ABCbc")
# Output : False
