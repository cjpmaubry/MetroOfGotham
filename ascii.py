

def FromNameToAscii(name):
    crypted_name = 0
    offset = 1000
    len_name = len(name)
    position = 0
    for letter in name:
        if position <= len_name:
            crypted_name += ord(name[position]) * pow(offset, len_name - position - 1)
            position += 1
    return crypted_name

def FromAsciiToName(crypted):
    name = ""
    offset = 1000
    index = 0
    if len(str(crypted)) % 3 == 0:
        number_letters = int(len(str(crypted)) / 3)
    else:
        number_letters = int((len(str(crypted)) + 1) / 3)

    for index in range(number_letters):
        print()
        #LOOOOOOOOOOOOOOL
    return name

test = FromNameToAscii("leopold")

print(FromAsciiToName(test))