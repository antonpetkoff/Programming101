
def reduce_file_path(path):
    path = path.split('/')
    fixedPath = []

    for i in range(len(path)):
        if not (path[i] == "" or path[i] == "."):
            fixedPath.append(path[i])

    i = 0
    while i < len(fixedPath):
        if fixedPath[i] == "..":
            if i-1 >= 0:
                del fixedPath[i-1:i+1]
                i -= 1
            else:
                del fixedPath[i]
        else:
            i += 1

    result = ""
    if len(fixedPath) < 1:
        return "/"
    else:
        for elem in fixedPath:
            result += "/" + elem
    return result


def main():
    print(reduce_file_path("/"))
    print(reduce_file_path("/srv/../"))
    print(reduce_file_path("/srv/www/htdocs/wtf/"))
    print(reduce_file_path("/srv/www/htdocs/wtf"))
    print(reduce_file_path("/srv/./././././"))
    print(reduce_file_path("/etc//wtf/"))
    print(reduce_file_path("/etc/../etc/../etc/../"))
    print(reduce_file_path("//////////////"))
    print(reduce_file_path("/../"))


if __name__ == '__main__':
    main()
