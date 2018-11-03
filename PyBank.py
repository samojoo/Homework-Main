import os
import csv


month_count = 0
date_list = []
profit_list = []
total_profit = float(0)
change_value_list = []
prior_value = float(0)

# path to file

csvpath = os.path.join('budget_data.csv')


with open(csvpath, 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)

# count months and add to list of dates and profit/loss values

    for value in csv_reader:
        month_count = 1 + month_count
        date_list.append(str(value[0]))
        profit_list.append(float(value[1]))

    # profit/loss changes month-to-month

        current_value = value[1]
        change_value = float(current_value) - float(prior_value)
        change_value_list.append(change_value)
        prior_value = current_value
        

# average change in profit/loss between months

def average(change_value_list):
    x = len(change_value_list)
    total = sum(change_value_list) - change_value_list[0]
    avg = total / (x - 1)
    return avg


average_change = round(average(change_value_list), 2)
total_profit = round(sum(profit_list))
highest_profit = round(max(profit_list))
lowest_profit = round(min(profit_list))
highest_index = profit_list.index(highest_profit)
lowest_index = profit_list.index(lowest_profit)


# results 

print("Financial Analysis")
print(f"Total Months: {month_count}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {date_list[highest_index]} ({highest_profit})")
print(f"Greatest Decrease in Profits: {date_list[lowest_index]} ({lowest_profit})")
