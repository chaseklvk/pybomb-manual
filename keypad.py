def run(args):
    # Q A L Z CAT H BACKC FRONTC EURO PHI STAR ? COPY W K R 6 PARA BT SMILE AE # PSI N OMEGA
    print("Symbol Options: Q A L Z CAT H BACKC FRONTC E EURO PHI CSTAR FSTAR ? COPY W K R 6 PARA BT SMILE AE # PSI N OMEGA")
    symbols = input("Symbols: ")

    col_1 = ["Q", "A", "L", "Z", "CAT", "H", "BACKC"]
    col_2 = ["EURO", "Q", "BACKC", "PHI", "CSTAR", "H", "?"]
    col_3 = ["COPY", "W", "PHI", "K", "R", "L", "CSTAR"]
    col_4 = ["6", "PARA", "BT", "CAT", "K", "?", "SMILE"]
    col_5 = ["PSI", "SMILE", "BT", "FRONTC", "PARA", "E", "FSTAR"]
    col_6 = ["6", "EURO", "#", "AE", "PSI", "N", "OMEGA"]

    cols = [col_1, col_2, col_3, col_4, col_5, col_6]

    symbol_list = symbols.split(" ")
    for col in cols: 
        for i, symb in enumerate(symbol_list):
            if symb not in col:
                break
            elif i == len(symbol_list) - 1:
                print("===SYMBOL ORDER===")
                for s in col:
                    if s in symbol_list:
                        print(s)
                break

        


