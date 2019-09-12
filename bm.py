import sys
import simple_wires as sw
import button as bt
import keypad as kp
import simon as sn
import wordpad as wp
import memory as mem
import morse as ms
import led_wires as ledw
import wire_sequence as ws
import password as pw
import knob as kb

if __name__ == '__main__':
    vowel = bool(int(input("Does serial number contain a vowel? ")))
    last_digit = input("Is last digit or serial number odd or even? ")
    parallel_port = bool(int(input("Is there a parallel port? ")))
    num_batteries = int(input("Number of batteries: "))
    args = {
        'last_digit': last_digit,
        'vowel': vowel,
        'num_batteries': num_batteries,
        'parallel_port': parallel_port
    }

    while True:
        print("Module Options: Simple Wires (SW), Button (BT), Keypad (KP), Simon (SN), Wordpad (WP),")
        print("Memory (MEM), Morse (MS), LED Wires (LED), Wire Sequence (WS), Password (PW), Knob (KB)")
        module = input("Module: ")

        if module == 'q': break

        if module == 'sw':
            sw.run(args)
        elif module == 'bt':
            bt.run(args)   
        elif module == 'kp':
            kp.run(args)
        elif module == 'sn':
            sn.run(args)
        elif module == 'wp':
            wp.run(args)
        elif module == 'mem':
            mem.run(args)
        elif module == 'ms':
            ms.run(args)
        elif module == 'led':
            ledw.run(args)
        elif module == 'ws':
            ws.run(args)
        elif module == 'pw':
            pw.run(args)
        elif module == 'kb':
            kb.run(args)

