def run(args):
    game_running = True

    translator_v = [
        {
            'r': 'Blue',
            'b': 'Red',
            'g': 'Yellow',
            'y': 'Green'
        },
        {
            'r': 'Yellow',
            'b': 'Green',
            'g': 'Blue',
            'y': 'Red'
        }, 
        {
            'r': 'Green',
            'b': 'Red',
            'g': 'Yellow',
            'y': 'Blue'
        }
    ]

    translator_nv = [
        {
            'r': 'Blue',
            'b': 'Yellow',
            'g': 'Green',
            'y': 'Red'
        },
        {
            'r': 'Red',
            'b': 'Blue',
            'g': 'Yellow',
            'y': 'Green'
        }, 
        {
            'r': 'Yellow',
            'b': 'Green',
            'g': 'Blue',
            'y': 'Red'
        }
    ]

    while game_running:
        pattern = input("Current Pattern: ")
        if pattern == 'q': break

        s = int(input("Number of Strikes: "))
        pattern_list = pattern.split(" ")

        response_list = []
        for p in pattern_list:
            if args['vowel']:
                response_list.append(translator_v[s][p])
            else:
                response_list.append(translator_nv[s][p])
        print("===RESPONSE===")
        for r in response_list:
            print(r)