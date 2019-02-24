##program to remove all whitespaces from a string.
import re
text="hari        krishna"
print(re.sub(r'\s+', "", text))## " " for multiple white spaces  

