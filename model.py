class_db = dict()
class_list = ['7a.txt', '7b.txt','test.txt']

def get_class_list():
    global class_list
    return class_list

def read_db(path: str):
    global class_db
    lesson_dict = dict()

    with open (path, 'r', encoding='UTF-8') as file:
        my_list = file.readlines()
        for line in my_list:
            student_dict = dict()
            new_list = line.split('|')            
            lesson = new_list[0]
            new_list= new_list[1].split(';')
                     
            for i in range(0, len(new_list)-1, 2):
                name = new_list[i]
                rating = list(map(int,(new_list[i + 1].split(',')))) 
                student_dict[name] = rating 
            lesson_dict[lesson] = student_dict
        class_db[path[0:path.find('.')]] = lesson_dict
        print(class_db)
    
        
def save_db(path: str):   
    with open((path+ '.txt'), 'w', encoding= 'UTF-8') as file:
        for key, item in class_db[path].items():
            file.write(key + '|')
            for key_item, new_item in item.items():
                file.write(key_item + ';')               
                # new_item = list(map(lambda x: str(x),new_item))
                for i in range(len(new_item)):
                    file.write(str(new_item[i]))
                    if i < len(new_item) - 1:
                        file.write(',')
                file.write(';')
            file.write('\n')
        
                   


            

