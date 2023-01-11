# Использовать конструкцию with as для обработки несуществующего файла

try:
    with open('test.txt', 'r', encoding='utf8') as file:
        print(file.read())
except FileNotFoundError:
    print("Файла не существует")
    
    