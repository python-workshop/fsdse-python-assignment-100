def has_unique_chars(inputString):
    count = 0
    if(inputString == None):
        return False
    elif(inputString == ""):
        return True
    else:
        for i in inputString:
            print inputString.count(i)
            if(inputString.count(i) > 1):
                return False
                count += count
                break
        if count == 0:
            return True





has_unique_chars("foo")
