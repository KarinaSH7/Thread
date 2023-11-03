"""
Напишите функцию которая через канал обмена возвращает количество валюты которую можно приобрести на n сумму денег при курсе 1 к 75.
Запустите функцию в отдельном процессе и отправьте в нее данные задержкой в 0.5 секунды передайте ей разное количество доступных денег.
Выводите количество валюты на экран по мере обработки данных.
"""
import multiprocessing

def calculatecurrency(money, conn):
    currency = money / 75
    conn.send(currency)
    conn.close()

if __name__ == "__main__":
    money_list = [50, 100, 200, 500, 1000, 2000]
    for money in money_list:
        parent_conn, child_conn = multiprocessing.Pipe()
        p = multiprocessing.Process(target=calculatecurrency, args=(money, child_conn))
        p.start()
        p.join(0.5)
        if parent_conn.poll():
            currency = parent_conn.recv()
            print(f"{money} UZS can buy {currency} currency units")
        else:
            print(f"Calculation for {money} UZS timed out")