import pandas as pd
import numpy as np
from sklearn.mixture import GaussianMixture
from sklearn.metrics import calinski_harabaz_score
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction import DictVectorizer
import csv

hero = pd.read_csv('./hero.csv')

dvec = DictVectorizer(sparse=False)
hero_features = hero.iloc[:,3:]
hero_features = dvec.fit_transform(hero_features.to_dict(orient = 'record'))

result = {}

for i in range(3,31):
    gmmx = GaussianMixture(n_components=i)
    gmmx.fit(hero_features)
    predictionx = gmmx.predict(hero_features)
    score = calinski_harabaz_score(hero_features,predictionx)
    result[i] = score


maxi = max(result,key=result.get)
gmm = GaussianMixture(n_components=maxi)
gmm.fit(hero_features)
prediction = gmm.predict(hero_features)

hero.insert(loc = 0,column = 'group',value=prediction)
hero.to_csv('./hero_group.csv', index=False, sep=',')