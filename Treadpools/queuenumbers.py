"""
Создайте функцию, которая выводит на экран все делители числа.
Создайте очередь и добавьте в нее числа.
Создайте пул потоков и запустите в пуле функцию с очередью.
"""

import concurrent.futures
import queue

def finddivisors(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    print(f"Делители числа {number}: {divisors}")


numbers = []
n = int(input("Введите количество чисел: "))
for i in range(n):
    num = int(input(f"Введите число {i+1}: "))
    numbers.append(num)

q = queue.Queue()
for number in numbers:
    q.put(number)


num_threads = 3
with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
    while not q.empty():
        number = q.get()
        executor.submit(finddivisors, number)