import csv
def main():
 while True: 
  sales_data = LoadSales()
  DisplayMenu()
  command = int(input("Enter a command:"))
  if command == 1:
   ListSales(sales_data)
  elif command == 2:
   YearlySummary(sales_data)
  elif command == 3:
   EditSales(sales_data)
 
def DisplayMenu():
 print("COMMAND MENU")
 print("1 - View monthly sales")
 print("2 - View yearly summary")
 print("3 - Edit sales for a month")
 print(" - Exit program")

def LoadSales(filename = "monthly_sales.csv"):
  sales_data = []
  try:
   with open(filename, mode="r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
     row['sales'] = float(row['sales'])
     sales_data.append(row)
  except FileNotFoundError:
   print(f"File wasn't found check the programs directory")
  except Exception as e:
   print(f"An error occured while loading the file: {e}")
  return sales_data
 
def WriteSales(sales_data):
  with open("monthly_sales.csv", "w", newline="") as file:
   writer = csv.DictWriter(file, fieldnames=['month','sales'])
   writer.writeheader()
   writer.writerows(sales_data)

def ListSales(sales_data):
 for row in sales_data:
  print(f"{row['month']}-{row['sales']}")

def ShowMonths(sales_data):
  print(f"{'month':>26}")
  for row in sales_data:
    print(f"{row['month']}", end="")
  print()

def YearlySummary(sales_data):
 print(f"{'Yearly Summary'}")
 value = sum(sales_data.values())
 average = value / len(sales_data)
 print(f"Yearly Total: {value}")
 print(f"Monthly: {average:.2f}")

def EditSales(sales_data):
 while True:
  print(f"{'Months':>30}")
  print(f"{'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec':1}", end=" ")
  print()
  edit_month = input("Enter the abbreviaton of the month you'd like to edit: ").title()
  if edit_month == "X":
   break
  elif edit_month in sales_data:
    new_sales = float(input(f"Enter new $ the sales for the month of {edit_month}:"))
    sales_data[edit_month] = new_sales
    print(f"Sales amount for {edit_month} was updated")
  else:
    print("Enter a vaild abbreviation for the month you'd like to edit: ")
    continue 
main()