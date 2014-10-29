import requests
from graph import DirectedGraph


class GitHubModule:

    def __init__(self):
        #elf.depth_counter = 0
        self.auth = ("tonynho", "ZiDaN4O10")
        self.graph = DirectedGraph()
        #self.fill_graph_for_user("Ivaylo-Bachvarov")
        self.fill_graph_recursion("Ivaylo-Bachvarov")

    def fill_graph_for_user(self, user):
        url = "https://api.github.com/users/{}/followers".format(user)
        user_followers = requests.get(url, auth=self.auth)
        followers_dict = user_followers.json()
        print(followers_dict)

        for follower in followers_dict:
            self.graph.add_edge(user, follower["login"])

        print(str(self.graph))

    def fill_graph_recursion(self, user):
        self.fill_graph_for_user(user)

        for follower in self.graph.nodes[user]:
            self.fill_graph_for_user(follower)

        print(str(self.graph))


def main():
    obj = GitHubModule()


if __name__ == '__main__':
    main()
