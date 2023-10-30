#1
class Person:
    def __init__(self, name='', age=0, dni=''):
        self.__name = name
        self.__age = age
        self.__dni = dni

    def set_name(self, name):
        if len(name) > 0:
            self.__name = name
        else:
            print("Nombre no válido. Debe tener al menos un carácter.")

    def get_name(self):
        return self.__name

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Edad no válida. Debe ser un valor no negativo.")

    def get_age(self):
        return self.__age

    def set_dni(self, dni):
        if len(dni) == 9:  # Suponemos que el DNI tiene 9 caracteres
            self.__dni = dni
        else:
            print("DNI no válido. Debe tener exactamente 9 caracteres.")

    def get_dni(self):
        return self.__dni

    def mostrar(self):
        print(f"Nombre: {self.__name}")
        print(f"Edad: {self.__age}")
        print(f"DNI: {self.__dni}")

    def esMayorDeEdad(self):
        return self.__age >= 18



persona1 = Person("Juan", 25, "123456789")
persona1.mostrar()
print("¿Es mayor de edad?", persona1.esMayorDeEdad())

persona2 = Person()
persona2.set_name("Ana")
persona2.set_age(16)
persona2.set_dni("987654321")
persona2.mostrar()
print("¿Es mayor de edad?", persona2.esMayorDeEdad())


#2
class Account:
    def __init__(self, holder, balance=0.0):
        self.holder = holder
        self.balance = balance
    def set_balance(self, balance):
        if balance >= 0:
            self.balance = balance
        else:
            print("No se puede establecer un saldo negativo.")
    def get_balance(self):
        return self.balance
    def show(self):
        print("Titular: ", self.holder)
        print("Saldo: $", self.balance)
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("No se puede depositar una cantidad negativa o cero.")
    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
        else:
            print("No se puede retirar una cantidad negativa o cero.")


account_holder = "John Doe"
account = Account(account_holder, 1000.0)
account.show()
account.deposit(500)
account.withdraw(300)
account.show()

#3
class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def get_longest_side(self):
        return max(self.side1, self.side2, self.side3)
    def determine_type(self):
        if self.side1 == self.side2 == self.side3:
            return "equilátero"
        elif self.side1 == self.side2 or self.side2 == self.side3 or self.side1 == self.side3:
            return "isósceles"
        else:
            return "escaleno"

side1 = float(input("Ingrese la longitud del primer lado del triángulo: "))
side2 = float(input("Ingrese la longitud del segundo lado del triángulo: "))
side3 = float(input("Ingrese la longitud del tercer lado del triángulo: "))
triangle = Triangle(side1, side2, side3)
longest_side = triangle.get_longest_side()
print(f"El lado más largo del triángulo tiene una longitud de {longest_side} unidades.")
triangle_type = triangle.determine_type()
print(f"El triángulo es de tipo {triangle_type}.")

#4

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
class Agenda:
    def __init__(self):
        self.contacts = []
    def add_contact(self, name, phone, email):
        new_contact = Contact(name, phone, email)
        self.contacts.append(new_contact)
        print("Contacto agregado con éxito.")
    def list_contacts(self):
        if not self.contacts:
            print("La agenda está vacía.")
        else:
            print("Lista de contactos:")
            for contact in self.contacts:
                print(f"Nombre: {contact.name}")
                print(f"Teléfono: {contact.phone}")
                print(f"Email: {contact.email}")
                print("")
    def find_contact(self, name):
        found = False
        for contact in self.contacts:
            if contact.name == name:
                print(f"Contacto encontrado:")
                print(f"Nombre: {contact.name}")
                print(f"Teléfono: {contact.phone}")
                print(f"Email: {contact.email}")
                found = True
                break
        if not found:
            print(f"El contacto '{name}' no se encuentra en la agenda.")
    def edit_contact(self, name, new_phone, new_email):
        found = False
        for contact in self.contacts:
            if contact.name == name:
                contact.phone = new_phone
                contact.email = new_email
                print(f"Contacto '{name}' editado con éxito.")
                found = True
                break
        if not found:
            print(f"El contacto '{name}' no se encuentra en la agenda.")
    def close_agenda(self):
        print("Agenda cerrada.")
def menu():
    print("Menú de la Agenda:")
    print("1. Añadir contacto")
    print("2. Lista de contactos")
    print("3. Buscar contacto")
    print("4. Editar contacto")
    print("5. Cerrar agenda")
    option = input("Seleccione una opción (1/2/3/4/5): ")
    return option




agenda = Agenda()

while True:
    option = menu()
    if option == "1":
        name = input("Ingrese el nombre del contacto: ")
        phone = input("Ingrese el teléfono del contacto: ")
        email = input("Ingrese el correo electrónico del contacto: ")
        agenda.add_contact(name, phone, email)
    elif option == "2":
        agenda.list_contacts()
    elif option == "3":
        name = input("Ingrese el nombre del contacto a buscar: ")
        agenda.find_contact(name)
    elif option == "4":
        name = input("Ingrese el nombre del contacto a editar: ")
        new_phone = input("Ingrese el nuevo teléfono del contacto: ")
        new_email = input("Ingrese el nuevo correo electrónico del contacto: ")
        agenda.edit_contact(name, new_phone, new_email)
    elif option == "5":
        agenda.close_agenda()
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida (1/2/3/4/5).")
