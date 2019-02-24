##program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
import re
def allowed_specific_character(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)
print(allowed_specific_character("ABCDEFabcdef123450"))
print(allowed_specific_character(("*&%@#!}{")))
