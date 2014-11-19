from cinema import Cinema


class CommandParser:

    def __init__(self, cinema):
        self.commands = {}  # command : function

    def add_command(self, command, function):
        self.commands[command] = function

    def handle_command(self, command):
        args = command.split(" ")
        print(args)
        print(self.commands[args[0]](*args[1:]))


def main():
    cinema = Cinema()
    command_parser = CommandParser(cinema)

    command_parser.add_command("show_movies", cinema.show_movies)

    while True:
        command = input("> ")
        command_parser.handle_command(command)


if __name__ == '__main__':
    main()
