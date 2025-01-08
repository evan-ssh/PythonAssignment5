import csv
def main():
 contacts = ReadContacts()

def ReadContacts():
 contacts = []
 with open("contacts.csv") as file:
  reader = csv.reader(file)
  for row in reader:
   contacts.append(row)
 return contacts

def SaveContacts(contacts):
 with open("contacts.csv") as file:
  writer = csv.writer(file)
  writer.writerows(contacts)



def DisplayMenu():
 print()
 print("1 - Display all contacts")
 print("2 - View Contact")
 print("3 - Add a contact")
 print("4 - Delete a contact")
 print("5 - Exit program")

