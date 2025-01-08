def main():
 while True:
  game_items = ReadGameItems()
  player_inventory = ReadPlayerInventory()
  DisplayCommands()
  command = input("Enter a command: ")
  if command == "1":
    pass
  elif command == "2":
    ShowPlayerInventory(player_inventory)
  elif command == "3":
    DropItem(player_inventory)


def ReadGameItems():
 game_items = []
 try:
  with open("wizard_all_items.txt") as file:
   for line in file:
    line = line.replace('\n', '').strip()
    game_items.append(line)
  return game_items
 except FileNotFoundError:
  print("File wasn't found, Ensure file is in directory")  
 

def ReadPlayerInventory():
 player_inventory = []
 try:
  with open("wizard_inventory.txt") as file:
   for line in file:
    line = line.replace('\n', '').strip()
    player_inventory.append(line)
  return player_inventory
 except FileNotFoundError:
  print("File wasn't found, Ensure file is in directory")

def ShowPlayerInventory(player_inventory):
 for i, items in enumerate(player_inventory):
  print(i, items)

def SaveInventory(player_inventory):
 with open("wizard_inventory.txt") as file:
  for items in player_inventory:
   file.write(f"{items}\n")

def DropItem(player_inventory):
 while True:
  ShowPlayerInventory(player_inventory)
  try:
    user_number = int(input("Number for item to delete: "))
    if user_number < 1 or user_number > len(player_inventory):
     print("Invaild number for inventory")
    else:
     item = player_inventory.pop(user_number-1)
     print(f"{item} was dropped from the inventory.")
     SaveInventory(player_inventory)
     break
  except ValueError:
    print("Enter a vaild number (1-4)")


def DisplayCommands():
 print("COMMAND MENU")
 print("1 - Walk down the path")
 print("2 - Show your items")
 print("3 - Drop an item")
 print("4 - Exit program")
main()