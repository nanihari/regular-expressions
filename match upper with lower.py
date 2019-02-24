#to find sequences of one upper case letter followed by lower case letters.
import re
def match_upperwithlower(text):
    patterns='[A-Z]+[a-z]+$'
    if re.search(patterns, text):
        return ("match found")
    else:
        return ("no match found")
print(match_upperwithlower("hariKrishna"))
print(match_upperwithlower("harikrishna"))
print(match_upperwithlower("hariKRISHNA"))


