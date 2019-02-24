#program that matches a word at the beginning of a string.
import re
def match_strbegin(text):
    patterns='^\w+'
    if re.search(patterns, text):
        return ("match found")
    else:
        return ("no match found")
print(match_strbegin("  hari krishna"))
print(match_strbegin("hari krishna"))


