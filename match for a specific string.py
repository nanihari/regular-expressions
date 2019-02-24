#program that matches a string that has an a followed by zero or more b's.
import re
def text_match(text):
    pattern="a*?b" ## ab+ for string that is followed by 1 more b's
    ## ab{3} can be used/abbb can be used to check str. followed by 3 b's
    if re.search(pattern, text):
        return ("match found")
    else:
        return ("no found")
print(text_match("abccc"))
print(text_match("accccb"))
print(text_match("ac"))
