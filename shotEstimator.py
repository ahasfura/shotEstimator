#columns: etype(gives if somethin was a shot), player(which player), result(made or missed), x, y

import csv
import math
import os

ETYPE = 13
PLAYER = 23
RESULT = 27
X_POS = 30 
Y_POS = 31
X_OFFSET = 4
Y_OFFSET = 4

def shotEstimator(player,x,y,numYears):
	made = 0
	total = 0
	yearList = os.listdir("./data/")
	yearList = yearList[0:numYears]
	for year in yearList:
		if 'regular_season' not in year:
			continue
		gameList = os.listdir("./data/" + year)
		for game in gameList:
			if 'csv' not in game:
				continue
			fp = './data/' + year + '/' + game
			with open(fp, 'rb') as csvfile:
				eventreader = csv.reader(csvfile)
				for row in eventreader:
					if ((row[PLAYER]==player)&(row[ETYPE]=='shot')&(row[X_POS]!='')&(row[Y_POS]!='')):
						if (math.fabs(x-int(row[X_POS]))<X_OFFSET)&(math.fabs(y-int(row[Y_POS]))<Y_OFFSET):
							total+=1
							if(row[RESULT]=="made"):
								made+=1
	
	if(total!=0):
		return (float(made)/float(total))	
	else:
		return "no shots taken there"

print shotEstimator("Shaquille O'Neal",25,5,1)
