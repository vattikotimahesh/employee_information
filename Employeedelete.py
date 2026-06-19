import pickle
def deleteemployee():
    with open('C:\\Users\\User\\PROJECTS\\empproj2', 'rb') as fp:
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
            recindex=index
            found=True
            break
    if found:
        records.pop(recindex)
        with open('C:\\Users\\User\\PROJECTS\\empproj', 'wb') as fp:
            for record in records:
                pickle.dump(record,fp)

            print("employee record deleted...")
    else:
        print("employee details doesn t exist..")



