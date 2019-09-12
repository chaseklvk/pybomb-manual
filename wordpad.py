def run(args):
    top_left = ['ur']
    top_right = ['first', 'okay', 'c']
    middle_left = ['yes', 'led', 'they are', 'nothing']
    middle_right = ['blank', 'read', 'red', 'you', 'you\'re', 'your', 'their']
    bottom_left = ['they\'re', 'reed', 'leed', ' ', ]
    bottom_right = ['display', 'says', 'no', 'lead', 'hold on', 'you are', 'there', 'see', 'cee']

    word = input("Word on display: ")

    if word in top_left:
        print("===TOP LEFT===")
    elif word in top_right:
        print("===TOP RIGHT===")
    elif word in middle_left:
        print("===MIDDLE LEFT===")
    elif word in middle_right:
        print("===MIDDLE RIGHT===")
    elif word in bottom_left:
        print("===BOTTOM LEFT===")
    elif word in bottom_right:
        print("===BOTTOM RIGHT===")
    
    new_word = input("Word on button: ")

    translator = {
        'ready': ['yes', 'okay', 'what', 'middle', 'left', 'press', 'right', 'blank', 'ready', 'no', 'first', 'uhhh', 'nothing', 'wait'],
        'first': ['left', 'okay', 'yes', 'middle', 'no', 'right', 'nothing', 'uhhh', 'wait', 'ready', 'blank', 'what', 'press', 'first'],
        'no': ['blank', 'uhhh', 'wait', 'first', 'what', 'ready', 'right', 'yes', 'nothing', 'left', 'press', 'okay', 'no', 'middle'],
        'blank': ['wait', 'right', 'okay', 'middle', 'blank', 'press', 'ready', 'nothing', 'no', 'what', 'left', 'uhhh', 'yes', 'first'],
        'nothing': ['uhhh', 'right', 'okay', 'middle', 'yes', 'blank', 'no', 'press', 'left', 'what', 'wait', 'first', 'nothing', 'ready'],
        'yes': ['okay', 'right', 'uhhh', 'middle', 'first', 'what', 'press', 'ready', 'nothing', 'yes', 'left', 'blank', 'no', 'wait'],
        'what': ['uhhh', 'what', 'left', 'nothing', 'ready', 'blank', 'middle', 'no', 'okay', 'first', 'wait', 'yes', 'press', 'right'],
        'uhhh': ['ready', 'nothing', 'left', 'what', 'okay', 'yes', 'right', 'no', 'press', 'blank', 'uhhh', 'middle', 'wait', 'first'],
        'left': ['right', 'left', 'first', 'no', 'middle', 'yes', 'blank', 'what', 'uhhh', 'wait', 'press', 'ready', 'okay', 'nothing'],
        'right': ['yes', 'nothing', 'ready', 'press', 'no', 'wait', 'what', 'right', 'middle', 'left', 'uhhh', 'blank', 'okay', 'first'],
        'middle': ['blank', 'ready', 'okay', 'what', 'nothing', 'press', 'no', 'wait', 'left', 'middle', 'right', 'first', 'uhhh', 'yes'],
        'okay': ['middle', 'no', 'first', 'yes', 'uhhh', 'nothing', 'wait', 'okay', 'left', 'ready', 'blank', 'press', 'what', 'right'],
        'wait': ['uhhh', 'no', 'blank', 'okay', 'yes', 'left', 'first', 'press', 'what', 'wait', 'nothing', 'ready', 'right', 'middle'],
        'press': ['right', 'middle', 'yes', 'ready', 'press', 'okay', 'nothing', 'uhhh', 'blank', 'left', 'first', 'what', 'no', 'wait'],
        'you': ['sure', 'you are', 'your', 'you\'re', 'next', 'uh huh', 'ur', 'hold', 'what?', 'you', 'uh uh', 'like', 'done', 'u'],
        'you are': ['your', 'next', 'like', 'uh huh', 'what?', 'done', 'uh uh', 'hold', 'you', 'u', 'you\'re', 'sure', 'ur', 'you are'],
        'your': ['uh uh', 'you are', 'uh huh', 'your', 'next', 'ur', 'sure', 'u', 'you\'re', 'you', 'what?', 'hold', 'like', 'done'],
        'you\'re': ['you', 'you\'re', 'ur', 'next', 'uh uh', 'you are', 'u', 'your', 'what?', 'uh huh', 'sure', 'done', 'like', 'hold'],
        'ur': ['done', 'u', 'ur', 'uh huh', 'what?', 'sure', 'your', 'hold', 'you\'re', 'like', 'next', 'uh uh', 'you are', 'you'],
        'u': ['uh huh', 'sure', 'next', 'what?', 'you\'re', 'ur', 'uh uh', 'done', 'u', 'you', 'like', 'hold', 'you are', 'your'],
        'uh huh': ['uh huh', 'your', 'you are', 'you', 'done', 'hold', 'uh uh', 'next', 'sure', 'like', 'you\'re', 'ur', 'u', 'what?'],
        'uh uh': ['ur', 'u', 'you are', 'you\'re', 'next', 'uh uh', 'done', 'you', 'uh huh', 'like', 'your', 'sure', 'hold', 'what?'],
        'what?': ['you', 'hold', 'you\'re', 'your', 'u', 'done', 'uh uh', 'like', 'you are', 'uh huh', 'ur', 'next', 'what?', 'sure'],
        'done': ['sure', 'uh huh', 'next', 'what', 'your', 'ur', 'you\'re', 'hold', 'like', 'you', 'u', 'you are', 'uh uh', 'done'],
        'next': ['what?', 'uh huh', 'uh uh', 'your', 'hold', 'sure', 'next', 'like', 'done', 'you are', 'ur', 'you\'re', 'u', 'you'],
        'hold': ['you are', 'u', 'done', 'uh uh', 'you', 'ur', 'sure', 'what?', 'you\'re', 'next', 'hold', 'uh huh', 'your', 'like'],
        'sure': ['you are', 'done', 'like', 'you\'re', 'you', 'hold', 'uh huh', 'ur', 'sure', 'u', 'what?', 'next', 'your', 'uh uh'],
        'like': ['you\'re', 'next', 'u', 'ur', 'hold', 'done', 'uh uh', 'what?', 'uh huh', 'you', 'like', 'sure', 'you are', 'your']
    }

    print("===WORD LIST===")
    for w in translator[new_word]:
        print(w)