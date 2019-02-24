##program to check a decimal with a precision of 2.
import re
def decimal_2places(nums):
    num=re.compile(r'^[0-9]+(\.[0-9]{1,2})?$')
    result = num.search(nums)
    return bool(result)
print(decimal_2places("123.19"))
print(decimal_2places("123"))
print(decimal_2places("123.1234"))

