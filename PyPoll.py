#The data we need to retrieve
import csv
import os
file_to_load = os.path.join("data", "election_results.csv")
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
    for row in file_reader:
        print(row)

#1. The total # of votes cast

#2. A complete list of candidates who received votes

#3. The % of votes each candidate won

#4. Tge ttal # of votes each candidate won

#5. The winner of the election based on popular vote