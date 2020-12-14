def longest_common_substring(s1, s2):

    maxLongest = 0
    offset = 0
    for i in range(0, len(s1)):
        longest = 0
        if ((i == len(s1) - len(s2) - 2)):
            break
        for j in range(0, len(s2)):
            if (i+j < len(s1)):
                if s1[i+j] == s2[j]:
                    longest = longest + 1
                    if (maxLongest < longest):
                        maxLongest = longest
                        offset = i
                else:
                    break
            else:
                break
    return maxLongest, offset


def encode_lzw(text):

    dictionary = dict()

    i = 0
    index = 1
    while i < len(text):
        if text[i] in dictionary:
            i = i + 1
        else:
            dictionary[text[i]] = index
            index = index + 1


    i = 0
    encoded = []
    while i < len(text):
        j = 0
        stringToBeSaved = text[i]

        while stringToBeSaved in dictionary and i+j < len(text):
            indexInDictionary = dictionary[stringToBeSaved]
            length = len(stringToBeSaved)
            if (i+j == len(text) - 1):
                break
            j = j + 1
            stringToBeSaved = stringToBeSaved + text[i+j]
        i = i + length
        encoded.append(indexInDictionary)
        if (stringToBeSaved not in dictionary):
            dictionary[stringToBeSaved] = index
        index = index + 1

    return encoded, dictionary

l = []
def decode_lzw(encoded, dictionary):
    i = 0
    while i < len(encoded):
        l.append (list(dictionary.keys())[list(dictionary.values()).index(encoded[i])])
        i = i+1

print("LZW Compression Algorithm")
print("=================================================================")
h = int(input("Enter 1 if you want to enter input in command window, 2 if you are using some file:"))
if h == 1:
    stringToEncode = input("Enter the string you want to compress:")
elif h == 2:
    file = input("Enter the filename:")
    with open(file, 'r') as f:
        stringToEncode = f.read()
else:
    print("You entered invalid input")
print ("Enetered string is:",stringToEncode)
[encoded, dictionary] = encode_lzw(stringToEncode)
a = [encoded, dictionary]
print(encoded)
print("Compressed file generated as compressed.txt")
output = open("compressed.txt","w+")
output.write(str(a))
print("Encoded string: ", end="")
decode_lzw(encoded, dictionary)
print("Decoded string:", "".join(l))
