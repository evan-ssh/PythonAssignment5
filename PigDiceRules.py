def main():
 with open("rules.txt") as file:
    for line in file:
     line = line.strip()
     print(line)
     
main()