import requests
from random import shuffle


class TeamMatcher:

    def __init__(self):
        self.jsonDict = self._getData()
        self.courses = self._getCourses()

    def _getData(self):
        r = requests.get("https://hackbulgaria.com/api/students/", verify=False)
        return r.json()

    def _getCourses(self):
        courses = set()
        for entry in self.jsonDict:
            for course in entry["courses"]:
                courses.add(course["name"])
        return list(courses)

    def list_courses(self):
        for i in range(len(self.courses)):
            print("[{}] {}".format(i+1, self.courses[i]))

    def match_teams(self, course_id, team_size, group_time):
        desired_match = {"group": group_time,
                         "name": self.courses[course_id-1]}
        names = []
        for entry in self.jsonDict:
            if desired_match in entry["courses"]:
                names.append(entry["name"])

        shuffle(names)

        print("==========")
        for i in range(len(names)):
            print(names[i])
            if (i+1) % team_size == 0:
                print("==========")

    @staticmethod
    def loop():
        tm = TeamMatcher()
        print("Hello, you can use one the the following commands:\n\
list_courses - this lists all the courses that are available now.\n\
match_teams <course_id>, <team_size>, <group_time>\n\
quit - for quitting")
        while True:
            command = input("Enter command>")
            if command == "list_courses":
                tm.list_courses()
            elif command.find("match_teams") != -1:
                args = command.split(" ")
                if len(args) != 4:
                    print("Invalid match_teams arguments")
                tm.match_teams(int(args[1]), int(args[2]), int(args[3]))
            elif command == "quit":
                break
        print("BYE!")


def main():
    TeamMatcher.loop()


if __name__ == '__main__':
    main()
