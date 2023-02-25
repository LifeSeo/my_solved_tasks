# Создайте класс Soda (для определения типа газированной воды), 
# принимающий 1 аргумент при инициализации (отвечающий за добавку 
# к выбираемому лимонаду). 
# В этом классе реализуйте метод show_my_drink(), 
# выводящий на печать «Газировка и {ДОБАВКА}» в случае наличия добавки, 
# а иначе отобразится следующая фраза: «Обычная газировка»

class Soda:
    
    def __init__(self, ingredient = None):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None
        
    def show_my_drink(self):
        if self.ingredient:
            print(f"Газировка + {self.ingredient}")
        else: print("Простая газировка")
        
coctail_1 = Soda("Малинка")
coctail_1.show_my_drink()
coctail_2 = Soda()
coctail_2.show_my_drink()