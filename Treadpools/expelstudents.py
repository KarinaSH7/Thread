"""
Отчисляем студентов в 2 раза быстрее.
Создайте 2 функции для работы с очередью.
В первой функции запросите пользователя вводить фамилии или off для завершения, добавьте фамилию в очередь.
Во второй функции выводится сообщение, что студент из очереди отчислен с фамилией студента.
В основном потоке добавьте в очередь пару фамилий и запустите функции в разных потоках.
"""
import threading
import queue

student_queue = queue.Queue()


def add_student():
    while True:
        name = input("Введите фамилию студента или 'off' для завершения: ")
        if name == 'off':
            break
        student_queue.put(name)


def dismiss_students():
    while True:
        student_name = student_queue.get()
        if student_name is None:
            break
        print(f"Студент {student_name} отчислен.")


student_queue.put("Петров")
student_queue.put("Иванов")


add_thread = threading.Thread(target=add_student)
dismiss_thread = threading.Thread(target=dismiss_students)

add_thread.start()
dismiss_thread.start()

# Ждем завершения работы потока ввода и добавляем None в очередь отчисления
add_thread.join()
student_queue.put(None)

# Ждем завершения работы потока отчисления
dismiss_thread.join()



