
#Returns the ascii value of the string "name"
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

#Returns the string of the "crypted" ascii 
def FromAsciiToName(crypted):
    name = ""
    offset = 1000
    index = 0
    #finds the length of the word to recreate
    if len(str(crypted)) % 3 == 0:
        number_letters = int(len(str(crypted)) / 3)
    else:
        number_letters = int((len(str(crypted)) + 1) / 3)

    #adds each letter to the name
    for index in range(number_letters):
        letter = int(crypted / pow(offset, number_letters - index - 1))
        #"substracts" the letter once its ascii value has been stored in "letter"
        crypted -= letter * pow(offset, number_letters - index - 1)
        #adds that letter to the word
        name += chr(letter % pow(offset, number_letters - index))
        index += 1
    return name

test = FromNameToAscii("agathe")

print(FromAsciiToName(test))