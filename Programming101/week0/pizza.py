from time import time
from datetime import datetime


def loadOrder(filename, orderDict):
    with open(filename, "r") as readFile:
        pass


def pizza():
    order = {}
    orderNames = []     # without *.txt extension
    isListCalled = False
    isLastOrderSaved = False

    while True:
        command = input("Enter command>")
        if command.find("take") != -1:
            arguments = command.split(" ")
            if len(arguments) == 3:
                if arguments[1] in order.keys():
                    order[arguments[1]] += float(arguments[2])
                else:
                    order[arguments[1]] = float(arguments[2])
                if isLastOrderSaved:
                    isLastOrderSaved = False
            else:
                print("Error: \"take\" has 2 arguments!")
        elif command == "status":
            for key in order.keys():
                print(key + " - " + str(order[key]))
        elif command == "save":
            if len(order.keys()) > 0:
                ts = time()
                stmp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
                orderName = "orders_" + stmp
                orderNames.append(orderName)
                with open(orderName + ".txt", "w") as writeFile:
                    for key in order.keys():
                        writeFile.write(key + " - " + str(order[key]) + "\n")
                    print("Saved the current order to " + orderName)
                isLastOrderSaved = True
            else:
                print("No orders for save! Make order with \"take\"!")
        elif command == "list":
            line = "[{}] - {}"
            if len(orderNames) > 0:
                for i in range(len(orderNames)):
                    print(line.format(i + 1, orderNames[i]))
                isListCalled = True
            else:
                print("No saved orders!")
        elif command.find("load") != -1:
            if not isListCalled:
                print("Use list command before loading")
            else:
                args = command.split(" ")
                if len(args) != 2:
                    print("Incorrect \"load\" command! No argument!")
                    continue

                if not isLastOrderSaved:
                    print("You have not saved the current order.")
                    print("If you wish to discard it,")
                    print("type load <number> again.")
                    newCommand = input("Enter command>")
                    if newCommand == command:
                        loadOrder(orderNames[int(args[1]) - 1], order)
                else:
                    loadOrder(orderNames[int(args[1]) - 1], order)
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
