import csv
def main():
 contacts = ReadContacts()
 DisplayMenu()
 while True:
  try: 
   command = int(input("Command:"))
   if command == 1:
    ListContacts(contacts)
   elif command == 2:
    ViewContacts(contacts) 
   elif command == 3:
    AddContacts(contacts)
   elif command == 4:
    DeleteContact(contacts)
   elif command == 5:
    return False
  except ValueError:
   print("Invalid command. Please enter a number.")
   continue


def ReadContacts():
 contacts = []
 with open("contacts.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
   contacts.append(row)  
 return contacts

def ListContacts(contacts):
 for i, contact in enumerate(contacts, start=1):
   print(f"{i}. Name: {contact['name']}")
   print(f" Email: {contact['email']}")
   print(f" Phone: {contact['phone']}")

def ListNames(contacts):
  for i, contact in enumerate(contacts, start=1):
    print(f"{i}. {contact['name']}")

def SaveContacts(contacts):
 with open("contacts.csv", "w", newline="") as file:
  fieldnames = ['name','email', 'phone']
  writer = csv.DictWriter(file, fieldnames=fieldnames)
  writer.writeheader()
  writer.writerows(contacts)

def AddContacts(contacts):
 name = input("Name:")
 email = input("Email: ")
 phone = input("Phone#:")
 contact = {'name': name, 'email': email, 'phone': phone}
 contacts.append(contact)
 SaveContacts(contacts)

def DeleteContact(contacts):
 while True:
  ListContacts(contacts)
  user_input = int(input("Enter the number of the contact youd like to delete"))
  if user_input < 1 or user_input > len(contacts):
   print("Invaild contact number.")
   continue
  else:
   contact = contacts.pop(user_input - 1)
   SaveContacts(contacts)
   print(f"{contact['name']} was deleted from the contacts list.")
   break

def ViewContacts(contacts):
 ListNames(contacts)
 while True: 
  name = input("Enter the name of the contact you'd like to view('Press x to cancel viewing)").lower()
 
  if name == "x":
   print("Viewing of contacts was cancelled")
   break
  for contact in contacts:
   if contact['name'].lower().strip() == name:
    print(f"Name: {contact['name']}")
    print(f"Email: {contact['email']}")
    print(f"Phone: {contact['phone']}")
   
  


def DisplayMenu():
 print()
 print("1 - Display all contacts")
 print("2 - View Contact")
 print("3 - Add a contact")
 print("4 - Delete a contact")
 print("5 - Exit program")

main()
