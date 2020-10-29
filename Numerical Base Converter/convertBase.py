correspondenceString = r"""0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz/-"""

def convert(number = '10', baseFrom = 10, baseTo = 10):
    check = checks(number, baseFrom, baseTo)
    if not check.accepted:return check.message
    convertedToBase10 = convertToBase10(number, baseFrom)
    return convertToBase(convertedToBase10, baseTo)


def convertToBase10(number = "10", baseFrom = 10, correspondenceString = correspondenceString):
    baseFrom = int(baseFrom)
    charToNumCorrespondence = {j:i for i, j in enumerate(correspondenceString)}
    convertedBase10 = 0

    for num, char in enumerate(reversed(str(number))):
        convertedBase10 += int(charToNumCorrespondence[char]) * (baseFrom ** num)
    
    return convertedBase10



def convertToBase(number = "10", baseTo = 10, correspondenceString = correspondenceString):
    baseTo = int(baseTo)
    numToCharCorrespondence = {i:j for i, j in enumerate(correspondenceString)}
    convertedNum = ""

    while number != 0:
        remainder = number % baseTo
        corresponding = numToCharCorrespondence[remainder]
        convertedNum += str(corresponding)
        number //= baseTo

    return convertedNum[::-1]


def checks(number, baseFrom, baseTo, correspondenceString = correspondenceString):
    try:
        baseTo = int(baseTo);baseFrom = int(baseFrom)
    except Exception:return checkMessage(False, "invalid base, must be a numerical value")
    
    if baseTo < 1 or baseFrom < 1:return checkMessage(False, "base must be greator then 0")
    if baseTo > len(correspondenceString):return checkMessage(False, "this base is not supported")
    for i in str(number):
        if i not in correspondenceString:return checkMessage(False, "invalid charater")
    
    return checkMessage(True, "All parameters accepted")
    

class checkMessage:
    def __init__(self, accepted, message):
        self.accepted, self.message = accepted, message