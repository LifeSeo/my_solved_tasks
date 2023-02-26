# Евгения создала класс KgToPounds с параметром kg,
# куда передается определенное количество килограмм,
# а с помощью метода to_pounds() они переводятся в фунты.
# Создайте декоратор, который проверить на то, что вводится число

def validator(func):
    def wrapper(ref):
        if isinstance(ref.kg, (int, float)):
            return func(ref)
        else:
            raise TypeError("Введите число")
    return wrapper


class KgToPounds:
    kg = 0

    def __init__(self, kg):
        self.kg = kg

    @validator
    def to_pounds(self):
        return self.kg * 2.205


kg = KgToPounds(9)
print(kg.to_pounds())
