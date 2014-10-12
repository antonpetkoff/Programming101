from time import time
from datetime import datetime


def pizza():
    order = {}
    orderNames = []     # without *.txt extension

    while True:
        command = input("Enter command>")
        if command.find("take") != -1:
            arguments = command.split(" ")
            if len(arguments) == 3:
                if arguments[1] in order.keys():
                    order[arguments[1]] += float(arguments[2])
                else:
                    order[arguments[1]] = float(arguments[2])
            else:
                print("Error: \"take\" has 2 arguments!")
        elif command == "status":
            for key in order.keys():
                print(key + " - " + str(order[key]))
        elif command == "save":
            ts = time()
            stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
            orderName = "orders_" + stamp
            orderNames.append(orderName)
            with open(orderName + ".txt", "w") as writeFile:
                for key in order.keys():
                    writeFile.write(key + " - " + str(order[key]) + "\n")
                print("Saved the current order to " + orderName)
        elif command == "list":
            pass
        elif command.find("load") != -1:
            pass
        elif command == "finish":
            return
        else:
            print("Unknown command!\nTry one of the following:")
            print("take <name> <price>\nstatus\nsave")
            print("list\nload <number>\nfinish")


def main():
    pizza()


if __name__ == '__main__':
    main()
