def commaCode(givenList):
    givenListCopy = []

    for value in givenList:
        if type(value) == str:
            givenListCopy.append(value)

        else:
            givenListCopy.append(str(value))

    outputString = ",".join(givenListCopy[:-1])
    return outputString + " and " + givenListCopy[-1]


givenInput = ["apples", "bananas", "tofu", "cats", 9, ["Yash", "Pandey"]]

print(commaCode(givenInput))
