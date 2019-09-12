def run(args):
    up_table_1 = "001011111101"
    up_table_2 = "101010011011"
    down_table_1 = "011001111101"
    down_table_2 = "101010010001"
    left_table_1 = "000010100111"
    left_table_2 = "000010000110"
    right_table_1 = "101111111010"
    right_table_2 = "101100111010"

    sequence = input("Sequence: ")

    if sequence == 'q': return

    if sequence == up_table_1 or sequence == up_table_2:
        print("===ALIGN TO UP LABEL===")
    elif sequence == down_table_1 or sequence == down_table_2:
        print("===ALIGN OPPOSITE OF UP===")
    elif sequence == left_table_1 or sequence == left_table_2:
        print("===ALIGN LEFT OF UP===")
    elif sequence == right_table_1 or sequence == right_table_2:
        print("===ALIGN RIGHT OF UP===")