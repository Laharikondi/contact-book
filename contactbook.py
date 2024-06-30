contacts={}
def add_contact():
    name=input("enter the name:")
    phone=input("enter the phone number")
    if name in contacts:
        print("this contact is already exist")
    else:
        contacts[name]=phone
        print("contact added successfully")

def del_contact():
    name=input("enter the name:")
    if name in contacts:
        del contacts[name]
        print("Contact is deleted successfully")
    else:
        print("contact does not exists")

def update_contact():
    name=input("enter the name:")
    for contact in contacts:
        if contact==name:
            phone=input("enter the new phone number")
            contacts[name]=phone
            print("contact updated successfully")
            break
        else:
            print("this contact does not exists")

def search():
    name=input("enter the name:")
    for contact in contacts:
        if contact.lower()==name.lower():
            print("Contact found")
            print(contact,contacts[contact])
            break
        else:
            print("contact not found")


def display():
    if contacts=={}:
        print("there are no contacts")
    else:
        print("contact list is:\n")
        for name,phone in contacts.items():
            print(name,phone)

while(True):
    print("Contact Book Menu\n1.Add Contact\n2.Delete Contact\n3.Update Contact\n4.Search Contact\n5.Display Contacts\n6.Exit")
    ch=int(input("Enter your choicce"))
    if ch==1:
        add_contact()
        
    if ch==2:
        del_contact()
        
    if ch==3:
        update_contact()
        
    if ch==4:
        search()
        
    if ch==5:
        display()
        
    if ch==6:
        print("Exciting the contact app,Good bye..!")
        break
    
    else:
        print("Enter the correct choice")
    
