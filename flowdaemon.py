"""
Создайте функцию в демоне потока которая каждые 3 секунды будет писать "Вводите быстрее".
В основной части программы запросите ввод кода от бомбы и если код неверный выведите: "Вы взорвались", если верный - "Бомба разминирована"
"""

import threading
import time


def bomb_defusing_process():
    while True:
        print("Вводите быстрее")
        time.sleep(5)


def main():
    bomb_code = input("Введите код от бомбы: ")


    if bomb_code == "5674":
        print("Бомба разминирована")
    else:
        print("Вы взорвались")



thread = threading.Thread(target=bomb_defusing_process)
thread.daemon = True
thread.start()


main()
