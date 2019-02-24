##program to search some literals strings in a string.
import re
patterns=["An", "aim", "fortune", "hari"]
text="An aim in the life is the only fortune worth finding"
for pattern in patterns:
        print('Searching for "%s" in "%s" ->' % (pattern, text),)
        if re.search(pattern, text):
            print("match found")
        else:
            print ("no match found")


