with open('input.txt', 'r') as file:
    data = file.read()

map = [rows for rows in data.split('\n')]

part_numbers = []

def get_number(map: str, row: int, column: int, number_list: list):
    number = ""
    start_col = column
    while map[row][column].isdigit():
        column -= 1
    while column != 139 and map[row][column + 1].isdigit():
        column += 1
        number += map[row][column]
    number_list.append(int(number))
    return column - start_col

def check_around(map: str, row: int, column: int):
    number_list = []
    for a in range(row - 1, row + 2):
        b = column - 1
        while (b < (column + 2)):
            if map[a][b].isdigit():
                b += get_number(map, a, b, number_list)
                if len(number_list) == 2:
                    part_numbers.append(number_list[0] * number_list[1])
            b += 1

if __name__ == "__main__":
    [check_around(map, row, column) for row in range(len(map)) for column in range(len(map[row])) if not map[row][column].isdigit() and map[row][column] != '.']
    print(sum(part_numbers))