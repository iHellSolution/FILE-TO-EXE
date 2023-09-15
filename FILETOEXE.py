import os

def command1():
    global starte
    starte = input("Enter File name: ")
    if starte == f"{starte}":
        os.system(f"pyinstaller --onefile {starte}.py")

def command2():
    global starta
    starta = input("Enter File Name: ")
    if starta == f"{starta}":
        os.system("npm i -g pkg")
        os.system(f"pkg {starta}.js")

def help():
    global command
attemps = 0
while attemps < 100:
    print("""
    ╔═╗╦╦  ╔═╗  ╔╦╗╔═╗  ╔═╗═╗ ╦╔═╗
    ╠╣ ║║  ║╣    ║ ║ ║  ║╣ ╔╩╦╝║╣ 
    ╚  ╩╩═╝╚═╝   ╩ ╚═╝  ╚═╝╩ ╚═╚═╝
    |-------------------------|
    | - - Command List - -    |
    |-------------------------|
    |   1    | PYTHON  | pip  |
    |   2    | NODE JS | node |
    |--------|---------|------|
    Made By iHellSolution""")
    command = str(input("Enter [1/2]: "))

    if command == "1" or command == "2":
       print("ok!")
       break
    else:
       print("INVALID COMMANDS! TRY AGAIN..")
       attemps += 1
       continue
if command == "1":
    command1()

elif command == "2":
    command2()

if __name__ == '__main__':
    help()
