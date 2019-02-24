##program that matches a string that has an a followed by two to three 'b'.

import re
def find_23bs(text):
    patterns="ab{2,3}?"
    if re.search(patterns, text):
        return( "match found")
    else:
        return("no match found")
print(find_23bs("hari krishnabb"))
print(find_23bs("abbb"))
print(find_23bs("abb"))
print(find_23bs("ab"))
