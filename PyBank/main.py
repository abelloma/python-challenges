import os
import csv

revenue = []
month = []
changed = [] 

csvpath = os.path.join('Resources','budget_data.csv')
# csvpath = os.path.join('budget_data.csv')

text_file = open("Output.txt", "w+")

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    #create two lists, one for the revenues and one for the months
    for row in csvreader:
        revenue.append(int(row[1]))
        month.append(row[0])

    #create new list to find the differences between months
    for i in range(1,len(revenue)):
        changed.append(revenue[i] - revenue [i-1])


    #finding the index of the min/max values in changed to find the matching date index in months
    max_change_index = changed.index(max(changed))
    min_change_index = changed.index(min(changed))

print("Financial Analysis")  
print("----------------------------")
print(f"Total months {len(month)}")
print (f"Total: ${sum(revenue)}")
print(f"Average Change: ${round((sum(changed)/len(changed)),2)}")


text_file.write("Financial Analysis \n")
text_file.write("----------------------------\n")
text_file.write(f"Total months {len(month)}\n")
text_file.write(f"Total: ${sum(revenue)}\n")
text_file.write(f"Average Change: ${round((sum(changed)/len(changed)),2)}\n")

#changed has one less row of data due to calculation so need the +1 to get the correct value
print(f"Greatest Increase in Profits: {month[max_change_index+1]} (${max(changed)})")
print(f"Greatest Decrease in Profits: {month[min_change_index+1]} (${min(changed)})")

text_file.write(f"Greatest Increase in Profits: {month[max_change_index+1]} (${max(changed)})\n")
text_file.write(f"Greatest Decrease in Profits: {month[min_change_index+1]} (${min(changed)})")

text_file.close()



