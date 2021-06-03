number = 2.5  
print(number.__class__)  
# => <class 'float'>  
  
people = ["Vasiliy", "Stanislav", "Alexandra", "Vasiliy"]  
print(people.__class__)  
# => <class 'list'>  
# Используем ключевое слово class, за которым идёт название класса, в примере это SalesReport  
class SalesReport():  
    pass  
  
# Сравните это с определением пустой функции  
# Команда pass не делает ничего; на её месте могли быть другие инструкции  
# Мы используем её только потому, что синтаксически python требует, чтобы там было хоть что-то  
def build_report():  
    pass  
  
  
# И давайте определим ещё один класс  
# Для имён классов традиционно используются имена в формате CamelCase, где начала слов отмечаются большими буквами  
# Это позволяет легко отличать их от функций, которые пишутся в формате snake_case  
class SkillfactoryStudent():  
    pass  

class SalesReport():  
    pass  
  
# создаём объект по классу  
report = SalesReport()  
  
# мы можем создавать множество объектов по одному классу  
report_2 = SalesReport()  
  
# Это будут разные объекты.   
print(report == report_2)  
# => False  