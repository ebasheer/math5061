import car
import motorcycle as mc

def drive(v):
    print('has {} wheels'.format(v.wheels))
    for i in range(5):
        v.speedup()
    v.slowdown()
    v.printspeed()


my_car = car.Car('bugatti', 250, 2)
my_bike = mc.Motorcycle('Honda', 120)
my_spcar = car.SportsCar('Honda', 180)

drive(my_car)
drive(my_bike)
drive(my_spcar)
