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
        goodGameis.append((i, sum(map(lambda y:int(teamNameDict[y]), matchup))))

tier1 = [games[t[0]] for t in goodGameis if t[1] == 4]
tier2 = [games[t[0]] for t in goodGameis if t[1] == 3]
tier3 = [games[t[0]] for t in goodGameis if t[1] == 2]

# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
from datetime import datetime
def mydate(datestr):
    return datetime.strptime(datestr, "%d/%m/%Y %H:%M" ).strftime("%A, %B %d, %I:%M %p")

def pprint(od):
    print(mydate(od["Date"]) + ": " + od["Away Team"] + " @ " + od["Home Team"])

def pprints(ls, adj):
    print("These are the " + adj + " matchups of the season:")
    for l in ls:
        pprint(l)
    print("")


pprints(tier1, "tier1")
pprints(tier2, "tier2")
pprints(tier3, "tier3")

