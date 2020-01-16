# Import required packages
import csv
import os


#paths for read and write file
csvpath= os.path.join("Resources", "election_data.csv")


# Placeholders for re-formatted contents
voter_id_list = []
County_list= []
candidate_list = []
total_vote_number=0

def unique_data(list_1):
    unique_list = []     
    for x in list_1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    return (unique_list) 


#read file for data
with open(csvpath, newline='') as election:
    reader = csv.reader(election, delimiter=',')

    #there is header, read the head row first
    header = next(election)
    print(f"Header:{header}") 

    for row in reader:
        #total vote count
        total_vote_number=total_vote_number+1

        #append to candidate_list
        candidate_list.append(row[2])

unique_cand=unique_data(candidate_list)

d={}

for cand in unique_cand:
    d["{0}".format(cand)]=[candidate_list.count(cand), candidate_list.count(cand)/total_vote_number*100]
Khan_count = d['Khan'][0]
Correy_count = d['Correy'][0]
Li_count = d['Li'][0]
O_Tooley_count = d["O'Tooley"][0]

max_vote = max(Khan_count, Correy_count, Li_count, O_Tooley_count)

Election_Results = os.path.join("Election Results.txt")
with open(Election_Results, "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("------------------------------------\n")
    txt_file.write("Total Votes: " + str(total_vote_number))
    print("Election Results\n")
    print("------------------------------------\n")
    print("Total Votes: " + str(total_vote_number))
    for k,v in d.items():
        txt_file.write
        print((k + ": " + str(v[1]) + "% (" + str(v[0]) + ")\n"))
        if d[k][0]==max_vote:
            winner = k
    txt_file.write("Winner: " + winner)
    print("Winner: " + winner)
    print("------------------------------------\n")
    txt_file.write("------------------------------------\n")
    # print (k, v)

# print(d)


# output = (
# f"Election Results\n"
# f"-----------------\n"
# f"Total Votes:: {total_vote_number}\n"
# f"Khan: {d['Khan'][1]} ({d['Khan'][0]})\n"
# f"Correy: {d['Correy'][1]} ({d['Correy'][0]})\n"
# f"Li: {d['Li'][1]} ({d['Li'][0]})\n"
# #"{0}: {1} ({2})". format( "O'Tooley", d["O'Tooley"][1], d["O'Tooley"][0] )
# f"OTooley: {d["OTooley"][1]} ({d["OTooley"][0]})\n"
# f"-----------------\n"
# f"Winner:{winner}\n"
# f"-----------------\n"
# )

# # #output path 
# Election_Results = os.path.join("Election Results.txt")
# # # # Print all of the results (to terminal)
# # print(output)

# # # # Save the results to analysis text file
# with open(Election_Results, "w") as txt_file:
#     txt_file.write(output)
