def run(args):
    button_color = input("Color of button: ")
    button_text = input("Button text: ")

    if button_color == 'w':
        car_indicator = bool(int(input("Lit CAR indicator? ")))
    
    if args['num_batteries'] > 2:
        frk_indicator = bool(int(input("Lit FRK indicator? ")))
    
    hold_button = False
    press_and_release = False

    if button_color == 'b' and button_text == 'abort':
        hold_button = True
    elif args['num_batteries'] > 1 and button_text == 'detonate':
        press_and_release = True
    elif button_color == 'w' and car_indicator:
        hold_button = True
    elif args['num_batteries'] > 2 and frk_indicator:
        press_and_release = True
    elif button_color == 'y':
        hold_button = True
    elif button_color == 'r' and button_text == 'hold':
        press_and_release = True
    else:
        hold_button = True
    
    if press_and_release: print("===PRESS AND IMMEDIATELY RELEASE===")

    if hold_button:
        print("===PRESS AND HOLD===")
        strip_color = input("Strip color: ")

        if strip_color == 'b':
            print("===RELEASE AT 4===")
        elif strip_color == 'y':
            print("===RELEASE AT 5===")
        else: 
            print("===RELEASE AT 1===")

