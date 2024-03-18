# 1
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

total = total_salary('SALARY')
print(f"Загальна сума заробітної плати: {total[0]}, Середня заробітна плата: {total[1]}")

# 2
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

print(get_cats_info('CATS'))

# 4
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        raise KeyError('Contact')
    contacts[name] = phone
    return "Contact updated successfully"

def show_contact(args, contacts):
    name, _ = args
    return contacts[name]

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "show":
            print(show_contact(args, contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
