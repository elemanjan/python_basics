class Airplane():
    make = "KG"
    model = "Shumkar"
    year = 2020
    max_speed = 500
    odometer = 250
    is_flying = False

    def take_off(self):
        is_flying = True
        print("The plane is taking off")

    def fly(self, distance, odometer):
        self.odometer = odometer
        distance = distance
        print("The plane is flying, \ndistance: ",
              distance, "\nOdometer: ", odometer)

    def land(self):
        is_flying = False
        print("The plane is landing")


shumkar = Airplane()
shumkar.take_off()
shumkar.fly(2222, 300)
shumkar.land()
