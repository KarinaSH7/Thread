"""
Напишите 2 функции, одна считает сумму четных чисел, вторая нечетных
Запустите функции в разных процессах со значениями от 1 до 1000000
"""

import multiprocessing

def sumevennumbers(start, end):
    allnumbers = 0
    for i in range(start, end +1):
        if i % 2 == 0:
            allnumbers += 1
    print(f"Сумма всех четных числе от {start} до {end}: {allnumbers}")

def sumoddnumbers(start, end):
    allnumbers = 0
    for i in range(start, end+1):
        if i % 2 == 1:
            allnumbers += i
    print(f"Сумма всех нечетных чисел от {start} до {end}: {allnumbers}")

if __name__ == "__main__":
    start = 1
    end = 1000000
    p1 = multiprocessing.Process(target=sumevennumbers, args=(start, end))
    p2 = multiprocessing.Process(target=sumoddnumbers, args=(start, end))
    p1.start()
    p2.start()
    p1.join()
    p2.join()