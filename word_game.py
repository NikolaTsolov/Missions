def word_game(word, table):
    count = 0
    for i in range(0, len(table)):
        for j in range(0, len(table[i])):
            if table[i][j] == word[0]:
                count += word_founder(table, (i, j), word)

    return count

DIRECTIONS = [
    (0, 1), (0, -1), (1, 0),
    (-1, 0), (1, 1), (-1, -1),
    (-1, 1), (1, -1)
]

def word_founder(table, position, word):
    count = 0
    length = 1
    for d in DIRECTIONS:
        l = len(word) - 1
        if out_of_range((position[0]+l*d[0], position[1]+l*d[1]), table):
            pass
        else:
            for n in range(1, len(word)):
                if word[n] != table[position[0]+n*d[0]][position[1]+n*d[1]]:
                    break
                length += 1
            if length == len(word):
                count += 1
            length = 1
    return count

def out_of_range(new_position, table):
    cond1 = new_position[0] >= len(table) or new_position[1] > len(table[0])
    cond2 = new_position[0] < 0 or new_position[1] < 0

    if cond1 or cond2:
        return True
    return False

def main():
    table = ["ivan", "evnh", "inav", "mvvn", "qrit"]
    print(word_game("ivan", table))

if __name__ == '__main__':
    main()

