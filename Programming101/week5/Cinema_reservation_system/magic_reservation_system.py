from manage_db import ManageDB


class CinemaCLI:

    def __init__(self):
        self.db = ManageDB("cinema_cli.db")

    def make_reservation(self):
        pass

    def main_loop(self):
        while True:
            command = input("> ")

            if command == "show_movies":
                self.db.show_movies()
            elif command.find("show_movie_projections") != -1:
                args = command.strip().split(" ")
                if len(args) == 2:
                    self.db.show_movie_projections(int(args[1]), None)
                elif len(args) == 3:
                    self.db.show_movie_projections(int(args[1]), args[2])
                else:
                    print("Invalid arguments!")
            elif command == "make_reservation":
                self.make_reservation()
            elif command == "help":
                self.print_help()
            elif command == "exit":
                print("Closing Pandora\'s Box!")
                break
            else:
                print("Invalid command!")

    def print_help(self):
        print("show_movies")
        print("show_movie_projections <movie_id> [date]")
        print("nmake_reservation")
        print("ncancel_reservation <name>")
        print("help")
        print("exit")


def main():
    cli = CinemaCLI()
    cli.main_loop()

if __name__ == '__main__':
    main()
