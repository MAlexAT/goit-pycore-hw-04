def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            count = 0
            for line in file:
                name, salary = line.strip().split(',')
                total += int(salary)
                count += 1
            if count == 0:
                return (0, 0)
            average = total / count
            return (total, average)
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return None
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None

# Приклад використання функції
total, average = total_salary("salary.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
