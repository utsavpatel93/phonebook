def add_contact():
    name = input ("Enter name: ")
    number = input ("Enter number ")
    d1[name] = number
    x = input ("Do you want to add some more? Write 'no' to exit")
    if x == "no":
        return
    else:
        add_contact()

d1={}
print ("Add contacts first!")
add_contact()

def call_contact():
    for name, numbers in d1.items():
        print("The number of {} contact is {}\n".format(name,numbers))

y = input ("Do you want to see the contacts that you have added? ")
if y == 'yes':
    call_contact()
else:
    print ("Thik hai")

def del_contacts():
    for name, numbers in d1.items():
        if (del_name == name):
            del d1[name]
        print("Deleted")
    else:
        print ("Contact does not exist")

z = input ("Do you wish to delete any of the number you deleted? ")

if z == 'yes':
    del_name = input ("Type the name of the contact you wish to delete")
    del_contacts()
else:
    print ("ok!")






##adding a contact in the phonebook
##name1, number1 = input('Provide the name and number ').split()
##np.update({name1:number1})
##print ("The contact is added in contact") ####
