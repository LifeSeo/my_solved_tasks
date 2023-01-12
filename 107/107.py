# Описать класс: имя, возраст, пол котов

class Cat:
    name = None
    age = None
    tip = None
    
    def set_date(self, name, age, tip):
        self.name = name
        self.age = age
        self.tip = tip
    
    def get_date(self):
        print(self.name, self.age, self.tip)
    
cat1 = Cat()
cat1.set_date("Васька", 3, "мужской")

cat2 = Cat()
cat2.set_date("Мурка", 2, "женский")

cat1.get_date()
cat2.get_date()