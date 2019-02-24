##program to separate and print the numbers of a given string.
import re
text="hari 10, krishna20, kasa 30, y 40,"
resplit=re.split("\D+", text)
for m in resplit:
    print(m)

