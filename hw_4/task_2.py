def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as fh:
            for line in fh:
                a = line.strip().split(',')
                if len(a) != 3:
                    raise ValueError("Неправильний формат рядка")
                cat = {'id': a[0], 'name': a[1], 'age': int(a[2])}
                cats_info.append(cat)
    except FileNotFoundError:
        print("Файл не знайдено. Перевірте правильність шляху.")
    except ValueError as e:
        print(f"Сталася помилка при обробці рядка: {e}")
    except Exception as e:
        print(f"Сталася помилка: {e}")
    else:
        return cats_info

print(get_cats_info('cats.TXT'))