def has_unique_chars(str):
    return False if str is None else \
        True if len(str) == len(set(str)) else False
