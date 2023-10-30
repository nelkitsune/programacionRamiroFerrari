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
