##program to convert camel case string to snake case string.
import re
def camel_snake(text):
    str1=re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return str1.lower()
print(camel_snake("HariKrishna"))
