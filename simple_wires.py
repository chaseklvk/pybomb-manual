# args: vowel: T/F serial: odd/even, num_batteries, port
def run(args):
    num_wires = int(input("Number of wires: "))
    last_color = input("Color of last wire: ")

    if num_wires == 3:
        num_red = int(input("Number of RED wires: "))
        num_white = int(input("Number of WHITE wires: "))
        num_blue = int(input("Number of BLUE wires: "))
        if num_red == 0:
            print("===CUT SECOND WIRE===")
        elif last_color == 'w':
            print("===CUT LAST WIRE===")
        elif num_blue > 1:
            print("===CUT LAST BLUE WIRE===")
        else:
            print("===CUT LAST WIRE===")
    elif num_wires == 4:
        num_red = int(input("Number of RED wires: "))
        num_yellow = int(input("Number of YELLOW wires: "))
        num_blue = int(input("Number of BLUE wires: "))

        if num_red > 1 and args['last_digit'] == 'odd':
            print("===CUT LAST RED WIRE===")
        elif (last_color == 'y' and num_red == 0) or (num_blue == 1):
            print("===CUT FIRST WIRE===")
        elif num_yellow > 1 == 1:
            print("===CUT LAST WIRE===")
        else:
            print("===CUT SECOND WIRE===")

    elif num_wires == 5:
        num_black = int(input("Number of BLACK wires: "))
        num_red = int(input("Number of RED wires: "))
        num_yellow = int(input("Number of YELLOW wires: "))

        if last_color == 'bl' and args['last_digit'] == 'odd':
            print("===CUT FOURTH WIRE===")
        elif num_red == 1 and num_yellow > 1:
            print("===CUT FIRST WIRE===")
        elif num_black == 0:
            print("===CUT SECOND WIRE===")
        else:
            print("===CUT FIRST WIRE===")
    elif num_wires == 6:
        num_yellow = int(input("Number of YELLOW wires: "))
        num_red = int(input("Number of RED wires: "))
        num_white = int(input("Number of WHITE wires: "))

        if num_yellow == 0 and args['last_digit'] == 'odd':
            print("===CUT THIRD WIRE===")
        elif num_yellow == 1 and num_white > 1:
            print("===CUT FOURTH WIRE===")
        elif num_red == 0:
            print("===CUT LAST WIRE===")
        else:
            print("===CUT FOURTH WIRE===")