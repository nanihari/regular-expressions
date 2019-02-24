##to match a string that contains only upper, lowercase letters, numbers,& underscores.
import re
def match_withAa1_(text):
    patterns= '^[a-zA-Z0-9_]*$'
    if re.search(patterns, text):
        return "found match"
    else:
        return "no match found"
print(match_withAa1_("hari krishnaAAA___"))
print(match_withAa1_("HARI_krishna%^%^"))
print(match_withAa1_("hhaa11HI_"))
print(match_withAa1_("!@#$%^&*()-"))
