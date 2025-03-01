'''condition'''
# 1. a-z in lowercase
# 2. digit-0-9
# 3. @-1

import re 
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("Enter the Email:")

if re.search(email_condition,user_email):
     print(" Right Email ")
else:
     print(" Wrong Email ")