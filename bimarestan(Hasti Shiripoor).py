List_of_patients=[]
def name(namelastname):
    List_of_patients.append(namelastname)
    print(List_of_patients)
def search (namelastname):
    c = 0
    for i in List_of_patients:
        if namelastname in i:
            print(namelastname,"patient is in list")
            c = 1
    if c == 1:
        return True
    if c == 0 :
        return False
def delete(namelastname):
    if search(name_lastname) == True:
        List_of_patients.remove(namelastname)
        print("new list=", List_of_patients)
    else:
        print("the name you search is not in list\n"+"your list is still:",List_of_patients)



start = int(input("enter 1 for start and 0 for end: "))
while start==1:
    number=int(input("1.save new patient\n"+"2.search name and lastname\n"+"3.delet patient\n"))
    if number==1:
        name_lastname = input("Enter your name and lastname: ")
        name(name_lastname)
    elif number==2:
        namelastname = str(input('Please Enter Patient Name : '))
        if search(namelastname) == False:
            print('There is No One With This Name')

    elif number==3:
        name_lastname = input("Enter your name and lastname: ")
        delete(name_lastname)
    start = int(input("enter 1 for start and 0 for end: "))

