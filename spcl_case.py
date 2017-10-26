import pandas as pd
import pymc3 as pm

def fix_teams(h_teams):
	h_teams.loc[7723, 'Name'] = 'Morior Invictus'
	h_teams.loc[8241, 'Name'] = 'ex-Nitrious'
	h_teams.loc[8349, 'Name'] = 'Good People'
	h_teams.loc[8008, 'Name'] = 'Grayhound'
	h_teams.loc[5293, 'Name'] = 'AVANT'
	h_teams.loc[8030, 'Name'] = 'Not Academy'
	return h_teams
	
def prep_pymc_model(n_teams, n_maps):
	with pm.Model() as rating_model:
		omega = pm.HalfCauchy('omega', 0.5)
		tau = pm.HalfCauchy('tau', 0.5)
		rating = pm.Normal('rating', 0, 1, shape=n_teams)
		theta_tilde = pm.Normal('rate_t', mu=0, sd=1, shape=(n_maps, n_teams))
		rating_map = pm.Deterministic('rating | map', rating + tau * theta_tilde)
		sigma = pm.HalfCauchy('sigma', 0.5, shape=n_maps)
	return rating_model