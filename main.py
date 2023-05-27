# Задача 16
'''
print('напишите длину списка ')
n = int(input())
list=[]
for i in range(n):
    list.append(int(input()))

print(list)
print('напишите число ')
x = int(input())
print(list.count(x))
'''
# Задача 18
'''
print('напишите длину списка ')
n = int(input())
list=[]
for i in range(n):
    list.append(int(input()))

print(list)
min = list[0]
print('напишите число ')
x = int(input())
for i in list:
    if abs(i-x) < abs(min - x):
        min = t
print(min)
'''
# Задача 20
listeng = {1:'AEIOLNSTR', 2:'DG', 3:'BCMP', 4:'FHVWY', 5:'K', 8:'JX', 10:'QZ'}
listru = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ', 4: 'ЙЫ',5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФЩЪ'}
print('напишите слово ')
list = input().upper()
summ = 0
for i in list:
    for j, k in listeng.items():
        if i in k:
            summ += j
for i in list:
    for j, k in listru.items():
        if i in k:
            summ += j
print(summ)
