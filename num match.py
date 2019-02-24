##program where a string will start with a specific number.
import re
def num_match(string):
    text = re.compile(r"^5")
    if text.match(string):
        return True
    else:
        return False
print(num_match("5-123"))
print(num_match("8-908"))


