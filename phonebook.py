import pickle
import sys
d1 = {}
def add_contact():
    while True:
        name = input ("Enter name: ")
        number = input ("Enter number ")
        d1[name] = number
        x = input ("Do you want to add some more? ")
        if x == "no":
            break

def call_contact():
    for name, number in d1.items():
        print("The number of {} contact is {}\n".format(name,number))

def del_contacts():
    while True:
        del_name = input ("Type the name of the contact you wish to delete")
        for name, number in d1.copy().items():
            if (del_name == name):
                del d1[name]
                print ("Contact deleted!")
        z =  input("Do you want to delete some more?")
        if z == "no":
            break

#--------------storing in file------------------
contacts = d1
f = open('contacts.txt','wb')
pickle.dump(contacts,f)
f.close()
f = open('contacts.txt','rb')
storedlist = pickle.load(f)

print (storedlist)

while True:
    choice = input("Enter the choice\n 1. Add a contact\n 2. Delete a contact\n 3. View all contacts\n 4. Quit ")
    if (choice == "1"):
        add_contact()
    elif (choice == "2"):
        del_contacts()
    elif (choice == "3"):
        call_contact()
    else:
        sys.exit()
