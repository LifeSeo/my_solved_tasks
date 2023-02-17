# Задача №51. Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.

values = [0, 2, 90, 70]

characteristic = lambda x: x % 2

def same_by(characteristic, objects):
    _list = []
    if not objects:
        return True
    for i in objects:
        if characteristic(i) == 0:
            _list.append(i)
            if len(_list) == len(objects):
                return True
    return False
    
print(same_by(characteristic, values))
