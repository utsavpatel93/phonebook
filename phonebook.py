#Existed phonebook
np= {'Utsav':'9312567901', 'Avinash':'8431567022', 'ABC':'1234566422'}

def call_contact():
    for name, numbers in np.items():
        print("The number of {} contact is {}\n".format(name,numbers))
call_contact()

#adding a contact in the phonebook
name1, number1 = input('Provide the name and number ').split()
np.update({name1:number1})
call_contact()

#removing a contact from phonebook
del_name = input ('Provide the name to delete from contact ')
for key in np.items():
    if (del_name == key):
        del np[key]
    else:
        print ("Contact does not exist")
call_contact()
