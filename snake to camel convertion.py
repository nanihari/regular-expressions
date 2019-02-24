##program to convert snake case string to camel case string.

import re
def snake_camel(text):
    return ''.join(x.capitalize() or '_' for x in text.split('_'))
print(snake_camel("harikrishna"))
print(snake_camel("hari__KRISHNA"))
print(snake_camel("HARI_krishna!!!@###"))
