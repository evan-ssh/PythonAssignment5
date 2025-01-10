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
    AddContacts(contacts)
    
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

def DisplayMenu():
 print()
 print("1 - Display all contacts")
 print("2 - View Contact")
 print("3 - Add a contact")
 print("4 - Delete a contact")
 print("5 - Exit program")

main()
