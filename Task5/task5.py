# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

a = int(input("Введите число: "))
def fib(n):
    if n in [1,2]:
        return 1
    else:
        return fib(n-1)+fib(n-2)

list1=[]
for e in range (1,a+1):
    list1.append(fib(e))

list2 = [0]*len(list1)
i = 0
while i < len(list1):
    list2[i] = -list1[i]
    i+=1
list2.reverse()
list2[len(list2)-1] = 1
list2.insert(len(list2),0)
for g in list2:
    print(g, end=' ')
for d in list1:
    print(d, end=' ')