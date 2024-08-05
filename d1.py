file = "input.txt" 
name_map = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}
def get_first_digit(line): 
    for i, chr in enumerate(line): 
        try: 
            return (i, int(chr))
        except ValueError: 
            pass 
    return (-1, 0)

def get_last_digit(line): 
    for i, chr in enumerate(reversed(line)): 
        try: 
            return (len(line) - i, int(chr))
        except ValueError: 
            pass 
    return (-1, 0)

def get_first_named_digit(line): 
    
    for i, _ in enumerate(line): 
        for j in range(1, 6): 
            if line[i:i + j] in name_map: 
                return (i, name_map[line[i:i + j]])
    return (-1, 0)



def get_last_named_digit(line): 
    
    last_word = (-1, 0)
    for i in range(len(line)): 
        for j in range(i, len(line)): 
            if line[i:j] in name_map: 
                last_word = (i, name_map[line[i:j]])
    return last_word


def d1q1(): 
    ans = 0
    with open(file, 'r') as f: 
        while True: 
            line = f.readline()
            if not line: 
                break
            _, first_digit = get_first_digit(line)
            _, last_digit = get_last_digit(line)
            ans += int(str(first_digit) + str(last_digit))
    return ans 

def get_first_real_digit(digit, named_digit):
    if digit[0] == -1: 
        return named_digit
    if named_digit[0] == -1: 
        return digit
    if digit[0] < named_digit[0]:
        return digit
    return named_digit

def get_last_real_digit(digit, named_digit):
    if digit[0] == -1: 
        return named_digit
    if named_digit[0] == -1: 
        return digit
    if digit[0] > named_digit[0]:
        return digit
    return named_digit

def d1q2(): 
    ans = 0
    with open(file, 'r') as f: 
        while True: 
            line = f.readline()
            if not line: 
                break
            _, first_digit = get_first_real_digit(get_first_digit(line), get_first_named_digit(line))
            _, last_digit = get_last_real_digit(get_last_digit(line), get_last_named_digit(line))
            ans += int(str(first_digit) + str(last_digit))
    return ans 

def main():
    return d1q2()
print(main())
