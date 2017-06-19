"""
Implement an algorithm to determine if a string has all unique characters.
Constraints
Can we assume the string is ASCII?
Yes
Note: Unicode strings could require special handling depending on your language
Can we assume this is case sensitive?
Yes
Can we use additional data structures?
Yes
Can we assume this fits in memory?
Yes
Instructions:

Program should be written in file build.py

Function name should be has_unique_chars.
Input
 Type:  String
 Value: 'AbkLCsfjXwZmpdFEo'
Expected Output
  Type:  Boolean
  Value: False.
"""
def has_unique_chars(s1):
    if s1 == None:
        return False
    l2 = sorted(set(s1), key=s1.index)
    return s1 == "".join(str(x) for x in l2)
    #return s1 == "".join((str(s) for s in set(s1)))

#print (has_unique_chars("ABCDA"))
