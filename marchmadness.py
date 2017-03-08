#import sklearn

f = open("Teams.csv","r")
s = f.read().split("\n")
s.pop(0)
s.pop(-1)
teamnames = {}
teams = []
for team in s:
    team = team.split(",")
    teamnames[team[1]] = team[0]
    teams.append(team[0])

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

simpledata = []
learningrate = 0.05
#for testing purposes
for match in regseasonmatches:
    if(match[SEASON] == 2003):
        simpledata.append((match[WINNER], match[WINNERSCORE], match[LOSER], match[LOSERSCORE]))

#attack, defense
teamParameters = {}
for team in teams
    teamParameters[team] = [30,30]

def calcerror(tparams, dat):
    err = 0.0
    for match in dat:
        team1atk = tparams[match[0]][0]
        team1def = tparams[match[0]][1]
        team2atk = tparams[match[2]][0]
        team2def = tparams[match[2]][1]
        exp1score = team1atk - team2def
        exp2score = team2atk - team1def
        err += (exp1score - match[1])**2
        err += (exp2score - match[3])**2
    return err / len(dat)


def calcgradient(tparams, dat):
    gradient = {}
    for team in tparams:
        gradient[team] = [0,0]
    for match in dat:
        pass
        
