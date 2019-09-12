def run(args):
    stage_one = int(input("Stage 1: "))

    game_state = [{'pos': -1, 'num': -1} for x in range(4)]

    if stage_one == 1 or stage_one == 2:
        print("===POSITION 2===")
        game_state[0]['num'] = int(input("Number: "))
        game_state[0]['pos'] = 2
    elif stage_one == 3:
        print("===POSITION 3===")
        game_state[0]['num'] = int(input("Number: "))
        game_state[0]['pos'] = 3
    elif stage_one == 4:
        print("===POSITION 4===")
        game_state[0]['num'] = int(input("Number: "))
        game_state[0]['pos'] = 4
    
    stage_two = int(input("Stage 2: "))

    if stage_two == 1:
        print("===LABELED 4===")
        game_state[1]['num'] = 4
        game_state[1]['pos'] = int(input("Position: "))
    elif stage_two == 2 or stage_two == 4:
        print("===POSITION {}===".format(game_state[0]['pos']))
        game_state[1]['pos'] = game_state[0]['pos']
        game_state[1]['num'] = int(input("Number: "))
    elif stage_two == 3:
        print("===POSITION 1===")
        game_state[1]['pos'] = 1
        game_state[1]['num'] = int(input("Number: "))
    
    stage_three = int(input("Stage 3: "))

    if stage_three == 1:
        print("===LABELED {}===".format(game_state[1]['num']))
        game_state[2]['num'] = game_state[1]['num']
        game_state[2]['pos'] = int(input("Position: "))
    elif stage_three == 2:
        print("===LABELED {}===".format(game_state[0]['num']))
        game_state[2]['num'] = game_state[0]['num']
        game_state[2]['pos'] = int(input("Position: "))
    elif stage_three == 3:
        print("===POSITION 3===")
        game_state[2]['pos'] = 3
        game_state[2]['num'] = int(input("Number: "))
    elif stage_three == 4:
        print("===LABELED 4===")
        game_state[2]['pos'] = int(input("Position: "))
        game_state[2]['num'] = 4
    
    stage_four = int(input("Stage 4: "))

    if stage_four == 1:
        print("===POSITION {}===".format(game_state[0]['pos']))
        game_state[3]['pos'] = game_state[0]['pos']
        game_state[3]['num'] = int(input("Number: "))
    elif stage_four == 2:
        print("===POSITION 1===")
        game_state[3]['pos'] = 1
        game_state[3]['num'] = int(input("Number: "))
    elif stage_four == 3 or stage_four == 4:
        print("===POSITION {}===".format(game_state[1]['pos']))
        game_state[3]['pos'] = game_state[1]['pos']
        game_state[3]['num'] = int(input("Number: "))
    
    stage_five = int(input("Stage 5: "))

    if stage_five == 1:
        print("===LABELED {}===".format(game_state[0]['num']))
    elif stage_five == 2:
        print("===LABELED {}===".format(game_state[1]['num']))
    elif stage_five == 3:
        print("===LABELED {}===".format(game_state[3]['num']))
    elif stage_five == 4:
        print("===LABELED {}===".format(game_state[2]['num']))


