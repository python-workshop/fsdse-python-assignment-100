

def has_unique_chars(inString):

    if inString is None:
        return False

    inputSet = set()
    for x in inString:
        if x in inputSet:
            return False
        inputSet.add(x)
    return True

print has_unique_chars('Rishabh')
