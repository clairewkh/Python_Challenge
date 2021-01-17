#Claire Wong
#Py Me Up, Charlie(Python Challenge)
#1.15.2021

#import and read csv file for budget data
import os
import csv

#Setting up Path
csvpath1 = os.path.join('Resources','budget_data.csv')
with open(csvpath1) as data1:            #Open and read data

    read1 = csv.reader(data1,delimiter = ",")
    
    first_row = next(read1)        #skip and store header
    budget_data = list(read1)
    rows_count = len(budget_data)
    
    #Print text
    print("Financial Analysis")
    print("--------------------")
   
    #The total number of months included in the dataset
    print(f'Total Month: {rows_count}')
    
    #The total amount of "Profit/Losses" over the entire period
    date_col = [d1[0] for d1 in budget_data]
    pro_los_col = [int(d2[1]) for d2 in budget_data]
    sum_pro_los = sum(pro_los_col[0:len(pro_los_col)])
    print(f'Total: ${sum_pro_los}')
    
    #Changes in "Profit/Losses" over the entire period, the find the average of the changes
    #Feb-17(the last month in the data) - Jan-10(the first month in the data) 
    #divided by 85 (86months in total but only 85 changes) and round it to 2 decimals 
    avg_changes = round((pro_los_col[rows_count-1] - pro_los_col[0])/85,2)
    print(f'Average Change: ${avg_changes}')
    
    #The Greatest increase in profits over the entire period
    list2 = []
    count = 0
    for i in pro_los_col:             #last: pro_los_col[85] first: pro_los_col[0]
        if count > 0:
            list2.append(pro_los_col[count]-pro_los_col[count-1])
        count = count + 1
    max_change = max(list2)
    max_index = list2.index(max_change)
    max_date = date_col[max_index+1]
    min_change = min(list2)
    min_index = list2.index(min_change)
    min_date = date_col[min_index+1]
    
    print(f'Greatest Increase in Profits: {max_date} (${max_change})')
    print(f'Greatest Decrease in Losses: {min_date} (${min_change})')
    
#Export Financial Analysis in a text format
pyBank_result = os.path.join('Analysis','pyBank Analysis.txt')
with open(pyBank_result, 'wt') as txt1:
    
    txt1.write("Financial Analysis\n")
    txt1.write("--------------------\n")
    txt1.write(f'Total Month: {rows_count}\n')
    txt1.write(f'Total: ${sum_pro_los}\n')
    txt1.write(f'Average Change: ${avg_changes}\n')
    txt1.write(f'Greatest Increase in Profits: {max_date} (${max_change})\n')
    txt1.write(f'Greatest Decrease in Losses: {min_date} (${min_change})\n')
