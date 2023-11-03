"""
Запустите фоновый процесс который следит за сроком подписки пользователя( для примера 10 секунд) если время подписки вышло выведите надпись "Ваша подписка закончилась."
и завершите работу программы. В основной программе сыграйте с пользователем в игру "угадай число".
"""
import multiprocessing
import time

def subscription_timer():
    time.sleep(10)
    print("Ваша подписка закончилась.")

def guess_number():
    number = 7
    while True:
        guess = int(input("Угадайте число от 1 до 10: "))
        if guess == number:
            print("Вы угадали!")
            break
        else:
            print("Неверно, попробуйте еще раз.")

if __name__ == "__main__":
    p = multiprocessing.Process(target=subscription_timer)
    p.start()
    guess_number()
    p.terminate() # завершаем процесс таймера, если пользователь угадал число до истечения времени подписки.