##program to split a string with multiple delimiters.
import re
text="An aim in, the\n life is* the only\n fortune worth"" finding"
print(re.split(r";, |, |\*|\n", text))

