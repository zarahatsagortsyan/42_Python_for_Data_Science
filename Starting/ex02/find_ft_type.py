#Write a function that prints the object types and returns 42.

def all_thing_is_obj(object: any) -> int:
    type_names = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: "String"
    }

    object_type = type(object)
    type_name = type_names.get(object_type, "Type not found")

    # print("dfgdfg " + type_name)
    if type_name == "String":
        print(object, "is in the kitchen :", object_type)
    elif type_name != "Type not found":
        print(type_name,":", object_type)
    else:
        print(type_name)
    return 42