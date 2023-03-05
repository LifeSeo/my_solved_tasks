# Дан рандомный массив и цисло k, необходимо найти максимальный элемент из диапазона k

from random import randint as rd

k = 3

lst = list(map(lambda _: rd(1, 99), range(10)))
print(lst)

def max_k(lst, k):
    for (i, item) in enumerate(lst):
        if len((lst[0+i:k+i])) >= k:
            print(max(lst[0+i:k+i]))
        
        
max_k(lst, k)