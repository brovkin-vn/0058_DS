import pandas as pd

# df = pd.DataFrame({
#     'men': [80, 80.8, 57.5, 98, 50.5, 73.8, 77.4, 59.7, 77.9, 52.6],
#     'women': [57.9, 57.3, 72.8, 48.2, 59.5, 48.3, 61.2, 53.9, 53.9, 70.7]
# })

# print(round(df.men.mean() - df.women.mean(), 1))
# print(df.men.median())
# print(df.women.median())
# df2 = pd.concat([df.men, df.women])
# print(df2.median())

# df1 = pd.DataFrame({
#     'val': [2,7,4,3,6,4,1,2]
# })
# df2 = pd.DataFrame({
#     'val': [5,2,4,8,1,6,7]
# })
# print(df1.val.median())
# print(df2.val.median() - df1.val.median())

# print(round(df.men.quantile([0.25, 0.75]),1))
# print(round(df.women.quantile([0.25, 0.75]),1))
# print(round(df.quantile([0.25, 0.75]),1))

# df = pd.DataFrame({
#     'men': [80.2, 80.8, 57.5, 98, 50.5, 73.8, 77.4, 59.7, 77.9, 52.6],
#     'women': [57.9, 57.3, 72.8, 48.2, 59.5, 48.3, 61.2, 53.9, 53.9, 70.7]
# })

# print(round(df.men.max() - df.men.min(), 1))
# print(round(df.women.max() - df.women.min(), 1))
# # print(df.quantile(q=0.25, axis=0, numeric_only=True, interpolation='midpoint'))
# # print(df.quantile(q=0.75, axis=0, numeric_only=True, interpolation='midpoint'))
# Q1 = df.quantile(q=0.25, axis=0, numeric_only=True, interpolation='midpoint')
# Q3 = df.quantile(q=0.75, axis=0, numeric_only=True, interpolation='midpoint')
# print(round(Q3.men - Q1.men, 1))
# print(round(Q3.women - Q1.women, 1))

# print(round(df.men.std(), 1))
# print(round(df.men.var(), 1))
# print(round(df.women.std(), 1))
# print(round(df.women.var(), 1))
# print(df.men[df.men < (Q1.men - 1.5*(Q3.men-Q1.men))])
# print(df.men[df.men > (Q3.men + 1.5*(Q3.men-Q1.men))])
# print(df.women[df.women < (Q1.women - 1.5*(Q3.women-Q1.women))])
# print(df.women[df.women > (Q3.women + 1.5*(Q3.women-Q1.women))])

# df = pd.DataFrame({
#     'year': [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018],
#     'temp': [-4.7, -6.1, -5.5, -3.3, -7.1, -3.1, -5.2, -7.3, -12.1, -6.6, -5.9, -6.3]
# })

# Q1 = df.quantile(q=0.25, axis=0, numeric_only=True, interpolation='midpoint')
# Q3 = df.quantile(q=0.75, axis=0, numeric_only=True, interpolation='midpoint')

# print(f"Среднее: {round(df.temp.mean(),1)}")
# print(f"Медиана: {round(df.temp.median(),1)}")
# print(f"СТД: {round(df.temp.std(),1)}")
# print(f"Размах: {round(df.temp.max() - df.temp.min(),1)}")
# print(f"Межквартильный размах: {round(Q3.temp - Q1.temp,1)}")
# print(df.temp[df.temp < (Q1.temp - 1.5*(Q3.temp-Q1.temp))])
# print(df.temp[df.temp > (Q3.temp + 1.5*(Q3.temp-Q1.temp))])

df = pd.DataFrame({
    'city_a': [240, 440, 455, 475, 475, 490, 490, 500, 500, 500, 530, 550, 578, 580, 620, 687, 694, 703, 859],
    'city_b': [500, 564, 590, 600, 600, 600, 645, 650, 660, 667, 689, 692, 700, 700, 705, 735, 760, 764, 805]
})




