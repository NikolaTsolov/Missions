def points(current_x, current_y, path):
    point = [current_x, current_y]
    directions = {
        "<": (-1, 0),
        ">": (1, 0),
        "^": (0, -1),
        "v": (0, 1),
    }
    n = 1
    for direction in path:
        if direction == "~":
            n = - n
        else:
            point[0] = point[0] + n * directions[direction][0]
            point[1] = point[1] + n * directions[direction][1]
    return point

def main():
    print(points(0, 0, ">>><<<~>>>~^^^"))

if __name__ == '__main__':
    main()
