str1 = "NIKKH:@!"

def has_unique_chars(string):
    cnt = 0
    if string is not None:
        for i in string:
            for j in string:
                if i == j:
                    cnt+=1
        return True if cnt == len(string) else False
    else:
        return False

print(has_unique_chars(str1))
