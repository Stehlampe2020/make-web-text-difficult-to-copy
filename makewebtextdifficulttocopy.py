try:
    print("This is NOT a way to fully copy-proof any text!\nThis tool does just convert the letters of the input text to <span>s with calls to pictures of letters. That helps to prevent Ctrl+A-Ctrl+C-Ctrl+V copying attacks.", end="\n")

    """
    This helpful tool was coded by Christian Lampe <kontakt@lampe2020.de> in January 2022.
    """

    import os
    import sys

    open("./.inputtext", "x")
    input("I created the file \".inputtext\" for you in the directory you run this tool in, please put your text in there and press [ENTER] here to start processing the text.")
    inputfile = open("./.inputtext", "r")
    inputtext = inputfile.read()
    print("\nThe file \".inputtext\" contains the following text:\n\n" + inputtext)
    print("Closing and removing the file \".inputext\"...")
    inputfile.close()
    os.remove("./.inputtext")
    print("Computing: replacing every letter with its appropriate HTML code...")
    letterlist = list(inputtext)

    for index,item in enumerate(letterlist):
        if item == "a":
            letterlist[index] = '<span class="letter_small_a")></span>'
        if item == "b":
            letterlist[index] = '<span class="letter_small_b")></span>'
        if item == "c":
            letterlist[index] = '<span class="letter_small_c")></span>'
        if item == "d":
            letterlist[index] = '<span class="letter_small_d")></span>'
        if item == "e":
            letterlist[index] = '<span class="letter_small_e")></span>'
        if item == "f":
            letterlist[index] = '<span class="letter_small_f")></span>'
        if item == "g":
            letterlist[index] = '<span class="letter_small_g")></span>'
        if item == "h":
            letterlist[index] = '<span class="letter_small_h")></span>'
        if item == "i":
            letterlist[index] = '<span class="letter_small_i")></span>'
        if item == "j":
            letterlist[index] = '<span class="letter_small_j")></span>'
        if item == "k":
            letterlist[index] = '<span class="letter_small_k")></span>'
        if item == "l":
            letterlist[index] = '<span class="letter_small_l")></span>'
        if item == "m":
            letterlist[index] = '<span class="letter_small_m")></span>'
        if item == "n":
            letterlist[index] = '<span class="letter_small_n")></span>'
        if item == "o":
            letterlist[index] = '<span class="letter_small_o")></span>'
        if item == "p":
            letterlist[index] = '<span class="letter_small_p")></span>'
        if item == "q":
            letterlist[index] = '<span class="letter_small_q")></span>'
        if item == "r":
            letterlist[index] = '<span class="letter_small_r")></span>'
        if item == "s":
            letterlist[index] = '<span class="letter_small_s")></span>'
        if item == "t":
            letterlist[index] = '<span class="letter_small_t")></span>'
        if item == "u":
            letterlist[index] = '<span class="letter_small_u")></span>'
        if item == "v":
            letterlist[index] = '<span class="letter_small_v")></span>'
        if item == "w":
            letterlist[index] = '<span class="letter_small_w")></span>'
        if item == "x":
            letterlist[index] = '<span class="letter_small_x")></span>'
        if item == "y":
            letterlist[index] = '<span class="letter_small_y")></span>'
        if item == "z":
            letterlist[index] = '<span class="letter_small_z")></span>'
        if item == "A":
            letterlist[index] = '<span class="letter_capital_a")></span>'
        if item == "B":
            letterlist[index] = '<span class="letter_capital_b")></span>'
        if item == "C":
            letterlist[index] = '<span class="letter_capital_c")></span>'
        if item == "D":
            letterlist[index] = '<span class="letter_capital_d")></span>'
        if item == "E":
            letterlist[index] = '<span class="letter_capital_e")></span>'
        if item == "F":
            letterlist[index] = '<span class="letter_capital_f")></span>'
        if item == "G":
            letterlist[index] = '<span class="letter_capital_g")></span>'
        if item == "H":
            letterlist[index] = '<span class="letter_capital_h")></span>'
        if item == "I":
            letterlist[index] = '<span class="letter_capital_i")></span>'
        if item == "J":
            letterlist[index] = '<span class="letter_capital_j")></span>'
        if item == "K":
            letterlist[index] = '<span class="letter_capital_k")></span>'
        if item == "L":
            letterlist[index] = '<span class="letter_capital_l")></span>'
        if item == "M":
            letterlist[index] = '<span class="letter_capital_m")></span>'
        if item == "N":
            letterlist[index] = '<span class="letter_capital_n")></span>'
        if item == "O":
            letterlist[index] = '<span class="letter_capital_o")></span>'
        if item == "P":
            letterlist[index] = '<span class="letter_capital_p")></span>'
        if item == "Q":
            letterlist[index] = '<span class="letter_capital_q")></span>'
        if item == "R":
            letterlist[index] = '<span class="letter_capital_r")></span>'
        if item == "S":
            letterlist[index] = '<span class="letter_capital_s")></span>'
        if item == "T":
            letterlist[index] = '<span class="letter_capital_t")></span>'
        if item == "U":
            letterlist[index] = '<span class="letter_capital_u")></span>'
        if item == "V":
            letterlist[index] = '<span class="letter_capital_v")></span>'
        if item == "W":
            letterlist[index] = '<span class="letter_capital_w")></span>'
        if item == "X":
            letterlist[index] = '<span class="letter_capital_x")></span>'
        if item == "Y":
            letterlist[index] = '<span class="letter_capital_y")></span>'
        if item == "Z":
            letterlist[index] = '<span class="letter_capital_z")></span>'
        if item == "\n":
            letterlist[index] = '<span class="item_newline")></span>'
        if item == "\t":
            letterlist[index] = '<span class="item_tab")></span>'
        else:
            pass
    
    outputtext = '',join(letterlist)

    print("Now the text is fully converted to hard-to-copy-as-text html code. You can copy it from below into your html file, note: please remove the single quotes from the beginning and end of the text below before posting! The CSS file needed to show the text as text can be found on https://github.com/Stehlampe2020/MakeWebTextDifficultToCopy, together with this program.\n\n" + outputtext + "\n\nNow the text is fully converted to hard-to-copy-as-text html code. You can copy it from above into your html file, note: please remove the single quotes from the beginning and end of the text above before posting! The CSS file needed to show the text as text can be found on https://github.com/Stehlampe2020/MakeWebTextDifficultToCopy, together with this program.")

except KeyboardInterrupt:
    print("\n\nExecution was cancelled by a KeyboardInterrupt!\n\n")
    os.remove("./.inputtext")
    pass
