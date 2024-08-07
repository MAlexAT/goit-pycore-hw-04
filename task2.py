def create_cats_file(path):
    with open(path, 'w', encoding='utf-8') as file:
        file.write('60b90c1c13067a15887e1ae1,Tayson,3\n')
        file.write('60b90c2413067a15887e1ae2,Vika,1\n')
        file.write('60b90c2e13067a15887e1ae3,Barsik,2\n')
        file.write('60b90c3b13067a15887e1ae4,Simon,12\n')
        file.write('60b90c4613067a15887e1ae5,Tessi,5\n')

# Виклик функції для створення файлу
create_cats_file('cats_file.txt')

def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats_info = []
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cat_dict = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }
                cats_info.append(cat_dict)
            return cats_info
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return None
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None

# Приклад використання функції
cats_info = get_cats_info('cats_file.txt')
if cats_info is not None:
    print(cats_info)

