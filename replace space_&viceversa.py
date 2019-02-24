##program to replace whitespaces with an underscore and vice versa.

import re
text="an aim in the life is the only fortune worth finding"
text1=text.replace(" ", "_")
text2=text1.replace("_"," ")
print(text1)
print(text2)
