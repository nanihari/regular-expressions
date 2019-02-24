#program to remove everything except alphanumeric characters from a string.


import re
text="*** HARI KRISHNA kasavarajula__!@#123***"
recompile=re.compile('[\W_]+')
print(recompile.sub("",text))
