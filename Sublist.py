SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    elif is_sublist(list_one, list_two):
        return SUBLIST
    elif is_sublist(list_two, list_one):
        return SUPERLIST
    else:
        return UNEQUAL

def is_sublist(list_one, list_two):
    len_one = len(list_one)
    len_two = len(list_two)

    for i in range(len_two - len_one + 1):
        if list_two[i:i + len_one] == list_one:
            return True

    return False
