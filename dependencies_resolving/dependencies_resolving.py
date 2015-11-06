import json
import sys
import os.path
import subprocess

ALL_PACKAGES = "all_packages.json"

def dependencies_resolving():
    dependanceies = read_json(sys.argv[1])
    all_packages = read_json(ALL_PACKAGES)
    for dependance in dependanceies["dependencies"]:
        find_all_dependances(dependance, all_packages)
    print("All done")

def combine(string, arrey):
    string += arrey[0]
    for word in arrey[1:]:
        string += " and " + word
    return string

def install(filename):
    with open(filename, "w") as f:
        pass

VISITED = set()

def find_all_dependances(start, all_packages):
    if os.path.isfile("installed_modules/{}".format(start)):
        print("{} is already installed".format(start))
        VISITED.add(start)
    if start not in VISITED:
        VISITED.add(start)
        print("Installing {}".format(start))
        if len(all_packages[start]) != 0:
            text = "In order to istall {}, we need ".format(start)
            print(combine(text, all_packages[start]))
        for neighbour in all_packages[start]:
            find_all_dependances(neighbour, all_packages)
    install("installed_modules/{}".format(start))
    print("Installation of {} has finished".format(start))
    return True

#def dfs(start, all_packages):
#        visited = set()
#        stack = []
#        stack.append((start, 0))
#
#        while len(stack) != 0:
#            current_data = stack.pop()
#            current_node = current_data[0]
#            if os.path.isfile("installed_modules/{}".format(current_node)):
#                print("{} is already installed".format(current_node))
#                visited.add(current_node)
#            if current_node not in visited:
#                visited.add(current_node)
#                print("Installing {}".format(current_node))
#                install("installed_modules/{}".format(current_node))
#                if len(all_packages[current_node]) != 0:
#                    text = "In order to istall {}, we need ".format(current_node)
#                    print(combine(text, all_packages[current_node]))
#                for neighbour in all_packages[current_node]:
#                    stack.append(neighbour)






def read_json(filename):
    with open(filename, "r") as f:
        info = f.read()
        needs = json.loads(info)
        return needs

def main():
    dependencies_resolving()

if __name__ == '__main__':
    main()

