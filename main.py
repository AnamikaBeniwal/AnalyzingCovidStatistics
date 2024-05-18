from getData import getAllData
from cleanData import makeDict, prepareDict
from  plot import plotPie


#pass the URL to the function to fetch needed data
tableCases = getAllData("https://data.who.int/dashboards/covid19/cases?n=c")

#pass the table, instant of beautiful soup, to make a dictionary 
dictCasesCountries = makeDict(tableCases)

# prepare data 
cleanDict = prepareDict(dictCasesCountries)

# draw the pie chart by the dictionary 
plotPie(cleanDict)
