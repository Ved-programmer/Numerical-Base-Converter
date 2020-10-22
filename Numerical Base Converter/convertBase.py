def convert(number = 10, baseTo = 10, baseFrom = 10):
    baseTo = int(baseTo)
    baseFrom = int(baseFrom)
    correspondenceString = r"""0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz/-"""
    if baseTo > len(correspondenceString):return "this base is not supported"
    for i in str(number):
        if i not in correspondenceString:return "invalid charater"
        

    convertedBase10 = 0
    for num, char in enumerate(reversed(str(number))):
        convertedBase10 += int(char) * baseFrom ** num
        
    correspondence = {i:j for i, j in enumerate(correspondenceString)}
    final = ""

    while convertedBase10 != 0:
        remainder = convertedBase10 % baseTo
        corresponding = correspondence[remainder]
        final += str(corresponding)
        convertedBase10 //= baseTo

    return final[::-1]



  


