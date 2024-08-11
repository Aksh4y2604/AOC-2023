input = "input.txt"

"""
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""
def count_points(cards): 
    points = 0
    for card in cards: 
        card1 = card[0]
        card2 = card[1]
        count = 0 
        for card in card2: 
            if card in card1: 
                count += 1 
        points += 2**(count-1)if count > 0 else 0
    return points

def parse_input(input): 
    with open(input, 'r') as f: 
        lines = f.readlines()
        cards = []
        for line in lines: 
            card = []
            line = line.strip().split(':') 
            line = line[1].strip().split('|')
            card.append(list(map(int, line[0].strip().split())))
            card.append(list(map(int, line[1].strip().split())))
            cards.append(card)
        return count_points(cards)
print(parse_input(input))
