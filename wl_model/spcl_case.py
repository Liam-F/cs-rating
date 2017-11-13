import pandas as pd
import pymc3 as pm
import numpy as np

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
		rating = pm.Normal('rating', 0, omega, shape=n_teams)
		theta_tilde = pm.Normal('rate_t', mu=0, sd=1, shape=(n_maps, n_teams))
		rating_map = pm.Deterministic('rating | map', rating + tau * theta_tilde)
		alpha = pm.Normal('alpha', 1., 0.2)
		beta = pm.Normal('beta', 0.5, 0.2)
		sigma = pm.HalfCauchy('sigma', 0.5)
	return rating_model
	
def prep_pymc_time_model(n_teams, n_maps, n_periods):
	with pm.Model() as rating_model:
		rho = pm.Uniform('rho', -1, 1)
		omega = pm.HalfNormal('omega', 0.5)
		sigma = pm.HalfNormal('sigma', 0.5)
		time_rating = [pm.Normal('rating_0', 0, omega, shape=n_teams)]
		tau = pm.HalfCauchy('tau', 0.5)
		time_rating_map = [pm.Deterministic('rating_0 | map', time_rating[0] + tau * theta_tilde)]
		for i in np.arange(1, n_periods):
			time_rating.append(pm.Normal('rating_'+str(i), rho*time_rating[i-1], sigma, shape=n_teams))
			time_rating_map.append(pm.Deterministic('rating_'+str(i)+' | map', time_rating[i] + tau * theta_tilde))

	return rating_model