# Дана последовательность из N чисел и число K. Необходимо сдвинуть всю последовательность (Сдвиг циклический)
# на K Элементов в право.К- положительное число.
# input[1,2,3,4,5] k=3. output [4,5,1,2,3]

spisok = [1,2,3,4,5,] 
k =2
for i in range(k):
    a = spisok.pop(-1)
    spisok.insert(0,a)
print (spisok)    