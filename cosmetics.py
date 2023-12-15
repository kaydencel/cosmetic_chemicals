"""
    Andrea Keiper and Kaydence Lin
    DS2000
    Spring 2023
    Final Project Code: Chemicals in Cosmetics
    
    
    Visualizations:
        - Bar chart: Top brands vs # of products on the list
        - Bar chart: Category vs number of products on the list
        - Pie chart: Chemicals used most frequently in cosmetics
"""

COSMETICS = 'cosmetics.csv'
COLORS = ('red', 'orange', 'green', 'blue', 'purple')
import csv
from collections import Counter
import matplotlib.pyplot as plt

COL_BRANDS = 6
COL_CAT = 8
COL_CHEMS = 14
TOP = 5

def read_file(filename):
    data = []
    with open(filename, "r") as infile:
        reader = csv.reader(infile, delimiter = ",")
        next(reader)
        for row in reader:
            data.append(row)
    return data

def get_stats(data, column, top):
    '''Function #1: get_stats
       Parameters: data - read from file, column - position in the file,
                   top - top number of categories
       Returns: top statistics of a category, it's name and counts
       Does: count the amount in each category in a column, get the top number 
             of counts
    '''
    lst = []
    dct = {}
    name = []
    amount = []

    for row in data:
        lst.append(row[column].lower().strip().split(",")[0].split("(")[0])      
    dct = Counter(lst)
    
    for category, count in dct.most_common(top):
        name.append(category)
        amount.append(count)
    return name, amount
    
def bar_chart(name, amount):
    '''Function #2: bar_chart
       Parameters: name - 2D list, amount - 2D list
       Returns: a bar chart
       Does: plots a bar chart using the name, amount, and color
    '''
    plt.bar(name, amount, color = COLORS)
    
def pie_chart(name, amount):
    '''Function #3: pie_chart
       Parameters: name - 2D list, amount - 2D list
       Returns: a pie chart
       Does: plots a pie chart using the name, amount
    '''  
    plt.pie(amount, autopct = "%.1f")
    plt.legend(labels = name, bbox_to_anchor = (.5, -.3), loc = "lower center")
    
def main():
    
    data = read_file(COSMETICS)
    
    # GRAPH 1: Bar Chart: Top brands vs # of products on the list
    graph1 = get_stats(data, COL_BRANDS, TOP)
    bar_chart(graph1[0], graph1[1])
    plt.title("Number of Products per top 5 Brands")
    plt.xlabel("Brand Name")
    plt.xticks(rotation = 60)
    plt.ylabel("Number of Products")
    plt.show()
    
    # GRAPH 2: Bar chart: Category vs number of products on the list
    graph2 = get_stats(data, COL_CAT, TOP)
    bar_chart(graph2[0], graph2[1])
    plt.title("Number of Items per top 5 Cosmetic Categories")
    plt.xticks(rotation = 60)
    plt.xlabel("Category of Product")
    plt.ylabel("Number of Items")        
    plt.show()
    
    # GRAPH 3: Pie chart: Chemicals used most frequently in cosmetics
    graph3 = get_stats(data, COL_CHEMS, TOP)
    pie_chart(graph3[0], graph3[1])
    plt.title("Most Common Chemicals Used in Cosmetics")
    plt.show()
    
main()
        
    


