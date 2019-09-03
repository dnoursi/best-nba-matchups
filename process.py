import csv

with open("allgames.csv") as infile:
    reader = csv.DictReader(infile)
    games = [row for row in reader]
matchups = [set([game["Home Team"], game["Away Team"]]) for game in games]

with open("goodteams.csv") as infile:
    reader = csv.reader(infile)
    goodTeams = [tuple(row) for row in reader]
# Useful for subset operations
goodTeamNames = set([t[0] for t in goodTeams])
# Obtains team "score"
teamNameDict = {t[0]:t[1] for t in goodTeams}

goodGameis = []
for i, matchup in enumerate(matchups):
    if matchup.issubset( goodTeamNames):
        goodGameis.append((i, sum(map(lambda y:float(teamNameDict[y]), matchup))))

tierScores = list(set([t[1] for t in goodGameis]))
tierScores.sort(reverse=True)
tiersMap = {score:int(i+1) for i,score in enumerate(tierScores)}
maxStars = len(tiersMap) + 1

# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
from datetime import datetime
def mydate(datestr):
    return datetime.strptime(datestr, "%d/%m/%Y %H:%M" ).strftime("%A, %B %d, %I:%M %p")

def pprint(od, nstars, mstars):
    return (("*"*nstars) + (" "*(mstars-nstars))  + "| " + mydate(od["Date"]) + ": " + od["Away Team"] + " @ " + od["Home Team"])

writefile = open("results.md", "w")
writefile.write("```\n")
for gamei, score in goodGameis:
    nstars = tiersMap[score]
    writefile.write(pprint(games[gamei], tiersMap[score], maxStars))
    writefile.write("\n")
print("Your customized schedule is printed in results.md")
writefile.write("```\n")
writefile.close()


