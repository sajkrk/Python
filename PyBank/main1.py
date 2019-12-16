
import os
import csv
numberOfmonths = []
proLoss = []

# importing the os module that helps to create the file path
file = os.path.join("..", "Resources", "budget_data.csv")

# opening the file
with open(file, newline='') as myCsvFile:
    csvReader =  csv.reader(myCsvFile, delimiter=',')
    next(csvReader)
    
# looping through the row to find out the total months and total amount of p/L    
    for row in csvReader: 
        numberOfmonths.append(row[0]) 
        proLoss.append(int(row[1])) 

#changes in revenue
    revChanges = []
    
    for p in range(1,len(proLoss)):
        revChanges.append(int(proLoss[p]- int(proLoss[p-1])))
        
    #calculate the average on revenue changes
    averageRevenue= sum(revChanges)/len(revChanges)
    
    #finding increase in profit
    maxincrease = max(revChanges)
    #finding decrease in losses
    mindecrease= min(revChanges)
print ("Financial Analysis")
print (".........................")
print ("Total number of months "+ str(len(numberOfmonths)))#Q1
print ("Total profit and loss "+ str(sum(proLoss)))#Q2
print ("Average changes "+ str(averageRevenue))#Q3

print ("Greatest Increase in " + (numberOfmonths[revChanges.index(max(revChanges)) +1] + " " + "(" + str(maxincrease) +")"))#Q4
print ("Greatest Decrease in " + (numberOfmonths[revChanges.index(min(revChanges)) +1] + " " + "(" + str(mindecrease)+")")) #Q5



   

