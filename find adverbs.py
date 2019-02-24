##program to find all adverbs and their positions in a given sentence.
import re
text="James coughed loudly to attract her attention."
for m in re.finditer(r"\w+ly", text):
    print(' found "%s" from %d to %d ' % (m.group(0), m.start(), m.end()))

