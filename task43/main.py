# Дан спсок чисел . Посчитайте сколько  в нем пар элементов ,равных друг другу, образуют одну пару которую необходимо
# посчитать .
# Вводится список чисел.все числа списка находятся на разных строках
# input: 12323 output:2  

a = " "
a = input("Введите числа (без пробела): \n")
print (a)
counter = 0
for i in range(len(a)):
    counter += a [i+1:].count(a[i])
print(counter)    