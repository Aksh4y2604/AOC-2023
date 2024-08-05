input = "input.txt" 

"""
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""




def is_symbol(char):
    try: 
        int(char)
        return False
    except:
        if char != ".": 
            return True
    return False


def get_full_number(data, row, col):
    number = ''
    left, right = 0, 0
    # traverse left
    for i in range(col, -1, -1): 
        try: 
            char = int(data[row][i])
        except ValueError:
            char = None
        if char == None: 
            break
        number = data[row][i] + number
        left = i
    # traverse right
    for i in range(col+1, len(data[0])): 
        try: 
            char = int(data[row][i])
        except ValueError:
            char = None
        if char == None: 
            break
        number += data[row][i]
        right = i

    return (int(number), min(left, col), max(right, col))

def get_numbers_around_symbols(data, row, col): 
    if row < 0 or row >= len(data): 
        return 0
    if col < 0 or col >= len(data[0]):
        return 0
    row_start = max(0, row-1)
    row_end = min(len(data), row+2)
    col_start = max(0, col-1)
    col_end = min(len(data[0]), col+2)
    sum = 0
    numbers = set()
    for i in range(row_start, row_end): 
        for j in range(col_start, col_end): 
            try : 
                if type(int(data[i][j])) == int: 
                    number = get_full_number(data, i, j)
                    numbers.add(number)
            except:
                pass
    mul = 1 
    for i in numbers: 
        sum += i[0]
        if len(numbers) == 2 and data[row][col] == "*": 
            mul = mul* i[0]
    return mul if len(numbers) == 2 and data[row][col] == "*" else 0

def parse_input(input): 
    data = []
    with open(input, 'r') as file:
        while True: 
            line = file.readline()
            if not line: 
                break 
            data.append(line.strip())
    ans = 0
    for i in range(len(data)): 
        for j in range(len(data[0])): 
            if is_symbol(data[i][j]): 
                ans+= get_numbers_around_symbols(data, i, j)
    return ans
print(parse_input(input))
