"""
Напишите 2 функции
Первая должна принимать ширину, длинну и высоты комнаты и записывать в файл площадь комнаты из 4 стен.
Вторая должна записать в тот же файл расход краски исходя из соотношения 5л/кв.м.
"""

import multiprocessing

def calculate_room_area(width, length, height):
    area = 2 * height * (width + length)
    with open("room_info.txt", "w") as file:
        file.write(f"Room area: {area} sq. m\n")

def calculate_paint_usage():
    with open("room_info.txt", "r") as file:
        area = float(file.readline().split(": ")[1].split()[0])
    paint_usage = area * 5
    with open("room_info.txt", "a") as file:
        file.write(f"Paint usage: {paint_usage} liters\n")

if __name__ == "__main__":
    width = float(input("Enter the width of the room in meters: "))
    length = float(input("Enter the length of the room in meters: "))
    height = float(input("Enter the height of the room in meters: "))
    p1 = multiprocessing.Process(target=calculate_room_area, args=(width, length, height))
    p2 = multiprocessing.Process(target=calculate_paint_usage)
    p1.start()
    p2.start()
    p1.join()
    p2.join()