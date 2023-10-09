# Initialize the dictionary with information of founding members
members = {
    1: {'name': 'Amanda Nunez', 'join_date': '03/17/2009', 'dues_paid': True},
    2: {'name': 'Barbara Molina', 'join_date': '03/17/2009', 'dues_paid': True},
    3: {'name': 'Lautaro Campos', 'join_date': '03/17/2009', 'dues_paid': True}
}

# Function to display the number of club members
def display_member_count():
    count = len(members)
    print(f'Total de miembros del club: {count}')

# Function to add a new member manually
def add_new_member():
    name = input('Ingrese el nombre del nuevo socio: ')
    join_date = input('Ingrese la fecha de ingreso del nuevo socio (dd/mm/aaaa): ')
    dues_paid = input('¿Las cuotas del nuevo socio están al día? (s/n): ').lower() == 's'
    member_number = max(members.keys()) + 1
    members[member_number] = {'name': name, 'join_date': join_date, 'dues_paid': dues_paid}
    print(f'Socio {member_number} agregado con éxito.')

# Function to mark dues as paid for an existing member
def mark_dues_paid(member_number):
    if member_number in members:
        members[member_number]['dues_paid'] = True
        print(f'El socio {member_number} ha pagado todas las cuotas adeudadas.')
    else:
        print('Socio no encontrado.')

# Function to modify the join date of all members who joined on '03/13/2018' to '03/14/2018'
def modify_join_date():
    for member_number, data in members.items():
        if data['join_date'] == '03/13/2018':
            data['join_date'] = '03/14/2018'
    print('Fechas de ingreso modificadas.')

# Function to remove a member by name and last name
def remove_member_by_name(name, last_name):
    for member_number, data in list(members.items()):
        full_name = data['name']
        if name in full_name and last_name in full_name:
            del members[member_number]
            print(f'{full_name} ha sido eliminado de la lista.')

# Function to print the complete list of members
def print_member_list():
    print('\nLista de Miembros del Club:')
    for member_number, data in members.items():
        dues_status = 'Pagado' if data['dues_paid'] else 'No Pagado'
        print(f'Socio #{member_number}, {data["name"]}, ingresó: {data["join_date"]}, cuotas: {dues_status}')

# Main program loop
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
