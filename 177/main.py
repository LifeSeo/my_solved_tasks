# Николаю требуется проверить, возможно ли из представленных 
# отрезков условной длины сформировать треугольник. 
# Для этого он решил создать класс TriangleChecker, принимающий 
# только положительные числа. 
# С помощью метода is_triangle() возвращаются следующие значения 
# (в зависимости от ситуации):
# – Ура, можно построить треугольник!;
# – С отрицательными числами ничего не выйдет!;
# – Нужно вводить только числа!;
# – Жаль, но из этого треугольник не сделать.

class TriangleChecker:
    def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c
        
    def is_triangle(self):
        if self.a > 0 and self.b > 0 and self.c > 0:
            print("Число не может быть отрицательным")
            if self.a + self.b > self.c and self.a + self.c > self.b and self.c + self.b > self.a:
                return "Супер, треугольник уже рисуется!"
            else:
                return "Эх, ничего не выйдет (("
            
triangle_1 = TriangleChecker(1, -3, 3)
print(triangle_1.is_triangle())
triangle_2 = TriangleChecker(5, 4, 3)
print(triangle_2.is_triangle())
        
        