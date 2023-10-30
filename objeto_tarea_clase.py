class Motorcycle:
    is_new = True
    motor = False
    def __init__(self, color, license_plate, fuel_liters, number_of_wheels, brand, model, manufacture_date, top_speed, weight):
        self.color = color
        self.license_plate = license_plate
        self.fuel_liters = fuel_liters
        self.number_of_wheels = number_of_wheels
        self.brand = brand
        self.model = model
        self.manufacture_date = manufacture_date
        self.top_speed = top_speed
        self.weight = weight
        self.price = None
    def start(self):
        if not self.motor:
            self.motor = True
            print("El motor ha arrancado.")
        else:
            print("El motor ya estaba en marcha.")
    def stop(self):
        if self.motor:
            self.motor = False
            print("El motor se ha detenido.")
        else:
            print("El motor ya estaba detenido.")
    def get_price(self):
        if self.price is not None:
            return f"El precio de la motocicleta '{self.brand} {self.model}' es de {self.price} $."
        else:
            return "El precio de esta motocicleta no está especificado."
        




#--------------------
motorcycle1 = Motorcycle(
    color="Red",
    license_plate="ABC123",
    fuel_liters=10,
    number_of_wheels=2,
    brand="Honda",
    model="CBR250",
    manufacture_date="2023-10-30",
    top_speed=200,
    weight=150
)
motorcycle1.start()
motorcycle1.stop()
motorcycle1.price = 5000
print(motorcycle1.get_price())

