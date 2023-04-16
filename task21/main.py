# Напишите программу для печати всех уникальных значений в словаре.
# input [{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},{"VII":" S005 "},{"V":" S009 "},{"VII":" S007 "}]
# output {'S001', 'S002', ' S007 ', ' S009 ', 'S005', ' S005 '}

lst =  [{"V": "S001"},
             {"V": "S002"},
             {"VI": "S001"},
             {"VI": "S005"},
             {"VII": " S005 "},
             {"V": " S009 "},
             {"VII": " S007 "}
             ]
print(lst)
a = set()
for  elem in lst:
    values = list(elem.values())[0]
    a.add (list(elem.values())[0])
print(a)