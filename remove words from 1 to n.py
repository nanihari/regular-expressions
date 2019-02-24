##program to remove words from a string of length between 1 and a given number.

import re
text="An aim in the life is the only fortune worth finding"
word=re.compile(r"\W*\b\w{1,3}\b")
print(word.sub("",text))
