
# Write a function that prints the object type of 
#all types of "Null".
# Return 0 if it goes well and 1 in case of error.
# Your function needs to print all types of NULL.

import math
def NULL_not_found(object: any) -> int:
    nan = float("NaN")
    null_types = {
        None: "Nothing",
        math.nan: "Garlic",
        '0': "Zero",
        '': "Empty",
        False: "Fake"
    }

    type_name = null_types.get(object, "Type not found")

    if  type_name != "Type not found":
        print(type_name,":", object, type(object))
    elif type(object) is float:
        print(null_types[math.nan], ":", object, type(object))
    else:
        print(type_name)
        return 1
    return 0