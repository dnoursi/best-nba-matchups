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
tiers = [ [games[t[0]] for t in goodGameis if t[1] == score] for score in tierScores]

# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
from datetime import datetime
def mydate(datestr):
    return datetime.strptime(datestr, "%d/%m/%Y %H:%M" ).strftime("%A, %B %d, %I:%M %p")

def pprint(od):
    return (mydate(od["Date"]) + ": " + od["Away Team"] + " @ " + od["Home Team"])

def pprints(ls, adj, f):
    f.write("These are the " + adj + " matchups of the season:\n")
    for l in ls:
        f.write(pprint(l))
        f.write("\n")
    f.write("\n")

writefile = open("results.md", "w")
writefile.write("```\n")
for n, tier in enumerate(tiers):
    print("There are " + str(len(tier)) + " games in tier" + str(n+1))
    pprints(tier, "tier"+ str(n+1), writefile)
print("Your customized schedule is printed in results.md")
writefile.write("```\n")
writefile.close()
