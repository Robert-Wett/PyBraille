import re
from colorama import *
init()

#               _   _   _              __ 
#              | | | | | |            / _|
# __      _____| |_| |_| | ___   __ _| |_ 
# \ \ /\ / / _ \ __| __| |/ _ \ / _` |  _|
#  \ V  V /  __/ |_| |_| | (_) | (_| | |  
#   \_/\_/ \___|\__|\__|_|\___/ \__,_|_|  
#                                         
#                                         


class Brailler(object):
    """
    Utility class to convert English text into Braille using the English Braille system.
    """

    def __init__(self, text=None, print=False):
        """
        Create a new instance with the default configuration settings
        """
        if text is None:
            text = "Braille"

        self.text = text
        self.abc = "abcdefghijklmnopqrstuvwxyz "
        self.base  = \
        ["O.....", "O.O...", "OO....", "OO.O..", "O..O..", 
        "OOO...", "OOOO..", "O.OO..", ".OO...", ".OOO..",
        "O...O.", "O.O.O.", "OO..O.", "OO.OO.", "O..OO.",
        "OOO.O.", "OOOOO.", "O.OOO.", ".OO.O.", ".OOOO.",
        "O...OO", "O.O.OO", ".OOO.O", "OO..OO", "OO.OOO",
        "O..OOO", "      "]
        self.basedict  = self.newdict("O", ".") 
        self.baselabel = "the English Braille system"
        self.leftjust  = True
        self.delim     = " "
        self.padlen    = 2
        self.braille   = self.tobraille(self.text, isinit=True, print=print)
        # We'll go christmas motif
        self.f      = Fore.BLACK
        self.b      = Back.YELLOW


    # def pad(self, string, length=self.padlen, delim=self.delim):
    def pad(self, string, delim=None):
        """
        Take a string and add a specified character every n'th index
        """
        if delim is None:
            delim = self.delim

        return delim + delim.join(string[i:i + self.padlen]\
             for i in range(0,len(string),self.padlen)) + delim


    def setdict(self, raised, lowered, update=True):
        """
        Set the default dictionary to use for translations.
        """
        self.basedict = self.newdict(raised, lowered)
        if update:
            self.tobraille(print=False)


    def newdict(self, raised, lowered):
        """
        Return a list of English Braille representations of A-Z
        """
        return {k:v for (k, v) in \
                zip(self.abc, [x.replace("O", raised). \
                    replace(".", lowered) for x in self.base])}


    def str(self, delim=None):
        """
        Print out the English Braille representation. Equivalent to the str() method.
        """
        if self.braille is None:
            return None
        if delim is None or (len(delim) != 1):
            delim = self.delim
        # print("{0:3}".format(self.pad("".join(self.braille[0]), delimchar=self.delim)), 
        for idx, row in enumerate(self.braille):
            if idx in [0, 1]:
                print(self.f+self.b+ "{0:2}".format(self.pad("".join(row), delim=" ")))
            else:
                print(Fore.RESET+Back.RESET+ "{0:2}".format(self.pad("".join(row), delim)))
        print("\n")

    def tobraille(self, sentence=None, bmap=None, isinit=False,
                    delim=None, ljust=None, print=True):
        """Get the English Braille representation of a string.

           Keyword arguments:
           `sentence`  -- The string to translate into braille.
           `bmap`      -- This is the 'Braille Map' to be used for the braille
                          representation. If none is passed, a new one is created
                          using "O" for raised and "." for lowered characters.
           `isinit`    -- True is passed on object initialization
           `delim`     -- The character to use as a delimiter
           `ljust`     -- Left justify the characters above the braille.
           `print`     -- Call self.str on the current sentence

        """
        if bmap is None:
            if self.basedict is None:
                print("No dictionary set.")
                pass
            bmap = self.basedict
        if sentence is None:
            if self.text is None:
                print("No text to braille!")
                pass
            sentence = self.text
        if ljust is None:
            ljust = self.leftjust
        self.leftjust = ljust
        if delim is None:
            delim = self.delim
        self.delim = delim

        r1, r2, r3, r4, r5 = [], [], [], [], []
        # Remove all non alpha numbers or spaces
        sentence = re.sub(r'[^A-Za-z\s]', "", sentence).rstrip()
        self.text = sentence

        for idx, c in enumerate(sentence.lower()):
            if ljust:
                r1.append("%s " % sentence[idx])
            else:
                r1.append(" %s" % sentence[idx])
            translated = re.findall('..', bmap[c])
            # Don't add underscores if it's a space
            if bmap[c] == "      ":
                r2.append("  ")
            else:
                r2.append("__")
            r3.append(translated[0])
            r4.append(translated[1])
            r5.append(translated[2])
        if isinit:
            return r1, r2, r3, r4, r5
        else:
            self.braille = r1, r2, r3, r4, r5
        if print: 
            self.str(delim=delim)
