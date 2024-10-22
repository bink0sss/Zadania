# import const
# print(const.PI)

from const import *
print(GRAVITY)

class Constants:
    PI = 3.14
    GRAVITY = 9.81

print(Constants.GRAVITY)
print(f"Stala grawitacja to {Constants.GRAVITY}")