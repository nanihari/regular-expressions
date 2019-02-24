##program to extract values between quotation marks of a string.
import re
text='"hari", "krishna", "kasavarajula"'
print(re.findall(r'"(.*?)"', text))

