# a-z  
# 0-9
# . _ time 1
# @ time 1
# . 2,3 positions

import re
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input('enter your email :')

if re.search(email_condition, user_email):
    print("right email")

else:
    print("wrong email")
