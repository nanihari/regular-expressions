#program to split a string at uppercase letters.

import re
text="AnAimInTheLifeIsTheOnlyFortuneWorthFinding"
print(re.findall('[A-Z][^A-Z]*', text))
