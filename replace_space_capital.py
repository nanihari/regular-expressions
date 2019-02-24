#program to insert spaces between words starting with capital letters.
import re
def replace_spaceC(text):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", text)
print(replace_spaceC("HariKrishna"))
print(replace_spaceC("AnAimInTheLifeIsTheOnlyFortuneWorthFinding"))

