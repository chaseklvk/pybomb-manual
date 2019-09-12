import numpy as np

def run(args):
    # Lookup table: [red][blue][star][led]
    # 1 == CUT WIRE, 2 == LEAVE WIRE, 3 == CUT IF EVEN SERIAL
    # 4 == CUT IF PARALLEL PORT, 5 == CUT IF TWO OR MORE BATTERIES
    lookup_table = np.ndarray((2, 2, 2, 2), dtype=int)
    lookup_table[0][0][0][0] = 1
    lookup_table[0][0][0][1] = 2
    lookup_table[0][0][1][0] = 1
    lookup_table[0][0][1][1] = 5
    lookup_table[0][1][0][0] = 3
    lookup_table[0][1][0][1] = 4
    lookup_table[0][1][1][0] = 2
    lookup_table[0][1][1][1] = 4
    lookup_table[1][0][0][0] = 3
    lookup_table[1][0][0][1] = 5
    lookup_table[1][0][1][0] = 1
    lookup_table[1][0][1][1] = 5
    lookup_table[1][1][0][0] = 3
    lookup_table[1][1][0][1] = 3
    lookup_table[1][1][1][0] = 4
    lookup_table[1][1][1][1] = 2

    while True:
        red = input("Has red coloring: ")
        if red == 'q': 
            break
        else:
            red = int(red)
        
        blue = int(input("Has blue coloring: "))
        star = int(input("Has star: "))
        led = int(input("Has LED: "))

        value = lookup_table[red][blue][star][led]

        if value == 1:
            print("===CUT WIRE===")
        elif value == 2:
            print("===LEAVE WIRE===")
        elif value == 3:
            if args['last_digit'] == 'even':
                print("===CUT WIRE===")
            else:
                print("===LEAVE WIRE===")
        elif value == 4:
            if args['parallel_port']:
                print("===CUT WIRE===")
            else:
                print("===LEAVE WIRE===")
        elif value == 5:
            if args['num_batteries'] >= 2:
                print("===CUT WIRE===")
            else:
                print("===LEAVE WIRE===")

