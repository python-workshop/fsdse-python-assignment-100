
def has_unique_chars(string):
    if string is None:
        return False
    string = string.replace(r' ', '')
    all_chars = list(string)
    unique_chars = set(all_chars)

    return len(all_chars) == len(unique_chars)

def build(n):
    if n < 0 or n > 100:
        return
    factorial = []
    product = 1
    for i in range(1, n+1):
        product = product*i
        factorial.append(product)

    return build
