import csv
def main():
 while True: 
  sales_data = LoadSales()
  DisplayMenu()
  command = input("Enter a command:").lower()
  if command == "monthly":
   ListSales(sales_data)
 
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

main()