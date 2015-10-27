import json
import sys
import os.path
import subprocess

ALL_PACKAGES = "all_packages.json"

def dependencies_resolving():
    dependanceies = read_json(sys.argv[1])
    all_packages = read_json(ALL_PACKAGES)
    for dependance in dependanceies["dependencies"]:
        dfs(dependance, all_packages)

def find_all_dependances(dependance, all_packages):
    if os.path.isfile("installed_modules/{}".format(dependance)):
            print("{} is already installed".format(dependance))
            return True
    else:
        print("Installing {}".format(dependance))
        if len(all_packages[dependance]) == 0:
            pass
        else:
            print("In order to istall {}, we need {}".format(dependance, all_packages[dependance]))
            for item in all_packages[dependance]:
                return (dfs(item, all_packages))

def combine(string, arrey):
    string += arrey[0]
    for word in arrey[1:]:
        string += " and " + word
    return string

def install(filename):
    with open(filename, "w") as f:
        pass

def dfs(start, all_packages):
        visited = set()
        stack = []
        stack.append((start, 0))

        while len(stack) != 0:
            current_data = stack.pop()
            current_node = current_data[0]
            current_level = current_data[1]
            if os.path.isfile("installed_modules/{}".format(current_node)):
                print("{} is already installed".format(current_node))
                visited.add(current_node)
            if current_node not in visited:
                visited.add(current_node)
                print("Installing {}".format(current_node))
                install("installed_modules/{}".format(current_node))
                if len(all_packages[current_node]) != 0:
                    text = "In order to istall {}, we need ".format(current_node)
                    print(combine(text, all_packages[current_node]))
                for neighbour in all_packages[current_node]:
                    stack.append((neighbour, current_level + 1))

        print("All done")

        return True





def read_json(filename):
    with open(filename, "r") as f:
        info = f.read()
        needs = json.loads(info)
        return needs

def main():
    dependencies_resolving()

if __name__ == '__main__':
    main()

