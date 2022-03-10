def mysplit(strng):
    my_list = []
    my_string = ""
    p = 0
    new_string = strng[p:-1]
    for char in strng:

        p = new_string.find(" ")
        my_string = new_string[0:p]
        new_string = new_string[p + 1:-1]

        if my_string == "":
            continue
        else:
            my_list.append(my_string)

    if not strng.endswith(" "):
        q = strng.rfind(" ")
        my_string2 = strng[q + 1:-1]

        my_list.append(my_string2)

    return my_list

