def main():
 game_items = ReadGameItems 
 ShowGameItems()


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
 

def ShowGameItems(game_items):
 for i, items in enumerate(game_items, start=1):
  print(i, items)
 main()