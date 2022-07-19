# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
a = int(input("Введите число, которое хотите представить в двоичной системе: "))
print(a)

count = 0
M = a
while M >= 1:
    count+=1
    M //=2
print(count)
num = [0]*count
i = 0
while i < count:
    if a%2 == 0:
        num[i] = 0

    if a%2 == 1:
        num[i] = 1
    i+=1  
    a //= 2
num.reverse()
for d in num:
    print(d,end='')
