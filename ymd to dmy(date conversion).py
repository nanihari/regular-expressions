#program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
import re
def change_date_format(dt):
    return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
dt1 = "2019-02-21"
print("New date in DD-MM-YYYY Format: ",change_date_format(dt1))

