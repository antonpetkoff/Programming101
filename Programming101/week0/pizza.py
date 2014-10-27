from time import time
from datetime import datetime


class Pizza:

    def __init__(self):
        self.order = {}
        self.orderNames = []
        self.isListCalled = False
        self.isLastOrderSaved = True
        self.finishCount = 0

    def loadOrder(self, orderName):
        order = {}
        with open(orderName, "r") as readFile:
            lines = readFile.readlines()
            for line in lines:
                items = line.split(" ")
                order[items[0]] = float(items[2])
        return order

    def take(self, command):
        arguments = command.split(" ")
        if len(arguments) == 3:
            if arguments[1] in self.order.keys():
                self.order[arguments[1]] += float(arguments[2])
            else:
                self.order[arguments[1]] = float(arguments[2])
            if self.isLastOrderSaved:
                self.isLastOrderSaved = False
        else:
            print("Error: \"take\" has 2 arguments!")

    def status(self):
        for key in self.order.keys():
            print(key + " - " + str(self.order[key]))

    def save(self):
        if len(self.order.keys()) > 0:
            ts = time()
            stmp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
            orderName = "orders_" + stmp
            self.orderNames.append(orderName)
            with open(orderName, "w") as writeFile:
                for key in self.order.keys():
                    writeFile.write(key + " - " + str(self.order[key]) + "\n")
                print("Saved the current order to " + orderName)
            self.isLastOrderSaved = True
        else:
            print("No orders for save! Make order with \"take\"!")

    def list(self):
        line = "[{}] - {}"
        if len(self.orderNames) > 0:
            for i in range(len(self.orderNames)):
                print(line.format(i + 1, self.orderNames[i]))
            self.isListCalled = True
        else:
            print("No saved orders!")

    def load(self, command):
        if not self.isListCalled:
            print("Use list command before loading")
        else:
            args = command.split(" ")
            if len(args) != 2:
                print("Incorrect \"load\" command! No argument!")

            if int(args[1]) > len(self.orderNames):
                print("Incorrect load ID!")

            if not self.isLastOrderSaved:
                print("You have not saved the current order.")
                print("If you wish to discard it,")
                print("type load <number> again.")
                newCommand = input("Enter command>")
                if newCommand == command:
                    self.order = self.loadOrder(self.orderNames[int(args[1])-1])
                    self.isLastOrderSaved = True
            else:
                self.order = self.loadOrder(self.orderNames[int(args[1]) - 1])
                self.isLastOrderSaved = True

    def finish(self):
        if self.finishCount == 1:
            print("Finishing order. Goodbye!")
            return 0
        if not self.isLastOrderSaved:
            print("You have not saved your order.")
            print("If you wish to continue, type finish again.")
            print("If you want to save your order, type save")
            self.finishCount = 1
            return 1
        else:
            print("Finishing order. Goodbye!")
            return 0

    @staticmethod
    def loop():
        pizza = Pizza()

        while True:
            command = input("Enter command>")
            if command.find("take") != -1:
                pizza.take(command)
            elif command == "status":
                pizza.status()
            elif command == "save":
                pizza.save()
            elif command == "list":
                pizza.list()
            elif command.find("load") != -1:
                pizza.load(command)
            elif command == "finish":
                if pizza.finish() == 0:
                    break
            else:
                print("Unknown command!\nTry one of the following:")
                print("take <name> <price>\nstatus\nsave")
                print("list\nload <number>\nfinish")


def main():
    Pizza.loop()

if __name__ == '__main__':
    main()
