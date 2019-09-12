def run(args):
    words = ['about', 'after', 'again', 'below', 'could', 'every', 'first', 'found', 'great', 'house', 'large', 'learn', 'never', 'other', 'place', 'plant', 'point', 'right', 'small', 'sound', 'spell', 'still', 'study', 'their', 'there', 'these', 'thing', 'think', 'three', 'water', 'where', 'which', 'world', 'would', 'write']
    checks = [False for i in range(5)]
    
    letter_options = input("Letter options: ")
    letter_options = letter_options.split('|')

    for word in words:
        chars = [ch for ch in word]

        for i, char in enumerate(chars):
            if char in letter_options[i]:
                checks[i] = True
            
        if all(checks):
            print("WORD: ", word)
            break
        
        checks = [False for i in range(5)]