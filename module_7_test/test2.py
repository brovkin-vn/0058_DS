w = 'dhck'
w = 'dkhc'
l = list(w) 

i = len(l) - 1
while i > 0 and l[i-1] >= l[i]:
    i -= 1
if i <= 0:
    print('no answer')
print(f'i:{i}')
j = len(l) - 1    
while l[j] <= l[i-1]:
    print(f' j:{j}')
    j -= 1
print(f'i:{i}, j:{j}')   
print(f'i:{l[i-1 ]}, j:{l[j]}')    
print(l) 
l[i-1], l[j] = l[j], l[i-1]
print(l) 
l[i:] = l[len(l) - 1: i - 1 : -1]
print(l) 



