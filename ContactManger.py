import csv
def main():
 contacts = ReadContacts()

def ReadContacts():
 contacts = []
 with open("contacts.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
   contacts.append(row)  
  return contacts

def ShowContacts(contacts):
 for name, contact in contacts:
   print(f"{name}")

def SaveContacts(contacts):
 with open("contacts.csv") as file:
  writer = csv.writer(file)
  writer.writerows(contacts)

def AddContacts(contacts):
 name = input("Name:")
 email = input("Email: ")
 phone = input("Phone#:")
 contact = [name, email, phone]
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
