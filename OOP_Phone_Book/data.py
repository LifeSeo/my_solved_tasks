def print_data(data):
    print(data)
    
def input_data():
    answer = ""
    data = input("Записать данные (нажмите 1) | Найти данные (нажмите 2): ")
    if data == "1":
        answer = "1"
    else:
        answer = input("По каким данным произвести поиск: ")
    return answer