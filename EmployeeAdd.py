#EmployeeAdd.py
import pickle

#
# def isunique(lst):
#     with open("empproj", 'wb') as fp:
#         eno=lst[0]
#         try:
#             while True:
#                 try:
#                     record=pickle.load(fp)
#                     if record == eno[0]:
#                         return False
#
#                 except EOFError:
#                     break
#         except FileNotFoundError:
#             pass
#     return True



def addemployee():
    with open("empproj2", 'ab') as fp:
        while True:
            try:
                print('-'*10)
                eno = int(input("enter the number:"))
                ename = input("enter the name:")
                empsal = float(input("enter the salary:"))
                empcom=input("Enter  emp company name:")
                print('-'*10)

                lst = list()
                lst.append(eno)
                lst.append(ename)
                lst.append(empsal)
                lst.append(empcom)

                # if isunique(lst):
                #     pickle.dump(lst,fp)
                #     print("\t Employee data saved as record in file successfully")
                # else:
                #     print("\t Employee data does nt saved  as record in file successfully")

                pickle.dump(lst, fp)
                print("\t emp data save in recorded file")
                ch = input("Enter ur choice:(yes/no)")
                if ch.lower() == 'no':
                  print("\t Thanks for using this program...")
                break
            except ValueError:
                print("\t Dont enter alnums/strs/symbols for emp and salary ")