 def zero_div():
    return 5/0

def normal_div():
    return 5/1

def safe_exec(foo):
    try:
        return foo()
    except:
        print('division by zero')
        return 0
    

    
print(safe_exec(zero_div))
# => division by zero
# => 0

print(safe_exec(normal_div))
# => 5