

def first_menu(class_all) :
    print('Выберите класс.')
    while True:
        for i, item in enumerate(class_all):
            print(f"\t{i + 1}. {item.replace('.txt', '')}")
        user_input = int(input('Введите ID класса >: '))
        print(class_all[user_input - 1].replace('.txt', ''))
        end = input(' Всё верно? 1 - Да 2 - Нет ')
        if end == '1':
            break
    return class_all[user_input - 1]

def second_menu(lessons: list):
    print('Выберите урок.')
    while True:
        for i, item in enumerate(lessons):
            print(f"\t{i + 1}. {item}")
        user_input = int(input('Введите ID урока >: '))
        print(lessons[user_input - 1])
        end = input(' Всё верно? 1 - Да 2 - Нет ')
        if end == '1':
            break
    return lessons[user_input - 1]

def tree_menu(students):    
    end = 0
    while True:
        print('Выберите ученика.')
        i = 0
        for key in students.keys():
            i += 1
            print(f"\t{i}. {key}")  
        user_input = input('Введите имя ученика >: ')
        print(students[user_input])
        rating = int(input(' Введите оценку ученика '))
        students[user_input].append(rating)
        end = input(' урок окончен? 1 - Да 2 - Нет ')
        if end == '1':
                break
    return students

