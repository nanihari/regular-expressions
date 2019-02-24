##program to replace maximum 2 occurrences of space, comma, or dot with a colon.
import re
text="An aim in the life is the only fortune worth finding"
print(re.sub(r"[ ,.]", ":", text, 2))

