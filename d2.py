input = "input_d2.txt"

"""
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""
def parse_games(games): 
    game_data = [[0 for _ in range(3)] for _ in range(len(games))]
    # "[red, blue, green]"
    for game_id, game in enumerate(games): 
        game = game.strip()
        game = game.split(",")
        for i in range(len(game)):
            if "red" in game[i]: 
                game_data[game_id][0] = int(game[i].strip().split(" ")[0])
            elif "blue" in game[i]: 
                game_data[game_id][1] = int(game[i].strip().split(" ")[0])
            elif "green" in game[i]: 
                game_data[game_id][2] = int(game[i].strip().split(" ")[0])
    return game_data
def is_valid_game(game_data): 
    for game in game_data: 
        if game[0] > 12: 
            return False
        if game[1] > 14:
            return False
        if game[2] > 13:
            return False
    return True

def min_ball_count(game_data): 
    r, g, b = 0, 0, 0  
    for game in game_data: 
        red, blue, green = game 
        r = max(r, red)
        b = max(b, blue)
        g = max(g, green)
    return r*g*b


def parse_input(input): 
    ans_1 = 0
    ans_2 = 0
    with open(input, 'r') as file:
        data = file.readlines()
        for line in data: 
            game_id = int(line.split(":")[0].strip()[5:])
            games = line.split(":")[1].split(";")
            game_data = parse_games(games)
            if is_valid_game(game_data): 
                ans_1 += game_id
            ans_2 += min_ball_count(game_data)
    return ans_2
print(parse_input(input))
