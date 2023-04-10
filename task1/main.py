# Введите 2 числа ,определить большее из них.
"cls"
a = int(input('Число а '))
b = int(input('Число b '))
if a > b:
    print(f" a = {a} больше чем b = {b}")
elif a < b:
    print(f"a = {a} меньше чем b = {b} ")
else:
    print("==")