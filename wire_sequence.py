def run(args):

    red_occurrence = 0
    blue_occurrence = 0
    black_occurrence = 0

    red_lookup = ['c', 'b', 'a', 'a|c', 'b', 'a|c', 'a|b|c', 'a|b', 'b']
    blue_lookup = ['b', 'a|c', 'b', 'a', 'b', 'b|c', 'c', 'a|c', 'a']
    black_lookup = ['a|b|c', 'a|c', 'b', 'a|c', 'b', 'b|c', 'a|b', 'c', 'c']

    while True:
        color = input("Wire color: ")
        letter = input("Wire letter: ")
        if color == 'q' or letter == 'q': break

        if color == 'r':
            cut_if = red_lookup[red_occurrence]
            red_occurrence += 1
        elif color == 'b':
            cut_if = blue_lookup[blue_occurrence]
            blue_occurrence += 1
        elif color == 'bl':
            cut_if = black_lookup[black_occurrence]
            black_occurrence += 1
        
        if '|' in cut_if:
            cut_if_letters = cut_if.split('|')
            if letter in cut_if_letters:
                print("===CUT WIRE===")
            else:
                print("===LEAVE WIRE===")
        else:
            if letter == cut_if:
                print("===CUT WIRE===")
            else:
                print("===LEAVE WIRE===")