#Employeeview.py
import pickle
def viewemployee():
    with open("C:\\Users\\User\\PROJECTS\\empproj2", "rb") as fp:
        records = []
        while True:
            try:

                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break


    found=False
    empno=int(input("Enter the number to view :"))
    for record in records:
                if record[0]==empno:
                    rec=record
                    found=True
                    break
    print("-" * 50)

    if found:
        print("employee number={}".format(rec[0]))
        print("employee name={}".format(rec[1]))
        print("employee salary={}".format(rec[2]))
        print("employee comp name={}".format(rec[3]))
    else:
        print("employee not found".format(empno))
    print("-"*50)


def viewallemployees():
        with open("C:\\Users\\User\\PROJECTS\\empproj2","rb") as fp:
            while True:
                try:
                    record = pickle.load(fp)
                    for val in record:
                        print("\t {}".format(val),end='')
                    print()
                except EOFError:
                    print("--"*20)
                    break
