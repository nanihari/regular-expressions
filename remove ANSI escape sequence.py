##program to remove the ANSI escape sequences from a string.
import re
text="\t\u001b[0;35mgoogle.com\u001b[0m \u001b[0;36m216.58.218.206\u001b[0m"
pattern=re.sub(r'\x1b[^m]*m',"",text)
print(pattern)

