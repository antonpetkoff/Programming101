import requests
from graph import DirectedGraph


class GitHubModule:

    URL_PATTERN = "https://api.github.com/users/{}/follow\
ers?client_id={}&client_secret={}"
    CLIENT_ID = "6fd2017ecf6841cd6666"
    CLIENT_SECRET = "19e84bb54b28974bbc2260a778b28c1139f91360"

    def __init__(self):
        self.graph = DirectedGraph()
        #self.fill_graph_for_user("tonynho")
        self.fill_graph_recursion("tonynho")

    def fill_graph_for_user(self, user):
        url = self.URL_PATTERN.format(user, self.CLIENT_ID, self.CLIENT_SECRET)
        user_followers = requests.get(url)
        followers_dict = user_followers.json()

        for follower in followers_dict:
            self.graph.add_edge(user, follower["login"])

    def fill_graph_recursion(self, user):
        self.fill_graph_for_user(user)
        followers = self.graph.nodes[user]
        temp = []

        for i in range(3):      # two more levels of depth
            for follower in followers:
                self.fill_graph_for_user(follower)
                for name in self.graph.nodes[follower]:
                    temp.append(name)
            followers = temp.copy()
            temp = []

        print(str(self.graph))


def main():
    obj = GitHubModule()


if __name__ == '__main__':
    main()
