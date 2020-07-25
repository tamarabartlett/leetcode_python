
def invert_string(string_to_invert):
    str_len = len(string_to_invert)
    half_len = int(str_len/2)
    for i in range(half_len):
        last = string_to_invert[str_len-(i+1)]
        string_to_invert[str_len-(i+1)] = string_to_invert[i]
        string_to_invert[i] = last
        print(string_to_invert)
    return string_to_invert
