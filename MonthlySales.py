import csv
def main():
 while True: 
  sales_data = LoadSales()
  DisplayMenu()
  try:
   command = int(input("\nEnter a command:"))
   if command < 1 or command > 8:
    print("\nEnter a valid command!\n")
   if command == 1:
    ListSales(sales_data)
   elif command == 2:
    YearlySummary(sales_data)
   elif command == 3:
    EditSales(sales_data)
   elif command == 4:
    ViewSingleMonth(sales_data)
   elif command == 5:
    HighestEarnings(sales_data)
   elif command == 6:
    LowestEarnings(sales_data)
   elif command == 7:
    GoalReached(sales_data)
   elif command == 8:
    print("Terminating Program, GOODBYE!")
    return False
  except ValueError:
   print("Enter a valid command!")

def DisplayMenu():
 print("COMMAND MENU")
 print("1 - View Monthly sales")
 print("2 - View Yearly Summary")
 print("3 - Edit Sales For a Month")
 print("4 - View a Single Month")
 print("5 - View Best Month")
 print("6 - View Worst Month")
 print("7 - See If Goal Was Reached")
 print("8 - Exit program")

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
    print(f"{row['month']}", end=" ")
  print()

def YearlySummary(sales_data):
  
 sales = [row['sales'] for row in sales_data]
 total_yearly_sales = sum(sales)
 average = total_yearly_sales / 12
 print("SUMMARY\n")
 print(f"Yearly Total: {total_yearly_sales}")
 print(f"Monthly: {average:.2f}\n")

def EditSales(sales_data):
 while True:
  print("Editing sales data\n")
  ShowMonths(sales_data)
  edit_month = input("Enter the abbreviaton of the month you'd like to edit: ").title()
  if edit_month == "X":
   break

  for month in sales_data:
   if month['month'] == edit_month:
    new_sales_amount = float(input(f"Enter new $ the sales for the month of {edit_month}:"))
    month['sales'] = new_sales_amount
    WriteSales(sales_data)
    print(f"Sales amount for {edit_month} was updated")
    break
  else:
   print("Enter a valid abbreviation for the month you'd like to edit: ")
   continue 
   
def ViewSingleMonth(sales_data):
 while True:
  ShowMonths(sales_data)
  print()
  view_month = input("Enter the month you'd like to view the data for (press x to exit viewing)").title()
  if view_month == 'x':
    break
  for month in sales_data:
   if month['month'] == view_month:
    print(f"\nSales for the month of {view_month} is ${month['sales']}")
    break
  else:
   print("Invalid month('Enter The Abbreviation')")
   continue

def HighestEarnings(sales_data):
 highest_sale = max([row['sales'] for row in sales_data])
 highest_month = [row['month'] for row in sales_data if row['sales'] == highest_sale]
 for month in highest_month:
  print(f"\n{month} is the best performing month with a total of ${highest_sale}")

def LowestEarnings(sales_data):
 lowest_sale = min([row['sales'] for row in sales_data])
 lowest_month = [row['month'] for row in sales_data if row['sales'] == lowest_sale]
 for month in lowest_month:
  print(f"\n{month} is the worst performing month with a total of ${lowest_sale}")

def GoalReached(sales_data):
 company_goal = float(input("\nEnter Companies Goal: "))
 total_of_sales = sum([row['sales'] for row in sales_data])
 compare_goal = company_goal / total_of_sales * 100
 print(f"Company hit %{compare_goal:.2f} of the targeted goal\n")
main()