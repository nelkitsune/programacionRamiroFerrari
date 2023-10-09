
travelers = []
cities = []

def add_traveler():
    name = input("Ingrese el nombre del pasajero: ")
    dni = int(input("Ingrese el DNI del pasajero: "))
    destination = input("Ingrese la ciudad de destino del pasajero: ")
    travelers.append((name, dni, destination))

def add_city():
    city = input("Ingrese el nombre de la ciudad: ")
    country = input("Ingrese el país al que pertenece la ciudad: ")
    cities.append((city, country))

def find_city_by_dni():
    dni = int(input("Ingrese el DNI del pasajero: "))
    for name, passenger_dni, destination in travelers:
        if passenger_dni == dni:
            print(f"{name} viaja a {destination}.")
            return
    print("No se encontró ningún pasajero con ese DNI.")

def count_travelers_by_city():
    city = input("Ingrese el nombre de la ciudad: ")
    count = sum(1 for _, _, destination in travelers if destination == city)
    print(f"Hay {count} pasajeros viajando a {city}.")

def find_country_by_dni():
    dni = int(input("Ingrese el DNI del pasajero: "))
    for name, passenger_dni, destination in travelers:
        if passenger_dni == dni:
            for city, country in cities:
                if destination == city:
                    print(f"{name} viaja a {country}.")
                    return
    print("No se encontró ningún pasajero con ese DNI o no se ha registrado su destino.")

def count_travelers_by_country():
    country = input("Ingrese el nombre del país: ")
    count = sum(1 for _, _, destination in travelers for city, destination_country in cities if destination == city and destination_country == country)
    print(f"Hay {count} pasajeros viajando a {country}.")

while True:
    print("\nMenú:")
    print("1. Agregar pasajero")
    print("2. Agregar ciudad")
    print("3. Buscar ciudad por DNI de pasajero")
    print("4. Contar pasajeros por ciudad")
    print("5. Buscar país por DNI de pasajero")
    print("6. Contar pasajeros por país")
    print("7. Salir")
    option = input("Ingrese su opción: ")
    
    if option == "1":
        add_traveler()
    elif option == "2":
        add_city()
    elif option == "3":
        find_city_by_dni()
    elif option == "4":
        count_travelers_by_city()
    elif option == "5":
        find_country_by_dni()
    elif option == "6":
        count_travelers_by_country()
    elif option == "7":
        break
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")

#---0----0-----0----0----0----0----0----0----0---0----0---0----0-
def get_addresses_for_invoices(sales):
    addresses = set() 
    
    for customer, day, amount, address in sales:
        addresses.add(address)
    
    return list(addresses)

sales = []

while True:
    customer = input("Ingrese el nombre del cliente (o 'salir' para terminar): ")
    if customer.lower() == "salir":
        break
    
    day = int(input("Ingrese el día del mes: "))
    amount = float(input("Ingrese el monto de la compra: "))
    address = input("Ingrese el domicilio del cliente: ")
    
    sales.append((customer, day, amount, address))

invoice_addresses = get_addresses_for_invoices(sales)

print("\nDomicilios para enviar facturas:")
for address in invoice_addresses:
    print(address)

#----0----0----0----0----0---0---0----0----0----0-----0-----0

members = {
    1: {'name': 'Amanda Nunez', 'join_date': '03/17/2009', 'dues_paid': True},
    2: {'name': 'Barbara Molina', 'join_date': '03/17/2009', 'dues_paid': True},
    3: {'name': 'Lautaro Campos', 'join_date': '03/17/2009', 'dues_paid': True}
}

def display_member_count():
    count = len(members)
    print(f'Total de miembros del club: {count}')

def add_new_member():
    name = input('Ingrese el nombre del nuevo socio: ')
    join_date = input('Ingrese la fecha de ingreso del nuevo socio (dd/mm/aaaa): ')
    dues_paid = input('¿Las cuotas del nuevo socio están al día? (s/n): ').lower() == 's'
    member_number = max(members.keys()) + 1
    members[member_number] = {'name': name, 'join_date': join_date, 'dues_paid': dues_paid}
    print(f'Socio {member_number} agregado con éxito.')

def mark_dues_paid(member_number):
    if member_number in members:
        members[member_number]['dues_paid'] = True
        print(f'El socio {member_number} ha pagado todas las cuotas adeudadas.')
    else:
        print('Socio no encontrado.')

def modify_join_date():
    for member_number, data in members.items():
        if data['join_date'] == '03/13/2018':
            data['join_date'] = '03/14/2018'
    print('Fechas de ingreso modificadas.')

def remove_member_by_name(name, last_name):
    for member_number, data in list(members.items()):
        full_name = data['name']
        if name in full_name and last_name in full_name:
            del members[member_number]
            print(f'{full_name} ha sido eliminado de la lista.')

def print_member_list():
    print('\nLista de Miembros del Club:')
    for member_number, data in members.items():
        dues_status = 'Pagado' if data['dues_paid'] else 'No Pagado'
        print(f'Socio #{member_number}, {data["name"]}, ingresó: {data["join_date"]}, cuotas: {dues_status}')

while True:
    print('\nMenú:')
    print('1. Mostrar Cantidad de Miembros')
    print('2. Agregar Nuevo Socio')
    print('3. Marcar Cuotas Pagadas para un Miembro')
    print('4. Modificar Fecha de Ingreso para Miembros')
    print('5. Eliminar Miembro por Nombre')
    print('6. Imprimir Lista de Miembros')
    print('7. Salir')
    
    choice = input('Ingrese su elección: ')
    
    if choice == '1':
        display_member_count()
    elif choice == '2':
        add_new_member()
    elif choice == '3':
        member_number = int(input('Ingrese el número de socio: '))
        mark_dues_paid(member_number)
    elif choice == '4':
        modify_join_date()
        print('Fechas de ingreso modificadas.')
    elif choice == '5':
        name = input('Ingrese el primer nombre del socio a eliminar: ')
        last_name = input('Ingrese el apellido del socio a eliminar: ')
        remove_member_by_name(name, last_name)
    elif choice == '6':
        print_member_list()
    elif choice == '7':
        break
    else:
        print('Opción no válida. Por favor, ingrese una opción válida.')
