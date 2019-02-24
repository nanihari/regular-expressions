##program to find all words which are at least 4 characters long in a string.
import re
text="An aim in the life is the only fortune worth finding"
print(re.findall(r"\b\w{4,}\b", text))##{3,5} will give us length of 3,4& 5 lettered words
print(re.findall(r"\b\w{5}\b", text))## only 5 letterd word
