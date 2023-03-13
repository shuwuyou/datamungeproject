# Place code below to do the analysis part of the assignment.
#import csv and open file and read file.
import csv

file = open("clean_data.csv", "r")
alldata = csv.reader(file)

#create a list with year number and the year average of that year.
newlist = []
for line in alldata:
    if alldata.line_num > 1:
        sublist = []
        sublist.append(line[0])
        sumforyear = 0
        for value in line[1:13]:
            sumforyear += float(value)
            yearaverage = sumforyear/12
        sublist.append(yearaverage)
        newlist.append(sublist)


#calculate the year average on a ten-year basis. If year frame is less than 10 years, calculate those years' average.
for i in range(0, len(newlist), 10):
    if (len(newlist[i:-1])%10 != 0) and len(newlist) - i < 10:
        total = 0
        for line in newlist[i:(len(newlist))]:
            value = line[1]
            total += value
            ave = format(total/(len(newlist[i:(len(newlist))])), ".2f")
        print(f"The average of values for remaining years {newlist[i][0]} to {newlist[-1][0]} is: {ave}")
    else:
        tenyears = newlist[i:i+10]
        total = 0
        for line in tenyears:
            value = line[1]
            total += value
            ave = format(total/10,".2f")
        print(f"The average of values for the years {newlist[i][0]} to {newlist[i+9][0]} is: {ave}")
    
    

