# Задача №27. Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

n = input("Введите свой текст: ").split()
n = set(n)
count = 0
print(n)

for i in n:
    count +=1
print(count)

