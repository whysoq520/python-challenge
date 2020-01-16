import csv
import os

#paths for read and write file
csvpath= os.path.join("Resources", 'budget_data.csv')


# Placeholders for re-formatted contents
total_num_month = 0
total_value = 0
value_list = []
month_change =[]
month_list= []

#read file for data
with open(csvpath, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

  #there is header, read the head row first
    header = next(reader)
    
    print(f"Header:{header}")
    for row in reader:
        month_list.append(row[0])
        total_num_month = total_num_month + 1
        total_value = total_value + int(row[1])
        value_list.append(row[1])
   
    print(total_num_month)
    print(total_value)
    #print(value_list)
    for i in range(1,len(value_list)):
        month_change.append(int(value_list[i])- int(value_list[i-1]))
    #print(month_change) 
    greatest_increase = max (month_change)
    increase_index =month_change.index(greatest_increase)
    greatest_increase_date = month_list[(increase_index+1)]
    print(greatest_increase)
    print(greatest_increase_date)
    greatest_decrease = min(month_change)
    decrease_index = month_change.index(greatest_decrease)
    greatest_decrease_date = month_list[(decrease_index +1)]
    print(greatest_decrease)
    print(greatest_decrease_date)
    average_change = round(sum(month_change)/len(month_change),2)
    print(average_change)
#path to store file
file_to_output = os.path.join("Financial Analysis.txt")

# Generate budget data Analysis Output
output = (
  f"Financial Analysis\n"
  f"-----------------------------------------------------\n"
  f"Total Months: {total_num_month}\n"
  f"Profit_losses Total: ${total_value}\n"
  f"Average Change : ${average_change}\n"
  f"Greatest Increase in Profits:{greatest_increase_date} (${greatest_increase})\n"
  f"Greatest Decrease in Profits:{greatest_decrease_date} (${greatest_decrease})\n")

# Print all of the results (to terminal)
print(output)
# Save the results to analysis text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
 