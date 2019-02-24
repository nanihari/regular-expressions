##program to remove leading zeros from an IP address.
import re
ip ="218.001.08.0196"
string=re.sub('\.[0]*', '.',ip)
print(string)
