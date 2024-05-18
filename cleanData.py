def makeDict(tableCases):
    """This function transforms the data into a dictionary of Countries as keys and number of cases as values.
    It takes the instance of the beautiful soup as the argument.
    It returns the dictionary.
    """
    nameNode = tableCases.find_all('th')
    numberNode = tableCases.find_all('span')

    countryName = []
    numberCases = []
    for name in nameNode:
        countryName.append(name.text.strip())

    countryName = countryName[2:7]


    print("names of countries :",countryName)

    for numbers in numberNode:
        numberCases.append(numbers.text.strip())

    numberCases = numberCases[1:6]
    print("number of cases", numberCases)

    dict_caseCountries = dict(zip(countryName,numberCases))
    print("dictionary is :",dict_caseCountries)

    return dict_caseCountries


def prepareDict(mainDict):
    """ This function prepares the dictionary by replacing units like 'm' or 'k' by its value,
      so that it is ready to be plotted as a pie chart. 
      And it adds on more item named "others" calculated according to the rest of the values.
      It takes in the Dictionary of country names a key and number of cases as the values. 
      Values are of string type in the passed dictionary, as it has the unit inilials along with the number.
      It returns the dictnary value as integer.
    """

    for key,value in mainDict.items():
        try:
            if 'm' in value:
                mainDict[key] = (int(float(value.replace('m', ''))))*1000000
            
            elif 'k' in value:
                mainDict[key] = (int(float(value.replace('k', ''))))*1000
            else:
                int(value)
        except ValueError:
            print(f"Unable to convert value: {value}")
            
    totalCases = mainDict.pop("World")
    print(type(mainDict.values()))
    sumCasesGiven = sum(mainDict.values())
    othersCases  = totalCases - sumCasesGiven

    mainDict["Others"] = othersCases
    print("dictionary now fully ready : ", mainDict)
    print("sum of all vlues:",sumCasesGiven)
    return mainDict

