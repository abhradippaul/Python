class battery:
    def battery_func(self) :
        print("This is a battery function")
class engine:
    def engine_func(self) :
        print("This is an engine function")

class Car:
    totalCars = 0
    def __init__(self, brand, model) :
        self.__brand = brand
        self.__model = model
        Car.totalCars += 1
    def display_fullname(self):
        print(self.__brand + " " + self.__model)
    @staticmethod
    def static_method():
        print("Total cars created:", Car.totalCars)

class ElectricCar(Car, engine, battery):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.__battery_size = battery_size
    def display_car_info(self):
        super().display_fullname()
        print("Battery size:", self.__battery_size)



my_corolla = Car("Toyota", "Corolla")
my_corolla.display_fullname()

my_tesla = ElectricCar("Tesla", "Model S", "100wh")
my_tesla.display_car_info()
my_tesla.battery_func()
my_tesla.engine_func()

print("Total cars created:")
Car.static_method()

def test_func(name):
    print("This is a test function that will be import from another file",name)