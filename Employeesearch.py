#Employeesearch.py
import pickle
def searchemployee():

    with open("C:\\Users\\User\\PROJECTS\\empproj2", "rb") as fp:
        records = []
        while True:
            try:

                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break

    found = False
    empno = int(input("Enter the number to view :"))
    for record in records:
        if record[0] == empno:

            found = True
            break
    print("-" * 50)

    if found:
        print("\t employee found and valid")
    else:
        print("\t employee  are notfound and  in valid")