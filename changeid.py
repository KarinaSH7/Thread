"""
Создайте функцию которая принимает путь до файла из папки files и меняет в нем "ids" на "id".
Запустите функцию для каждого файла в отдельном потоке.
Измерьте время выполнения программы.
"""
import os
import threading
import time

def replace_ids(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    content = content.replace("ids", "id")
    with open(file_path, 'w') as f:
        f.write(content)

start_time = time.time()

folder_path = "files/"
file_names = os.listdir(folder_path)

threads = []
for file_name in file_names:
    file_path = folder_path + file_name
    thread = threading.Thread(target=replace_ids, args=(file_path,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

end_time = time.time()

print(f"Время выполнения программы: {end_time - start_time} секунд")