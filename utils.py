def convert_string_to_int(string):
    try:
        str_len = len(string)
        int_ele = None
        if string[0] == '[' and string[str_len - 1] == ']':
            int_ele = eval(string)
        else:
            int_ele = int(string)
    except:
        return None
    return int_ele
