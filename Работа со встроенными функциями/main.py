# Работа с функциями

# Анонимные, lambda-функции, функция сложения и умножения

def mult(a, b):
    return a * b

def sum(a, b):
    return a + b

def calc(func, a, b):
    print(func(a, b))
       
calc(mult, 5, 12)

calc(lambda a, b: a + b, 5, 6)

# Работа с функцией map

data = '1 2 3 5 8 15 23 38'.split()
print(data)

# data = list(map(int, input().split()))
# print(data)

# Работа с функцией filter

data = [i for i in range(10)]
res = list(filter(lambda i: i % 2 == 0, data))
print(res)

# Работа с функцией zip

data = [i for i in range(10)]
simvols = [i for i in range(10)]

result = list(zip(data, simvols))
print(result)

# Работа с функцией enumerate

users = ['user1', 'user2', 'user3']

data = list(enumerate(users))
print(data)

# Работа с файлами

with open("test.txt", "a") as data:
    data.write("Hi\n")
print(data)