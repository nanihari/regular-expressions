#program to separate and print the numbers and their position of a given string.
import re
text="It may be shown by a mark (33) on the 26th digit of Sharpe's Egyptian cubit"
for m in re.finditer("\d+", text):
    print(m.group(0))
    print("Index position", m.start())
