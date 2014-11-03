import requests
from graph import DirectedGraph


class GitHubModule:

    URL_PATTERN = "https://api.github.com/users/{}/follow\
ers?client_id={}&client_secret={}"
    CLIENT_ID = "6fd2017ecf6841cd6666"
    CLIENT_SECRET = "19e84bb54b28974bbc2260a778b28c1139f91360"

    def __init__(self, parent):
        self.parent = parent
        self.graph = DirectedGraph()
        self.fill_graph(self.parent)

    def fill_graph_for_user(self, user):
        url = self.URL_PATTERN.format(user, self.CLIENT_ID, self.CLIENT_SECRET)
        user_followers = requests.get(url)
        followers_dict = user_followers.json()

        for follower in followers_dict:
            self.graph.add_edge(user, follower["login"])

    def fill_graph(self, user):
        self.fill_graph_for_user(user)
        followers = set(self.graph.nodes[user])
        temp = set()            # use set to prevent repetitions

        for i in range(2):      # two more levels of depth
            for follower in followers:
                self.fill_graph_for_user(follower)
                for name in self.graph.nodes[follower]:
                    temp.add(name)
            followers = temp.copy()
            temp = set()

    def following(self):
        users_the_parent_follows = []
        for user in self.graph.nodes.keys():
            if self.parent in self.graph.nodes[user]:
                users_the_parent_follows.append(user)
        return users_the_parent_follows


def main():
    obj = GitHubModule("tonynho")
    print(obj.following())


if __name__ == '__main__':
    main()
