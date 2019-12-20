
import csv

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    print(readCSV)
    
    dates =[]
    colors =[]
    
    for row in readCSV:
        date = row[0]
        color = row[3]
        
        dates.append(date)
        colors.append(color)
        
    print(dates)
    print(colors)
    
    try:
        whatColor = input('For which color do you want to know the date? ')
        
        if whatColor in colors:
            colorIndex = colors.index(whatColor.lower())
            colorDate = dates[colorIndex]
            print(colorDate)
        else:
            print('Color not found or is not a color')
        
    except Exception as e:
        print(e)
        
    print('continuing')