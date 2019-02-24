#to search a literals string in a string and also find the location within the original string where the pattern occurs.
import re
pattern="fortune"
text="An aim in the life is the only fortune worth finding"
match=re.search(pattern,text)
s=match.start()
e=match.end()
print('found "%s" in "%s" from %d to %d ' % \
      (match.re.pattern,match.string, s, e))
