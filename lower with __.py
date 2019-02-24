#program to find sequences of lowercase letters joined with a underscore.
import re
def lower_with__(text):
    patterns="^[a-z]+_[a-z]+$"
    if re.search(patterns,text):
        return ("found match")
    else:
        return ("no match")
print(lower_with__("aab_hari"))
print(lower_with__("hari_krishna"))
print(lower_with__("harI_kriShna"))
print(lower_with__("HARI_Kri###na"))
