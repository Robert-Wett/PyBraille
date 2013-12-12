class Brailler(object):
    """
    Utility class to convert English text into Braille using the English Braille system.
    """

    def __init__(self, text=None):
        """
        Create a new instance with the default configuration settings
        """
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

    def pad(string, length=self.padlen, delim=self.delimchar):
        """Take a string and add a specified character every n'th index

           Keyword arguments:
           `string` -- String to apply the pad operation on.
           `length` -- Interval in which to add the `delim` character.
           `delim`  -- Character to use as the padder, defaults to a space.

        """
        return delim + delim.join(string[i:i + length]\
             for i in range(0,len(string),length)) + delim

    def setdict(raised=self.raised, lowered=self.lowered, returndict=False):
        """
        Set the default dictionary to use for translations.
        """

        self.basedict = self.newdict(raised, lowered)
        if returndict:
            return self.basedict

    def newdict(raised, lowered):
        """
        Return a list of English Braille representations of A-Z
        """
        return {k:v for (k, v) in \
                zip(self.abc, [x.replace("O", raised).replace(".", lowered) for x in self.basemap])}

    def print(self, *args, delimlabel=False):
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
        for row in self.braille:
            print("{0:3}".format(pad("".join(row), delim=delimchar)))

    def get_braille(sentence=this.text, bmap=self.basedict, 
                    lname=self.baselabel, ljust=self.leftjust):
        """Get the English Braille representation of a string.

           Keyword arguments:
           `sentence`  -- The string to translate into braille.
           `bmap`      -- This is the 'Braille Map' to be used for the braille
                          representation. If none is passed, and no default map
                          is set then a new one is created
                          using "O" for raised and "." for lowered characters.
           `ljust`     -- Left justify the characters above the braille.

        """
        r1, r2, r3, r4 = [], [], [], []
        # Remove all non alpha numbers or spaces
        sentence = re.sub(r'[^A-Za-z\s]', "", sentence).rstrip()
        for idx, c in enumerate(sentence.lower()):
           if ljust:
               r1.append(sentence[c]+" ")
           else:
               r1.append(" "+sentence[c])
           translated = re.findall('..', bmap[c])
           r2.append(translated[0])
           r3.append(translated[1])
           r4.append(translated[2])
        self.braille = r1, r2, r3, r4
