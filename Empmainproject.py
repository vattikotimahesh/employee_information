#Empmainproject.py'
from Empmenu import menu
from EmployeeAdd import addemployee
from Employeeview import viewallemployees ,viewemployee
from Employeesearch import searchemployee
from Employeeupdate import updateemployee
from Employeedelete import deleteemployee


while True:
    try:
        menu()
        print('-'*10)
        ch=int(input("Enter your choice: "))
        match(ch):
            case 1:
                addemployee()
            case 2:
                deleteemployee()
            case 3:
                updateemployee()

            case 4:
                viewemployee()
            case 5:
                viewallemployees()
            case 6:
                    searchemployee()
            case 7:
                print("Thanks for using this project")
            case _:
                print("\t ur selection of operation wrong--try again")
                break

    except ValueError:
        print("\t Dont enter alnums/strs and symbols for choice--try again")

