import csv
def main():
 while True: 
  sales_data = LoadSales()
  DisplayMenu()
  command = input("Enter a command:").lower()
  if command == "monthly":
   ListSales(sales_data)
  elif command == "yearly":
   YearlySummary(sales_data)
  elif command == "edit":
   EditSales(sales_data)
 
def DisplayMenu():
 print("COMMAND MENU")
 print("Monthly - View monthly sales")
 print("Yearly - View yearly summary")
 print("Edit - Edit sales for a month")
 print("Exit - Exit program")

def LoadSales(filename = "monthly_sales.csv"):
  sales_data = {}
  try:
   with open(filename, mode="r", newline="") as file:
    reader = csv.reader(file, quotechar='"')
    for row in reader:
     month = row[0].strip()
     sales = round(float(row[1].strip()), 2)
     sales_data[month] = sales
    sales_data[row[0].strip()] = 0
  except FileNotFoundError:
   print(f"File wasn't found check the programs directory")
  except Exception as e:
   print(f"An error occured while loading the file: {e}")

  return sales_data

def ListSales(sales_data):
 for key, value in sales_data.items():
  print(f"{key}-{value}")

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