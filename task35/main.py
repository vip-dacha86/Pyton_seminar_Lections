# Задача №35. Решение в группах Напишите функцию, которая принимает одно число и проверяет, является ли оно простым.
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число) 
# Input: 5 Output: yes

def checkNum (n,i = 2):
    if n == i :
        return True
    elif n % i == 0:
        return False
    elif i * i > n:
        return True
    return checkNum(n, i + 1)
print (checkNum(6))