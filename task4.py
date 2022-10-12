# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры .

from random import Random, randint

n = int(input('Введите число '))
list = []

for i in range(n):
    list.append(randint(-n,n+1))
   
print(list)

res=1
while True:
    pos = input('Укажите позицию для вычисления - ')
    if pos == "":
        break
    elif int(pos)>n or int(pos)<n:         
         res=res*list[int(pos)]         
    else:
         print(f"Введите от 0 до {n-1}")
            
print(f'Сумма произведения:{res}')    

   
