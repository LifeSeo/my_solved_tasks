# 1. Вычислить число Фибоначи по номеру элемента
# 2. Вычислить номер элемента по числу Фибоначи

# a=int(input("Введите натуральное число A > 1"))
# f=2
# n1=1
# n2=0
# sf=0
# while a>sf:
#    sf=n1+n2
#    n2=n1
#    n1=sf
#    f+=1
# if a==sf:
#    print(f-1)
# else:
#    print(-1)

# Альтернативный вариант

n = int(input("Введите номер элемента: "))
list = []

def Fibonachi(n):
    if n < 2:
        return 1
    else:
        return Fibonachi(n-2)+Fibonachi(n-1)
    
print(f"Число Фибоначи: {Fibonachi(n)}")

    