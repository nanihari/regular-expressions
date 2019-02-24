##program to check for a number at the end of a string.
import re
def check_number(string):
    search=re.compile(r".*[0-9]$")
    if search.match(string):
        return True
    else:
        return False
print(check_number("haari00"))
print(check_number("hari"))

