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

file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:
    election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)
    #3. The % of votes each candidate won
    winning_count = 0
    winning_percentage = 0
    winning_candidate = ""
    for name in candidate_votes:
        votes = candidate_votes[name]
        summary = f"{name}: {float(votes) / float(total_votes) * 100:.1f}% ({votes:,})\n"
        print(summary)
        txt_file.write(summary)
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
    txt_file.write(winning_candidate_summary)