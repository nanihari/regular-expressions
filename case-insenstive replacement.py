#program to do a case-insensitive string replacement.
import re
text="HARI krishna"
recompile=re.compile(re.escape("hari"), re.IGNORECASE)
print(recompile.sub("hi","hari krishna"))

