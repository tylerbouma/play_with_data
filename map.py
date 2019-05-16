# let's play with some pandas
import pandas as pd
import statistics

f = pd.read_csv('heart.csv', delimiter=',')

sixty = f[f.age>=60]
fifty = f[(f.age>=50) & (f.age<60)]
forty = f[(f.age>=40) & (f.age<50)]
thirty = f[(f.age>=30) & (f.age<40)]
young = f[f.age<30]

print(int(statistics.mean(sixty.chol)))
print(int(statistics.mean(fifty.chol)))
print(int(statistics.mean(forty.chol)))
print(int(statistics.mean(thirty.chol)))
print(int(statistics.mean(young.chol)))