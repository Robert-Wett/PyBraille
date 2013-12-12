import sys
import re

alphabet = "abcdefghijklmnopqrstuvwxyz "
space = "      "

braille_data = \
["O.....", "O.O...", "OO....", "OO.O..", "O..O..", 
"OOO...", "OOOO..", "O.OO..", ".OO...", ".OOO..",
"O...O.", "O.O.O.", "OO..O.", "OO.OO.", "O..OO.",
"OOO.O.", "OOOOO.", "O.OOO.", ".OO.O.", ".OOOO.",
"O...OO", "O.O.OO", ".OOO.O", "OO..OO", "OO.OOO",
"O..OOO", space]


# Add a couple other lists to build a dictionary/lookup with
# TODO: Generate lists based on a char for raised and a char
#       for lowered.
poundlabel="'#' for raised, '.' for lowered"
braille_pound = \
["#.....", "#.#...", "##....", "##.#..", "#..#..", 
"###...", "####..", "#.##..", ".##...", ".###..",
"#...#.", "#.#.#.", "##..#.", "##.##.", "#..##.",
"###.#.", "#####.", "#.###.", ".##.#.", ".####.",
"#...##", "#.#.##", ".###.#", "##..##", "##.###",
"#..###", space]

binlabel="'1' for raised and '0' for lowered"
braille_binary = \
["100000", "101000", "110000", "110100", "100100", 
"111000", "111100", "101100", "011000", "011100",
"100010", "101010", "110010", "110110", "100110",
"111010", "111110", "101110", "011010", "011110",
"100011", "101011", "011101", "110011", "110111",
"100111", space]

lookup   = {k:v for (k, v) in zip(alphabet, braille_data)}
lookup_p = {k:v for (k, v) in zip(alphabet, braille_pound)}
lookup_b = {k:v for (k, v) in zip(alphabet, braille_binary)}
def pad(string, length=2, delim=' '):
    """ Take a string and add a specified character every nth index """
    return delim+delim.join(string[i:i+length] for i in range(0,len(string),length))+delim

def get_braille(sentence, used):
    sentence = re.sub(r'[^A-Za-z\s]', "", sentence).rstrip()
    r1, r2, r3, r4, r5 = [], [], [], [], []
    for idx, c in enumerate(sentence.lower()):
       r1+=sentence[idx]+" "
       translated = re.findall('..', lookup[c])
       r2+=translated[0]
       r3+=translated[1]
       r4+=translated[2]
       r5+="--"
    delimchar=" "
    print("")
    print(pad("".join(r1), delim=delimchar)) 
    print(pad("".join(r5), delim=delimchar)) 
    print(pad("".join(r2), delim=delimchar)) 
    print(pad("".join(r3), delim=delimchar)) 
    print(pad("".join(r4), delim=delimchar)) 

try:
    get_braille(sys.argv[1], sys.argv[2])
except:
    try:
        get_braille(sys.argv[1])
    except:
        get_braille("I CANT SEE")