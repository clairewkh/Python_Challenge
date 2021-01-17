#Importing csv and os
import csv
import os

#Setting path of the csv and reading the csv file
path2 = os.path.join('Resources','election_data.csv')
with open (path2) as data2:
    read2 = csv.reader(data2,delimiter = ",")

#Setting up holders to store values in the loop
    tot_counts = 0
    Khan_counts = 0
    Correy_counts = 0
    Li_counts = 0
    Otooley_counts = 0
    vote_result = []
    win_name = ""
    skip_first = next(data2)    #Skip and store Header

#Writing a loop to get result of the Poll
    for c in read2:
        if c[2] != "Candidate":
            tot_counts = tot_counts + 1
        
        if c[2] == "Khan":
            Khan_counts = Khan_counts + 1
        elif c[2] == "Correy":
            Correy_counts = Correy_counts + 1
        elif c[2] == "Li":
            Li_counts = Li_counts + 1
        else:
            Otooley_counts = Otooley_counts + 1
            
        
#Calculate each candidates percentage
        k_per = (Khan_counts/tot_counts)*100
        c_per = (Correy_counts/tot_counts)*100
        l_per = (Li_counts/tot_counts)*100
        o_per = (Otooley_counts/tot_counts)*100
        
#Storing all the reults into the list         
    vote_result.append(k_per)
    vote_result.append(c_per)
    vote_result.append(l_per)
    vote_result.append(o_per)

#Determining who is the winner of the Election
    winner = max(vote_result)
    if winner == k_per:
        win_name = "Khan"
    elif winner == c_per:
        win_name= "Correy"
    elif winner == l_per:
        win_name = "Li"
    else:
        win_name = "O'tooley"
        
#Printing and formatting all the results
    print("Election Results")
    print("-----------------------")
    print(f'Total Votes: {tot_counts}')
    print("-----------------------")
    print(f'Khan: {format(k_per,".3f")}% ({Khan_counts})')
    print(f'Correy: {format(c_per,".3f")}% ({Correy_counts})')
    print(f'Li: {format(l_per,".3f")}% ({Li_counts})')
    print("O'Tooley: "+ format(o_per,'.3f')  + "%" + " (" + str(Otooley_counts) + ")")
    print("-----------------------")
    print(f'Winner: {win_name}')
    print("-----------------------")
    
#Exporting Results into a new txt file and formatting
pyPoll_result = os.path.join('Analysis','pyPoll Analysis.txt')
with open(pyPoll_result, 'wt') as txt2:
    
    txt2.write("Election Results\n")
    txt2.write("---------------------------\n")
    txt2.write(f'Total Votes: {tot_counts}\n')
    txt2.write("---------------------------\n")
    txt2.write(f'Khan: {format(k_per,".3f")}% ({Khan_counts})\n')
    txt2.write(f'Correy: {format(c_per,".3f")}% ({Correy_counts})\n')
    txt2.write(f'Li: {format(l_per,".3f")}% ({Li_counts})\n')
    txt2.write("O'Tooley: "+ format(o_per,'.3f')  + "%" + " (" + str(Otooley_counts) + ")\n")
    txt2.write("---------------------------\n")
    txt2.write(f'Winner: {win_name}\n')
    txt2.write("---------------------------\n")
    
