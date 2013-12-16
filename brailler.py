class Brailler(object):
    """
    Utility class to convert English text into Braille using the English Braille system.
    """

    def __init__(self, text=None):
        """
        Create a new instance with the default configuration settings
        """
        if text is None:
            text = ""
        self.text = text
        self.abc = "abcdefghijklmnopqrstuvwxyz\t"
        self.base  = \
        ["O.....", "O.O...", "OO....", "OO.O..", "O..O..", 
        "OOO...", "OOOO..", "O.OO..", ".OO...", ".OOO..",
        "O...O.", "O.O.O.", "OO..O.", "OO.OO.", "O..OO.",
        "OOO.O.", "OOOOO.", "O.OOO.", ".OO.O.", ".OOOO.",
        "O...OO", "O.O.OO", ".OOO.O", "OO..OO", "OO.OOO",
        "O..OOO", "\t"*6]
        self.basedict  = self.newdict("O", ".")
        self.baselabel = "the English Braille system"
        self.leftjust  = True
        self.delimchar = " "
        self.padlen    = 2
        self.braille   = None

    def pad(self, string, length=self.padlen, delim=self.delimchar):
        """Take a string and add a specified character every n'th index

           Keyword arguments:
           `string` -- String to apply the pad operation on.
           `length` -- Interval in which to add the `delim` character.
           `delim`  -- Character to use as the padder, defaults to a space.

        """
        return delim + delim.join(string[i:i + length]\
             for i in range(0,len(string),length)) + delim

    def setdict(raised=self.raised, lowered=self.lowered):
        """
        Set the default dictionary to use for translations.
        """
        pass

    def newdict(raised, lowered, bmap=self.basedict):
        """
        Return a list of English Braille representations of A-Z
        """
        return {k:v for (k, v) in \
                zip(self.abc, [x.replace("O", raised).replace(".", lowered) for x in bmap])}

    def print(self, *args, label=False):
        """Print out the English Braille representation. Equivalent to the str() method.

           Keyword arguments:
           `*args`  -- Each argument will be printed below the `label`, and above the braille.
           `label`  -- `True` to print an explanation or title string.

        """
        if self.braille is None:
            return None
        if label:
            print("Translating '", self.text, "' to braille, with ", lname, sep='')
        if args:
            for line in ["".join(x) for x in args]:
               print(line)
        print("{0:3}".format(pad("".join(r1), delim=delimchar)), 
              "{0:3}".format(pad("".join(r2), delim=delimchar)), 
              "{0:3}".format(pad("".join(r3), delim=delimchar)), 
              "{0:3}".format(pad("".join(r4), delim=delimchar)), 
              sep="\n", end="\n\n")

    def get_braille(sentence, *args, bmap=self.basedict, 
                    delimchar=self.delimchar, lname=self.baselabel, 
                    ljust=self.leftjust):
        """Get the English Braille representation of a string.

           Keyword arguments:
           `sentence`  -- The string to translate into braille.
           `*args`     -- Additional text that you wish to display above the 
                          tranlated braille.
           `bmap`      -- This is the 'Braille Map' to be used for the braille
                          representation. If none is passed, a new one is created
                          using "O" for raised and "." for lowered characters.
           `delimchar` -- The character placed in between each letter. This character
                          will essentially "frame" the braille. Default is " ".
           `ljust`     -- Left justify the characters above the braille.

        """
        r1, r2, r3, r4 = [], [], [], []
        # Remove all non alpha numbers or spaces
        sentence = re.sub(r'[^A-Za-z\s]', "", sentence).rstrip()
        for idx, c in enumerate(sentence.lower()):
           if ljust:
               r1+=sentence[c]+" "
           else:
               r1+=" "+sentence[c]
           translated = re.findall('..', bmap[c])
           r2+=translated[0]
           r3+=translated[1]
           r4+=translated[2]
        self.braille = r1, r2, r3, r4
