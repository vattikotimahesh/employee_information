import pickle
def updateemployee():
    with open("C:\\Users\\User\\PROJECTS\\empproj2", "rb") as fp:
        records=[]
        while True:
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
        found=False
        empno=int(input("Enter employee number:"))
        for index in range(len(records)):
                if records[index][0]==empno:
                    found=True
                    recindex=index
                    break
        if found:
            empsal=float(input("enter the employee salary:"))
            empcomp=input("enter the emp company name:")
            records[recindex][2]=empsal
            records[recindex][3]=empcomp

    with open("C:\\Users\\User\\PROJECTS\\empproj", "wb") as fp:
        for record in records:
            pickle.dump(record,fp)
        print("\t emp details updated --verify")

