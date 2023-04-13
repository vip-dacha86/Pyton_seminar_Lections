# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1. 
# Input:     5 Output:  6

A = int(input("Введите искомый номер числа Фибоначи "))
if A == 0:
    print("0")
elif A == 1:
    print("1\n или")
if (A < 0):
    print("-1")        
else:
    fib1 = 0
    fib2 = 1
    fib3 = 1
    FibIndex = 2

    while(fib2 < A):
        fib3 = fib1 + fib2
        fib1 = fib2
        fib2 = fib3
        FibIndex += 1

result = FibIndex

if fib2 == A:
  print (result)

else:
     print("-1")