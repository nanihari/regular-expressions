#program to find all words starting with 'a' or 'e' in a given string.
import re
text="An aim in the life is the only fortune worth finding"
print(re.findall("[af]\w+", text))

