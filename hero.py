import json
import pandas as pd
import numpy as np
import requests
from pandas.core.frame import DataFrame


html = 'https://api.opendota.com/api/heroes'
res = requests.get(html)
hero = res.json()

hero_data = pd.DataFrame()
hero_n = len(hero)

for i in range(hero_n):
    hero_data = hero_data.append(DataFrame(hero[i]))

roles = hero_data['roles'].unique()

hero_list = hero_data.loc[0]
hero_list = hero_list.reset_index()
hero_list.drop(columns = hero_list.columns[[0,6,7]], inplace = True )

for role in roles:
    hero_list[role] = np.NAN
    role_TF = hero_data['roles'].str.contains(role) + 0
    for i in range(hero_n):
        hero_TF = (hero_data['id'].values==1) + 0
        hero_list.loc[i,role] = sum(role_TF * hero_TF)

hero_list.to_csv('./hero.csv')

