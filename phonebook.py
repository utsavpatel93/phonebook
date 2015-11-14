import pickle
def add_contact():
    while True:
        name = input ("Enter name: ")
        number = input ("Enter number ")
        d1[name] = number
        x = input ("Do you want to add some more? ")
        if x == "no":
            break

d1={}
print ("Add contacts first!")
add_contact()

def call_contact():
    for name, number in d1.items():
        print("The number of {} contact is {}\n".format(name,number))

y = input ('Do you want to see the contacts that you have added? ')
if y == 'yes':
    call_contact()
else:
    print ("ok")

def del_contacts():
    for name, number in d1.copy().items():
        if (del_name == name):
            del d1[name]
            print ("Contact deleted!")
    else:
        print ("Contact does not exist")

z = input ("Do you wish to delete any of the number you added? ")

if z == 'yes':
    del_name = input ("Type the name of the contact you wish to delete")
    del_contacts()
else:
    print ("ok")
    
#--------------storing in file------------------
contacts = 'd1.data'
f = open(contacts,'wb')
pickle.dump(contacts,f)
f.close()

del contacts

f = open(contacts,'rb')
storedlist = pickle.load(f)

print (storedlist)
