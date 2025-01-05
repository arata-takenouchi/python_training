class Car(object):
    def run(self):
        print('run')

class ToyotaCar(Car):
    pass

class TeslaCar():
    def auto_run(self):
        print('auto run')

car = Car()
car.run()

toyota_car = ToyotaCar()
toyota_car.run()

tesla_car = TeslaCar()
tesla_car.auto_run()
tesla_car.run()