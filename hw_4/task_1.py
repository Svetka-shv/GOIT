def total_salary(path):
    sum_salary = 0
    try:
        with open(path, 'r', encoding='utf-8') as fh:
            for line in fh:
                a = line.strip().split(',')
                salary = int(a[1])
                sum_salary += salary
            avg_salary = sum_salary // 3
        return sum_salary, avg_salary
    except FileNotFoundError:
        print("Файл не знайдено. Перевірте правильність шляху.")
    except Exception as e:
        print("Сталася помилка під час обробки файлу:", e)

total = total_salary('salary.TXT')
print(f"Загальна сума заробітної плати: {total[0]}, Середня заробітна плата: {total[1]}")