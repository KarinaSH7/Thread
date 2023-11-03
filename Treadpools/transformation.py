"""
Создайте функцию, которая из файла Names.txt берет имена, превращает его в путь до файла и помещает в очередь.
Создайте функцию, которая создает txt файл по пути из очереди.
Запустите все в разных потоках.
"""

import queue
import threading

def rnamesfile(filename, queue):
    with open(filename, 'r') as file:
        for line in file:
            filename = line.strip()
            queue.put(filename)

def createfilequeue(queue):
    while not queue.empty():
        filename = queue.get()
        with open(filename, 'w') as file:
            file.write('This is a new file: ' + filename)



file_queue = queue.Queue()

rnamesfile('Names.txt', file_queue)

threads = []
for _ in range(2):
    thread = threading.Thread(target=createfilequeue, args=(file_queue,))
    thread.start()
    threads.append(thread)


for thread in threads:
    thread.join()
