def convert(number = '10', baseFrom = 10, baseTo = 10):
    try:
        baseTo = int(baseTo);baseFrom = int(baseFrom)
    except Exception:return "invalid base, must be a numerical value"

    correspondenceString = r"""0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz/-"""
    
    if baseTo < 1 or baseFrom < 1:return "base must be greator then 0"
    if baseTo > len(correspondenceString):return "this base is not supported"
    for i in str(number):
        if i not in correspondenceString:return "invalid charater"
        
    numToCharCorrespondence = {i:j for i, j in enumerate(correspondenceString)}
    charToNumCorrespondence = {j:i for i, j in enumerate(correspondenceString)}

    final = ""

    convertedBase10 = 0
    for num, char in enumerate(reversed(str(number))):
        convertedBase10 += int(charToNumCorrespondence[char]) * (baseFrom ** num)

    while convertedBase10 != 0:
        remainder = convertedBase10 % baseTo
        corresponding = numToCharCorrespondence[remainder]
        final += str(corresponding)
        convertedBase10 //= baseTo

    return final[::-1]