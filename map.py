# let's play with some pandas
import pandas as pd
import statistics

f = pd.read_csv('heart.csv', delimiter=',')

old = f[f.age>=60]
young = f[f.age<60]

# find the mean chol of everyone older than 60
print(statistics.mean(old.chol))
# find the mean chol of everyone younger than 60
print(statistics.mean(young.chol))