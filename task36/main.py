# Полиндром рекурсий
# Проверить строку полиндром или нет

a = input("Введите слово: ")
def polindrom(x):
    if len(x) <= 1:
        return True
    elif x[0] == x[-1]:
        return polindrom (x[1: -1])
    return False
print (polindrom(a))
