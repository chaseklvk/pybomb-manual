def run(args):
    translator = {
        '.-': 'A',
        '-...': 'B',
        '-.-.': 'C',
        '-..': 'D',
        '.': 'E',
        '..-.': 'F',
        '--.': 'G',
        '....': 'H',
        '..': 'I',
        '.---': 'J',
        '-.-': 'K',
        '.-..': 'L',
        '--': 'M',
        '-.': 'N',
        '---': 'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.': 'R',
        '...': 'S',
        '-': 'T',
        '..-': 'U',
        '...-': 'V',
        '.--': 'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z'
    }

    frequency_table = {
        'shell': '3.505',
        'halls': '3.515',
        'slick': '3.522',
        'trick': '3.532',
        'boxes': '3.535',
        'leaks': '3.542',
        'strobe': '3.545',
        'bistro': '3.552',
        'flick': '3.555',
        'bombs': '3.565',
        'break': '3.572',
        'brick': '3.575',
        'steak': '3.582',
        'sting': '3.592',
        'vector': '3.595',
        'beats': '3.600'
    }

    while True:
        sequence = input("Sequence: ")
        if sequence == 'q': break

        code = sequence.split(" ")
        temp_letters = []
        for i, c in enumerate(code):
            print("Letter {}: {}".format(i+1, translator[c]))
            temp_letters.append(translator[c])
        
        for l in temp_letters:
            for word, freq in frequency_table.items():
                if l.lower() in word:
                    print("PARTIAL MATCH: {}/{}".format(word, freq))
        

