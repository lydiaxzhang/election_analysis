#The data we need to retrieve.
#1. Total number of votes cast
#2. A complete list of candidates who received votes
#3. The total number of votes each candidate received
#4. The percentage of votes each candidate won
#5. The winner of the election based on popular vote

import os
import csv

#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

#Open the election results and read the file
with open(file_to_load) as election_data:

     #Print the file object
     print(election_data)

#Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#Using the with statement open the file as a text file
#with open(file_to_save, "w") as txt_file:

    #Write three counties to the file
    #txt_file.write("Arapahoe")
    #txt_file.write("Denver")
    #txt_file.write("Jefferson")
    #txt_file.write("Arapahoe\nDenver\nJefferson")
    #txt_file.write(f"Counties in the Election\n-----------------------------------------\nArapahoe\nDenver\nJefferson")

#Add dependencies
import os
import csv

#Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#Open the election results and read the file.
with open(file_to_load) as election_data:

     #Read the file object with the reader function
     file_reader = csv.reader(election_data)

     #Print the header row
     headers = next(file_reader)
     print(headers)
