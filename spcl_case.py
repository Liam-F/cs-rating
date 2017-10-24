import pandas as pd

def fix_teams(h_teams):
	h_teams.loc[7723, 'Name'] = 'Morior Invictus'
	h_teams.loc[8241, 'Name'] = 'ex-Nitrious'
	h_teams.loc[8349, 'Name'] = 'Good People'
	h_teams.loc[8008, 'Name'] = 'Grayhound'
	h_teams.loc[5293, 'Name'] = 'AVANT'
	return h_teams