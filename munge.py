# Place code below to do the munging part of this assignment.
file = open("./data/nasa_data.txt", "r")

alldata = file.read() # one big string...
splitdata = alldata.split("\n") # removes the line breaks and makes a list

file.close()

newdata = []
for i in range(0, len(splitdata)):
    if len(splitdata) > 0 and (splitdata[i][0:4] == "Year" or splitdata[i][0:4].isnumeric() == True):
        newdata.append(splitdata[i])
    else:
        continue

#create a list with no year data
noyeardata = []
noyeardata.append(newdata[0])
for i in range(1, len(newdata)):
    if newdata[i] != newdata[0]:
        noyeardata.append(newdata[i])
    else:
        continue

#data without the last year column
noyeardata2 = []
for i in range(0, len(noyeardata)):
    noyearline = noyeardata[i][0:-6]
    noyeardata2.append(noyearline)

#turn it into csv format setp1
result = []
headers = noyeardata2[0].split()
result.append(",".join(headers))
for line in noyeardata2[1:]:
    value = line.split()
    result.append(",".join(value))
#use the calculation process

finaldata = []
finaldata.append(result[0])
for line in result[1:]:
    singlevalue = line.split(",")
    year = singlevalue[0]
    #process the value by equation and process missing data
    processedline = ""
    for element in singlevalue[1:]:
        if "*" in element:
            processvalue = "NaN"
        else:
            processvalue = format(((int(element)/100)*1.8), ".1f")
        processedline += "," + processvalue
    finaldata.append(year + processedline)
    last = "\n".join(finaldata)

#create file
clean_data = open("clean_data.csv", "w")
clean_data.write(last)
clean_data.close()