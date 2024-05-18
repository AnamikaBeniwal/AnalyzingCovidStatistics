import matplotlib.pyplot as plt 

def plotPie(myDict):
    """ This function plots the pie chart for the dictionary passed.
    The keys in dictionary act as the labels and the vlues as the size of each division.
    It returns Nothing.
    """
    labels = list(myDict.keys())
    sizes = list(myDict.values())

    plt.figure(figsize=(10, 7))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)

    # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.axis('equal')

    # Add a title
    plt.title('COVID-19 Cases Distribution')

    # Display the pie chart
    plt.show()

    