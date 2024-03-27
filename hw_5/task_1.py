def caching_fibonacci():
    cache = {0: 0, 1: 1}  # Попередньо додаємо значення для 0 та 1
    def fibonacci(n):
        if n not in cache:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
