# Евгения создала класс KgToPounds с параметром kg,
# куда передается определенное количество килограмм,
# а с помощью метода to_pounds() они переводятся в фунты.
# Создайте декоратор, который проверить на то, что вводится число


class KgToPounds:
    kg = 0
    
    def validator(func):
        def wrapper(self):
            if isinstance(self.kg, (int, float)):
                return func(self)
            else:
                raise TypeError("Введите число")
        return wrapper
    
    def __init__(self, kg):
        self.kg = kg

    @validator
    def to_pounds(self):
        return self.kg * 2.205


kg = KgToPounds(999)
print(kg.to_pounds())
