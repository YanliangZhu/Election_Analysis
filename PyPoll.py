import csv
import os
file_to_load = os.path.join("data", "election_results.csv")

#1. The total # of votes cast
total_votes = 0
#2. A complete list of candidates who received votes
candidate_options = []

#candidate vote
candidate_votes = {}

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader:
        #1
        total_votes += 1
        #2
        name = row[2]
        if name not in candidate_options:
            candidate_options.append(row[2])
            candidate_votes[name] = 0
        candidate_votes[name] += 1

#print(total_votes)
#print(candidate_options)
#print(candidate_votes)

#3. The % of votes each candidate won
winning_count = 0
winning_percentage = 0
winning_candidate = ""
for name in candidate_votes:
    votes = candidate_votes[name]
    print(f"{name}: {float(votes) / float(total_votes) * 100:.1f}% ({votes:,})\n")
    if (votes > winning_count) and ((float(votes) / float(total_votes) * 100) > winning_percentage):
        winning_count = votes
        winning_percentage = float(votes) / float(total_votes) * 100
        winning_candidate = name
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)