import sklearn

f = open("Teams.csv","r")
s = f.read().split("\n")
s.pop(0)
s.pop(-1)
teams = {}
for team in s:
    team = team.split(",")
    teams[team[1]] = team[0]

f = open("RegularSeasonDetailedResults.csv","r")
s = f.read().split("\n")

attr = s.pop(0).split(",")[6:]
s.pop(-1)
#(season, daynum, winner, winnerscore, loser, loserscore, attributes)
SEASON = 0
DAYNUM = 1
WINNER = 2
WINNERSCORE = 3
LOSER = 4
LOSERSCORE = 5
ATTR = 6
LOCATIONS = "HNA"

regseasonmatches = []
for match in s:
    match = match.split(",")
    attrs = {}
    for i in range(len(attr)):
        val = LOCATIONS.index(match[ATTR+i]) if match[ATTR+i] in LOCATIONS else int(match[ATTR+i])
        attrs[attr[i]] = val # these are all integers except for locations, which are H, N, A
    regseasonmatches.append((int(match[SEASON]), int(match[DAYNUM]),
                             match[WINNER], int(match[WINNERSCORE]), # team IDs intentionally left as strings so we 
                             match[LOSER], int(match[LOSERSCORE]),   # don't accidentally use them as continuous variables
                             attrs))
