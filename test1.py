#Класс находится в папке cars
class Car:  
    def __init__(self):
        print ("Двигатель заведен")
        self.name = "corolla"
        self.__make = "toyota"
        self._model = 1999

car_a = Car()  
print(car_a.name) #corolla
print(car_a._model) #1999
print(car_a.__make) #AttributeError: 'Car' object has no attribute '__make'
