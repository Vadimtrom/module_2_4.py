# Разделить данный список на простые и составные числа
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# создаём пустые списки
primes = []
not_primes = []
# при помощи цикла for перебираем список
for i in numbers:
    if i < 2:                    # число 1 не является ни простым, ни составным числом
        continue
    is_prime = True              # Запишем значение True в переменную is_prime

    for j in range(2,i):         # вложенный цикл for, для подборки делителя
        if i % j == 0:           # проверяем на простоту числа
            is_prime = False
            break

    if is_prime:
        primes.append(i)         # добавляем в список primes, простые числа
    else:
        not_primes.append(i)     # добавляем в список not_primes, составные числа

print('Primes: ',primes)
print('Not primes: ',not_primes)