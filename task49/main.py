def show_menu():
    print("\n Выберите необходимое действие:\n"
    "1.Отобразить весь справочник\n"
    "2.Найти абонента по имени\n"
    "3.Найти абонента по фамилии\n"
    "4.Найти абонента по номеру телефона\n"
    "5.Добавить абонента в справочник\n"
    "6.Удалить абонента из справочника\n"
    "7.Изменить данные абонента в справочнике\n"
    "8.Сохранить справочник в текстовом формате\n"
    "9.Закончить работу " )
    choice = int(input())
    return choice
# Трансформируем справочник из файла список из словарей.
def parse_csv(filename):
    results =[]
    fields = ["Фамилия","Имя","Телефон","Описание"]
    with open(filename, 'r', encoding='utf-8') as data:
         for line in data:
             record = dict(zip(fields, line.strip().split(',')))
             results.append(record)
    return results
#Выполняем функции работы с телефонной книгой в зависимости от выбранногопункта меню.
def work_with_phone_book():
    choice = show_menu()
    phone_book = parse_csv('phonebook.csv')

    while(choice != 9):
        if choice ==1:
            show_phonebook(phone_book) 
        elif choice == 2:
            show_phonebook(find_by_name(phone_book)) 
        elif choice == 3:
            show_phonebook(find_by_surname(phone_book))
        elif choice == 4:
            show_phonebook(find_by_number(phone_book))
        elif choice == 5:
          add_new_user(phone_book)
          write_csv('phone_book.csv',phone_book)  
        elif choice == 6:
            delete_user(phone_book)
            rewrite_csv('phone_book',phone_book)
        elif choice == 7:
            change_userdata(phone_book)
            rewrite_csv('phone_book.csv',phone_book)
        elif choice == 8:   
            make_txt()
        choice = show_menu() 
  # 1.Отобразить весь справочник
def show_phonebook(phone_book):
    for elem in phone_book:
        for key in elem:
            print(f'{key}:{elem[key]}')
            print()
 # 2.Найти абонента по имени
def find_by_name(phone_book):
    name =input('Введите имя для поиска: ')
    results=[]
    for elem in phone_book:
        if elem['Имя']==name:
            results.append(elem)
    return results
#3. Найти абонента по фамилии
def find_by_surname(phone_book):
    surname = input('Введите имя для поиска: ')
    results =[]
    for elem in phone_book:
        if elem['Фамилия'] == surname:
            results.append(elem)
    return results
# 4.Найти абонента по номеру телефона.
def find_by_number(phone_book):
    number = input('Введите номер телефона для поиска: ')
    results =[]
    for elem in phone_book:
        if elem['Телефон'] ==number:
            results.append(elem)
            return results
# 5.Добавить абонента в справочник
def add_new_user(phone_book):
    record = dict()
    for k in phone_book[0].keys():
        record[k] = input(f'Введите {k}: ')
        phone_book.append(record)
def write_csv(filename, phone_book):
    with open(filename,'a',ecoding ='utf-8') as data:
        line =''
        for v in phone_book[-1].values():
            line += v + ','
        data.write(f'{line[:-1]}\n ')
# 6.Удалить абонента из справочника
def delete_user(phone_book):
    user = input('Введите фамилию или ямя абонента ,которого необходимо удалить: ')
    for elem in phone_book:
        for v in elem.values():
            if v == user:
                phone_book.remove(elem)
def rewrite_csv(filename, phone_book):
    with open(filename, 'w',encoding='utf-8') as data: 
         for i in range(len(phone_book)) :  
             line =''
         for v in phone_book[i].values() :
             line += v +','
    data.write(f'{line[:-1]}\n')
# 7. Изменить данные абонента в справочнике                                     
def change_userdata(phone_book):
    user = input('Введите фамилию или имя абонента данные которого необходимо изменить: ')
    changed_atr = input('Введите новое название атрибута ,который необходимо изменить: ')
    new_atr =input('Введите новое значениеатрибут: ')
    for elem in phone_book:
        for v in elem.values():
            if v == user:
               elem[changed_atr] = elem[changed_atr].replace(elem[changed_atr],new_atr)    
# #  8.Сохранить справочник в текстовом формате
# def make_txt():
#     filename = input('Введите имя файла для сохранения: ')
#     shutil.copyfile('phonebook.csv',f'{filename}txt')

# 9.Закончить работу-программа просто выйдет из цикла while и закончит работу.

# import shutil
work_with_phone_book()
            
