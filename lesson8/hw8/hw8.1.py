class Car:
    owner = "Eleman"
    make = "KG"
    model = "Tulpar"
    year = 2020
    odometer = 300
    is_going = False

    def go(self, distance, odometer):
        self.odometer = odometer
        self.distance = distance
        is_going = True
        print("Car's going, distance is",
              distance, "odometer is ", odometer)

    def stop(self):
        is_going = False
        print("Car's stopped")


tulpar = Car()
tulpar.go(200, 100)
print(tulpar.odometer)
tulpar.stop()
