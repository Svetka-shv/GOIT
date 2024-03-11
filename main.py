# 1
import datetime

def get_days_from_today(date):
    date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    today_date = datetime.date.today()
    return (today_date - date).days

print(get_days_from_today('2024-03-01'))


# 2
import random

def get_numbers_ticket(minimum, maximum, quantity):
    if not (1 <= minimum <= maximum <= 1000):
        return []
    if not (1 <= quantity <= maximum - minimum + 1):
        return []

    numbers = random.sample(range(minimum, maximum + 1), quantity)

    return sorted(numbers)

print(get_numbers_ticket(1, 49, 6))


# 4
from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        try:
            birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        except ValueError:
            print(f"Некоректна дата народження для користувача {user['name']}")
            continue

        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday <= 7:
            if birthday_this_year.weekday() >= 5:  # 5 та 6 - субота і неділя
                days_until_monday = (7 - birthday_this_year.weekday()) + 1
                birthday_this_year += timedelta(days=days_until_monday)

            upcoming_birthdays.append({
                'name': user['name'],
                'congratulation_date': birthday_this_year.strftime('%Y.%m.%d')
            })

    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Jane Smiths", "birthday": "1990.03.11"}
]
print(get_upcoming_birthdays(users))