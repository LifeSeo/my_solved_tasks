# Создать основной класс и несколько классов наследования

class Building:
    year = None
    tip = None
    town = None
    
    def __init__(self, year, tip, town):
        self.year = year
        self.tip = tip
        self.town = town
        
    def get_info (self):
        print("Год постройки:", self.year, "Тип здания:", self.tip, "Город:", self.town)
        
        
class School(Building):
    pupils = None
    
    def __init__(self, year, tip, town, pupils):
        super(School, self).__init__(year, tip, town)
        self.pupils = pupils
        
    def get_info (self):
        super().get_info()
        print("Количество учеников:", self.pupils)
        
class Museum(Building):
    painter = None
    
    def __init__(self, year, tip, town, painter):
        super(Museum, self).__init__(year, tip, town)
        self.painter = painter
        
    def get_info (self):
        super().get_info()
        print("Количество художников:", self.painter)
        
building = Building(2001, "Жилой дом", "Москва")
building.get_info()
school = School(2001, "Жилой дом", "Москва", 1251)
school.get_info()
museum = Museum(2001, "Жилой дом", "Москва", 59)
museum.get_info()