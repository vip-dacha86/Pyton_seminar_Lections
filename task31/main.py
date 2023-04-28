# Задача №31. Общее обсуждение Последовательностью Фибоначчи называется последовательность чисел a0 , a1 , ..., an , ..., где a0 = 0, a1 = 1,
# ak = ak-1 + ak-2 (k > 1). 
# Требуется найти N-е число Фибоначчи 
# Input: 7 Output: 21 Задание необходимо решать через рекурсию

# n = int(input("n: "))
# def Fib(n):
#     if n in (0,1):
#         return 1
#     return Fib(n-1)+Fib(n-2)
# print(Fib(n))

# факториал :

# 1*2*3*4*5

n = int(input("n: "))
def Factor (n):
    if n < 1:
        return 1
    return n * Factor (n-1)
print (Factor(n))

