# Colorado Board of Elections Audit

## Overview of Project
The following project will assist Tom, a Colorado Board of Elections employee with completing an audit of the election results for US congressional precinct in Colorado. 

### Purpose
As a part of the audit, the findings below will confirm the following information:
* The total number of votes cast
* The candidates for the election
* The number of votes the candidates received
* The percentage of votes for each candidate
* The voter turnout for each county
* The percentage of votes from each county out of the total
* The county with the highest turnout
* The winner of the election

## Election-Audit Results
### Resources
The basis of this audit used the data file *election_results.csv*. In terms of software, *Python 3.9.1* and *Visual Studio Code 1.52.1* was used.

### Results
The chart below includes information extracted from *election_analysis.txt*, which is the final output of the analysis conducted:
    
    Election Results
    -------------------------
    Total Votes: 369,711
    -------------------------

    County Votes:
    Jefferson: 10.5% (38,855)

    Denver: 82.8% (306,055)

    Arapahoe: 6.7% (24,801)

    -------------------------
    Largest County Turnout: Denver
    -------------------------

    Charles Casper Stockham: 23.0% (85,213)
    Diana DeGette: 73.8% (272,892)
    Raymon Anthony Doane: 3.1% (11,606)
    -------------------------
    Winner: Diana DeGette
    Winning Vote Count: 272,892
    Winning Percentage: 73.8%
    -------------------------

#### Total Votes Cast
* A total of 369,711 votes were cast in this congressional election

#### Breakdown of Votes/ Percentage of Total Votes
The total votes can be broken down by both county and by candidate.
* The breakdown by county:
  * Jefferson County had 38,855 votes or 10.5% of the total vote
  * Denver County had 306,055 votes or 82.8% of the total vote
  * Arapahoe County had 24,801 votes or 6.7% of the total vote
* The breakdown by candidate:
  * Charles Casper Stockham received 85,213 votes or 23.0% of the total vote
  * Diana DeGette received 272,892 votes or 73.8% of the total vote
  * Raymon Anthony Doane received 11,606 votes or 3.1% of the total vote

#### County with the Largest Number of Votes
* Denver County had the largest number of votes

#### Candidate with the Largest Number of Votes (The Winner)
* Diana DeGette received the largest number of votes (272,892) and hence won the election with 73.8% of the total vote.

## Election-Audit Results
The script developed for the US Colorado congressional precinct election audit can be re-purposed with some adjustments/ modifications and applied with other election results. A simple modification would be to change the existing lists and dictionaries so that the variables are representative of the components of another electoral district or system. An important consideration to note is that this particular script determines the winner of an election based on the popular vote and therefore cannot be used to audit information in another region/ country that does not determine electoral results in this manner. The basic structure of the script examines the voter turnout based on counties - if another election is based on candidates within counties (2 levels), the application will be easy to modify.

Another suggested change for the script is based on the presentation of the analysis or end output. At this time, there are two separate *for loops* that determine the results per county and then per candidate. A modification could be done to combine the *for loops* so that the results per candidate can be presented as a subset of each county or vice versa. This would give further depth to the analysis and can help to determine several additional factors:
* For each county, which was the most popular candidate
* For each candidate, which county did they have the most success in

Given some modifications, the script from this project can be applied for analysis in numerous other audits.
