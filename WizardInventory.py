def main():
    wizard_item = []


def ReadFile(wizard_item):
    with open("wizard_all_items.txt") as file:
        for line in file:
         wizard_item.append(line.strip())
