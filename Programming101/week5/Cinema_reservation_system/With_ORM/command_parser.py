from cinema import Cinema
from reservation import Reservation
import sys


class CommandParser:
    def __init__(self, cinema):
        self.commands = {}  # command : function
        self.cinema = cinema

        self.__fill_commands()

    def add_command(self, command, function):
        self.commands[command] = function

    def __fill_commands(self):
        self.add_command("show_movies", self.cinema.show_movies)
        self.add_command("show_movie_projections",
                         self.cinema.show_movie_projections)
        self.add_command("help", self.cinema.get_help)
        self.add_command("exit", self.exit)
        self.add_command("cancel_reservation", self.cancel_reservation)

    def handle_command(self, command):
        args = command.split(" ")
        print(self.commands[args[0]](*args[1:]))

    def exit(self):
        sys.exit("Closing Pandora\'s Box!")

    def cancel_reservation(self, name):
        reservations = self.cinema.get_reservations_for_name(name)

        if len(reservations) == 0:
            print("No reservations for {}!".format(name))
            return
        elif len(reservations) > 1:
            print("Multiple reservations for {}".format(name))
            print("Please select reservation by ID from the following:")
            for elem in reservations:
                print(elem)

            while True:
                command = input("Select reservation ID > ")
                id = int(command)

                print(id, [r.id for r in reservations])
                if id in [int(r.id) for r in reservations]:
                    for elem in reservations:
                        if elem.id == id:
                            for_deletion = elem
                            break
                    break
        elif len(reservations) == 1:
            for_deletion = reservations[0]

        self.cinema.cancel_reservation(for_deletion)

    def make_reservation(self):
        pass


def main():
    cinema = Cinema()
    command_parser = CommandParser(cinema)

    while True:
        command = input("> ")
        command_parser.handle_command(command)


if __name__ == '__main__':
    main()
