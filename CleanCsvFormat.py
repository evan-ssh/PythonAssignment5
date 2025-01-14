import csv

def main():
 prospects = OpenProspects()
 for row in prospects:
  print(row['FIRST_NAME'])
  print(row['LAST_NAME'])
  print(row['EMAIL'])

def OpenProspects():
 prospects = []
 try:
  with open("prospects.csv") as file:
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
main()