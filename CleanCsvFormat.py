import csv

def main():
 prospects = OpenProspects()
 #for row in prospects:
 #print(row['FIRST_NAME'])
 #print(row['LAST_NAME'])
 #print(row['EMAIL'])
 WriteToCleanFile(prospects)
def OpenProspects():
 prospects = []
 try:
  with open("prospects.csv",newline='') as file:
   reader = csv.DictReader(file)
   for row in reader:
    row['FIRST_NAME'] = row['FIRST_NAME'].strip().title()
    row['LAST_NAME'] = row['LAST_NAME'].strip().title()
    row['EMAIL'] = row['EMAIL'].strip().lower()
    prospects.append(row)
 except FileNotFoundError as e:
  print(f"Could not open file {e}")
 except PermissionError:
  print("User does not have needed permissions to open file")
 return prospects

def WriteToCleanFile(prospects):
 try:
  with open("formatted_prospects.csv","w",newline='') as file:
   fieldnames = ['FIRST_NAME','LAST_NAME','EMAIL']
   writer = csv.DictWriter(file,fieldnames=fieldnames)
   writer.writeheader()
   writer.writerows(prospects)
   print("FILE CREATED")
 except PermissionError:
  print("User does not have necessary permissions to create file")
main()