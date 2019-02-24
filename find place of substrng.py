#program to find the occurrence and position of the substrings within a string.
import re
text="Hari krishna, Mohan krishna, rama krishna, arun"
pattern="krishna"
for m in re.finditer(pattern,text):
    s=m.start()
    e=m.end()
    print("found "%s" from %d:%d" %(text[s:e],s,e))

