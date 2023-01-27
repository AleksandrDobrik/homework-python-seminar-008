import model
import view

def get_list_lessons(my_db, num_class):
    list = []
    for item in my_db[num_class].keys():
        list.append(item)
    return list

def get_list_students(my_db, my_lesson, num_class ): 
    return my_db[num_class][my_lesson]

def rating_students(my_db, students_dict, my_lesson, num_class ):
    for item in my_db[num_class][my_lesson].keys():
        my_db[num_class][my_lesson][item] = students_dict[item]

def start():
    path = view.first_menu(model.class_list)
    model.read_db(path)
    
    lesson_list = get_list_lessons(model.class_db, path.replace('.txt', ''))
    lesson = view.second_menu(lesson_list)
    print(' do',model.class_db)
    students_dict = get_list_students(model.class_db, lesson, path.replace('.txt', ''))
    students_dict = view.tree_menu(students_dict)
    
    rating_students(model.class_db, students_dict, lesson, path.replace('.txt', '')) 
    model.save_db(path.replace('.txt', ''))
    
