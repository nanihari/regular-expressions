##program to abbreviate 'hari krishna' as 'hk.' in a given string.
import re
text="I am hari krishna and I live in hyderabad"
print(re.sub("hari krishna", "hk.", text))##replace hari krishna with hk
print(re.sub("hyderabad$", "hyd.", text))#replace hyderabad with hyd

