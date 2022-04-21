spam = ['apples', 'bananas', 'tofu', 'cats']
result = ''

def convert(inputList):
    returnValue = ''
    for i in range(len(inputList)):
        if(inputList[i] == inputList[-1]):
            returnValue += 'and '
        returnValue += inputList[i] + ' '
    return returnValue

result = convert(spam)
print (result)
