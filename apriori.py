import csv
import requests
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
from efficient_apriori import apriori,generate_rules_apriori

bp = csv.reader(open('./bp.csv','r'))

data = []
for heros in bp:
    hero_new = []
    for hero in heros:
        hero_new.append(hero.strip())
    data.append(hero_new[1:])

itemsets , rules = apriori(data, min_support=0.6, min_confidence=0.6)
print(itemsets)
print(rules)
