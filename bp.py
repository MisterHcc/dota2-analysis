import json
import requests
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
from efficient_apriori import apriori,generate_rules_apriori

res = pd.read_csv('./duet.lnk.csv')

hero = pd.read_csv('./hero.csv')
IdToName = hero.iloc[:,[1,3]]
IdToName.index = IdToName['id']

def idtoname(id):
    try:
        name = IdToName.loc[id,'localized_name']
    except:
        name = id
    return name

ccc = DataFrame()

t = res.iloc[1,0].rfind('/')

for item in res.iloc[:,0]:
    item = item[t+1:]
    res['Game ID'] = item
    html = 'https://api.opendota.com/api/matches/' + item
    res1 = requests.get(html)

    data = res1.json()
    aaa = data['picks_bans']
    bbb = DataFrame(aaa)
    ccc[item] = bbb.iloc[:,1]

bp = ccc.transpose()
bp = bp.astype(int)

bp = bp.applymap(lambda x : idtoname(x))

bp.to_csv('./bp.csv')