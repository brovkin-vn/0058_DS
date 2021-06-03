class DepartmentReport():

    def __init__(self, company_name):  
        self.revenues = []  
        self.company_name = company_name  

    def add_revenue(self, v):
        self.revenues.append(v)

    def average_revenue(self):
        newvar = [int(s) for s in self.revenues]
        avg = round(sum(newvar) / len(newvar))
        return f"Average department revenue for {self.company_name}: {avg}"

    
report = DepartmentReport('Danon')
report.add_revenue(1_000_000)
report.add_revenue(400_000)
# print(report.revenues)
# => [1000000, 400000]
print(report.average_revenue())
# => 700000.0

class User():
    def __init__(self, emale, password, balance):
        self.emale = emale
        self.password = password
        self.balance = balance

    def login(self, emale, password):
        return (self.emale == emale and self.password == password)

    def update_balance(self, amount):
        self.balance = self.balance + amount


user = User("gosha@roskino.org", "qwerty", 20_000)
user.login("gosha@roskino.org", "qwerty123")
# => False
user.login("gosha@roskino.org", "qwerty")
# => True
user.update_balance(200)
user.update_balance(-500)
print(user.balance)
# => 19700

class IntDataFrame():

    def __init__(self, lst):
        self.lst = [round(x) for x in lst]
        print(self.lst)

    def count(self):
        return len([x for x in self.lst if x > 0])

    def unique(self):
        return len(set([x for x in self.lst if x > 0]))

df = IntDataFrame([4.7, 4, 3, 0, 2.4, 0.3, 4])

print(df.count())
# => 5
print(df.unique())
# => 4

class OwnLogger():

    def __init__(self):
        self.log_dic = {'info':[],'warning':[],'error':[],'all':[]}

    def log(self, message, level):
        self.log_dic[level].append(message)
        self.log_dic['all'].append(message)

    def show_last(self, level='all'):
        if len(self.log_dic[level]) == 0:
            return None 
        else:
            return self.log_dic[level][-1]


logger = OwnLogger()
logger.log("System started", "info")
logger.show_last("error")
# => None
# Некоторые интерпретаторы Python могут не выводить None, тогда в этой проверке у вас будет пустая строка
logger.log("Connection instable", "warning")
logger.log("Connection lost", "error")

print(logger.show_last())
# => Connection lost
print(logger.show_last("info"))
# => System started

class Dog():

    def bark(self):
        return "Bark!"
    
    def give_paw(self):
        return "Paw"