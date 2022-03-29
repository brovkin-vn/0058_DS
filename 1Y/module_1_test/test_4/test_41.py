import pandas as pd
from IPython.display import display


# log = pd.read_csv('module_4/log.csv', header = None)
# log.columns =[ 'user_id','time','bet','win']
# display(log)

# sample = pd.read_csv('module_4/sample.csv')
# sample.columns = ['name', 'city', 'age', 'profession']
# columns = sample.columns
# print(columns)

# users = pd.read_csv('module_4/users.csv', encoding="koi8_r", sep='\t')
# users.columns=['user_id','email','geo']
# display(users)

# sample = pd.read_csv('module_4/sample.csv')
# sample.columns = ['name', 'city', 'age', 'profession']
# columns = sample.columns
# display(sample.city)
# sample.info()

# log = pd.read_csv('module_4/log.csv', header = None)
# log.columns =[ 'user_id','time','bet','win']
# display(log.user_id.unique())

# df[df['column']>X]
# df[(df['column_name_1']>X) & (df['column_name_2']<Y)]

# sample = pd.read_csv('module_4/sample.csv')
# sample2 = sample[sample['Age'] < 30]
# display(sample2)

# log = pd.read_csv("module_4/log.csv",header=None)
# log.columns = ['user_id','time', 'bet','win']
# log_win = log[log['win'] > log['bet']]
# win_count=log_win.user_id.count()
# display(win_count)


# sample = pd.read_csv("module_4/sample.csv")
# sample2 = sample[(sample['Age'] < 30) & (sample['Profession'] == 'Рабочий')]
# display(sample2)

# sample.query('City in ["Рига", "Сочи","Чебоксары", "Сургут"] & 21<Age<50 & Profession!="Менеджер"')

# log = pd.read_csv("module_4/log.csv",header=None)
# log.columns = ['user_id','time', 'bet','win']
# # Напишите ваш код ниже
# log2 = log.query('bet < 2000 & win > 0')
# display(log2)


# str.match ("abc") — ищет строки, которые начинаются c abc,
# str.contains ("abc") — ищет строки, в которых есть abc.
# sample.Name.str.match("К", na=False)

# sample = pd.read_csv("module_4/sample.csv")
# sample2 = sample[sample.Name.str.match("К", na=False)]
# sample2 = sample[~sample.Name.str.match("К", na=False)]
# sample3 = sample[sample.City.str.contains("о", na=False)]
# sample4 = sample[~sample.City.str.contains("о", na=False)]
# display(sample4)

# log = pd.read_csv("module_4/log.csv",header=None)
# log.columns = ['user_id','time', 'bet','win']
# new_log = log[~log.user_id.str.contains("error", na=False)]
# display(new_log)

# sample.Age.apply(lambda x:x**2)

# sample = pd.read_csv("module_4/sample.csv")
# sample2 = sample
# sample2.Age = sample.Age.apply(lambda x:x+1)
# sample2.City = sample.City.apply(lambda s:str(s).lower())

# def profession_code(s):
#     if s == 'Рабочий':
#         return 0
#     elif s == 'Менеджер':
#         return 1
#     else:
#         return 2

# sample2.Profession = sample.Profession.apply(profession_code)        
# display(sample2)

# def age_category(age):
#     if age < 23:
#         return 'молодой'
#     elif age <= 35:
#         return 'средний'
#     else:
#         return 'зрелый'

# sample2 = sample
# sample2['Age_category'] = sample.Age.apply(age_category)        
# display(sample2)

# log = pd.read_csv("module_4/log.csv",header=None)
# log.columns = ['user_id','time', 'bet','win']
# # Напишите ваш код ниже

# def extr(s):
#     v = s.split('-')
#     if(len(v) > 1):
#         return f"{v[1].replace(' ' , '')}"
#     else:
#         return ''


# log.user_id = log.user_id.apply(extr)            

# display(log)

log = pd.read_csv('module_4/log.csv', header=None)
log.columns = ['user_id','time','bet','win']
# Напишите ваш код ниже
log = log.time.apply(lambda s:str(s).replace('[',''))     
            
display(log)
