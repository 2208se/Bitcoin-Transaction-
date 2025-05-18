# 3D Text Printer - Bitcoin Transaction
def print_3d_text(text):
    # 3D Alphabet Patterns (5-line format)
    alphabet = {
        'A': ["  A  ", " A A ", "AAAAA", "A   A", "A   A"],
        'B': ["#### ", "#   #", "##### ", "#   #", "#### "],
        'C': [" CCC ", "C    ", "C    ", "C    ", " CCC "],
        'D': ["DDDD ", "D   D", "D   D", "D   D", "DDDD "],
        'E': ["EEEEE", "E    ", "EEEEE", "E    ", "EEEEE"],
        'F': ["FFFFF", "F    ", "FFFF ", "F    ", "F    "],
        'G': [" GGG ", "G    ", "G GGG", "G   G", " GGG "],
        'H': ["H   H", "H   H", "HHHHH", "H   H", "H   H"],
        'I': [" III ", "  I  ", "  I  ", "  I  ", " III "],
        'J': ["  JJJ", "   J ", "   J ", "J  J ", " JJ  "],
        'K': ["K   K", "K  K ", "KK   ", "K  K ", "K   K"],
        'L': ["L    ", "L    ", "L    ", "L    ", "LLLLL"],
        'M': ["M   M", "MM MM", "M M M", "M   M", "M   M"],
        'N': ["N   N", "NN  N", "N N N", "N  NN", "N   N"],
        'O': [" OOO ", "O   O", "O   O", "O   O", " OOO "],
        'P': ["PPPP ", "P   P", "PPPP ", "P    ", "P    "],
        'Q': [" QQQ ", "Q   Q", "Q Q Q", "Q  Q ", " QQ Q"],
        'R': ["RRRR ", "R   R", "RRRR ", "R R  ", "R  RR"],
        'S': [" SSS ", "S    ", " SSS ", "    S", " SSS "],
        'T': ["TTTTT", "  T  ", "  T  ", "  T  ", "  T  "],
        'U': ["U   U", "U   U", "U   U", "U   U", " UUU "],
        'V': ["V   V", "V   V", "V   V", " V V ", "  V  "],
        'W': ["W   W", "W   W", "W W W", "WW WW", "W   W"],
        'X': ["X   X", " X X ", "  X  ", " X X ", "X   X"],
        'Y': ["Y   Y", " Y Y ", "  Y  ", "  Y  ", "  Y  "],
        'Z': ["ZZZZZ", "   Z ", "  Z  ", " Z   ", "ZZZZZ"],
        ' ': ["     ", "     ", "     ", "     ", "     "],  # Space
    }

    # Convert text to uppercase for consistent mapping
    text = text.upper()

    # Initialize lines to build the 3D text
    text_lines = [""] * 5

    for char in text:
        char_pattern = alphabet.get(char, ["?????"] * 5)  # Handle unsupported characters
        for i in range(5):
            text_lines[i] += char_pattern[i] + "  "  # Add space between letters

    # Print each line of the final 3D text
    for line in text_lines:
        print(line)


# Example Usage
text = "BITCOIN TRANSACTION"
print_3d_text(text)
