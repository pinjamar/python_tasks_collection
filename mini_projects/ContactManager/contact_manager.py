from FileManager import *
from Customer import *
from Employee import *

while True:
    print('1. Unos kupca')
    print('2. Unos zaposlenika')
    print('3. Izlaz iz aplikacije')

    choice = input('Unesite broj ispred funkcionalnosti koju želite koristiti.')

    if choice == '1':
        name = input('Unesite ime kupca: ')
        email = input('Unesite email kupca: ')

        customer = Customer(name, email)

        append_to_file_path_open_close('customer.txt', customer.print_customer_data())
    elif choice == '2':
        name = input('Unesite ime zaposlenika: ')
        position = input('Unesite poziciju zaposlenik: ')

        employee = Employee(name, position)

        append_to_file_path_open_close('employee.txt', f'Name: {employee.name}\tPosition: {employee.position}\n')
    elif choice == '3':
        break
