# Работа с классами наследования

class Building:
    city = None
    age = None
    
    def __init__(self, age, city):
        self.city = city
        self.age = age
    
    def get_info(self):
        print("Год:", self.age, "Город:", self.city, "Ученики:", self.pupils)
        
        
class School(Building):
    pupils = 0
    
    def __init__(self, age, city, pupils):
        super(School, self).__init__(age, city)
        self.pupils = pupils
        
school = School(1977, "Varna", 159)
school.get_info()