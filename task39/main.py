# Даны два массива чисел .Требуется вывести те элементы первого массива (в том порядке в каком они идут в первом массиве,которых
# нет во втром  массиве).Пользователь вводит число N- количество элементов в первом массиве ,зетем N - чисел элементы массива 
# затем число M -количество элементов во втором массиве.Затем элементы второго массива.
# input: 7-> 3 1 3 4 2 4 12
#        6-> 4 1 5 4 3 1 16   output: 3 3 2 12

a = input().split()
b = input().split()
result = []

for i in a:
    if i not in b:
        result.append(i)
print(result)        