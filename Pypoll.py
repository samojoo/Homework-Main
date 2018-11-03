import os
import csv



total_votes = 0
candidate_list = []
candidate_name = []

# counter for 4 candidates

candidate_vote = [0, 0, 0, 0]
candidate_vote_percent = [0, 0, 0, 0]
candidate_winner = []

# path to file

csvpath = os.path.join('election_data.csv')
with open(csvpath, 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)

     # count total votes, add names to the candidate_name list, and votes per candidate

    for row in csv_reader:
        total_votes = 1 + total_votes
        candidate_list.append(str(row[2]))
    for row[2] in candidate_list:
        if row[2] not in candidate_name:
            candidate_name.append(row[2])
        if row[2] == candidate_name[0]:
            candidate_vote[0] = 1 + candidate_vote[0]
        elif row[2] == candidate_name[1]:
            candidate_vote[1] = 1 + candidate_vote[1]
        elif row[2] == candidate_name[2]:
            candidate_vote[2] = 1 + candidate_vote[2]
        elif row[2] == candidate_name[3]:
            candidate_vote[3] = 1 + candidate_vote[3]

    # percentage of the total vote for each candidate

    candidate_vote_percent[0] = round(100 * (candidate_vote[0] / total_votes), 4)
    candidate_vote_percent[1] = round(100 * (candidate_vote[1] / total_votes), 4)
    candidate_vote_percent[2] = round(100 * (candidate_vote[2] / total_votes), 4)
    candidate_vote_percent[3] = round(100 * (candidate_vote[3] / total_votes), 4)

    # if statement to determine winner
    if candidate_vote[0] == max(candidate_vote[0], candidate_vote[1], candidate_vote[2], candidate_vote[3]):
       candidate_winner = candidate_name[0]
    elif candidate_vote[1] == max(candidate_vote[0], candidate_vote[1], candidate_vote[2], candidate_vote[3]):
       candidate_winner = candidate_name[1]
    elif candidate_vote[2] == max(candidate_vote[0], candidate_vote[1], candidate_vote[2], candidate_vote[3]):
       candidate_winner = candidate_name[2]
    elif candidate_vote[3] == max(candidate_vote[0], candidate_vote[1], candidate_vote[2], candidate_vote[3]):
       candidate_winner = candidate_name[3]

    # results

    print("Election Results")

    print(f"Total Votes: {total_votes}")
   
    print(f"{candidate_name[0]}: {candidate_vote_percent[0]}% ({candidate_vote[0]})")
    print(f"{candidate_name[1]}: {candidate_vote_percent[1]}% ({candidate_vote[1]})")
    print(f"{candidate_name[2]}: {candidate_vote_percent[2]}% ({candidate_vote[2]})")
    print(f"{candidate_name[3]}: {candidate_vote_percent[3]}% ({candidate_vote[3]})")
 
    print(f"Winner: {candidate_winner}")

