#matches a string that has an 'a' followed by anything, ending in 'b'.

import re
def match_lowerwith_(text):
    patterns='a*?b$'
    if re.search(patterns, text):
        return ("found match")
    else:
        return ("no match found")
print(match_lowerwith_("abba"))
print(match_lowerwith_("ari_krishnab"))
print(match_lowerwith_("aHARI_krishnab"))
