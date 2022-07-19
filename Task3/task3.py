# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
list = [1.22, 3.01, 3.64, 5.91]
b = len(list)
list2 = list
i = 0

while b > 0:
    list2[i] = list[i]%1
    b-=1
    i+=1

max = list2[0]
min = list[len(list2)-1]
for e in list2:
    if e > max:
        max = e
    if e < min:
        min = e
        
res = max - min
print(res)