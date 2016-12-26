import unittest

CLUE_1 = ('k', 'm')
CLUE_2 = ('o', 'q')
CLUE_3 = ('e', 'g')
CIPHER_TEXT = ("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq "
               "ypc dmp. bmgle  gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw "
               "rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. "
               "lmu ynnjw ml rfc spj.")
CIPHER = 2
MIN_ASCII = 97
MAX_ASCII = 121
ASCII_REDUCE = 26

# Not moved to lib/functions.py as str.maketrans() is preferred
def decipherChar(char):
    """
    Return the deciphered value of a character
    """
    ord_value = ord(char)
    if ord_value < MIN_ASCII:
        return char
    if ord_value >= MAX_ASCII:
        ord_value = ord_value - ASCII_REDUCE
    return chr(ord_value  + CIPHER)

# Not moved to lib/functions.py as str.maketrans() is preferred
def decipherString(input):
    """
    Return the deciphered String
    """
    char_list = []
    for char in input:
        char_list.append(decipherChar(char))
    return ''.join(char_list)

class TestFixture(unittest.TestCase):

    def test_getOrdinalValue(self):
        # http://www.asciitable.com/
        self.assertEqual(107, ord(CLUE_1[0]))
        self.assertEqual(111, ord(CLUE_2[0]))
        self.assertEqual(101, ord(CLUE_3[0]))

    def test_ordinalDifference(self):
        self.assertEqual(-2, ord(CLUE_1[0]) - ord(CLUE_1[1]))
        self.assertEqual(-2, ord(CLUE_2[0]) - ord(CLUE_2[1]))
        self.assertEqual(-2, ord(CLUE_3[0]) - ord(CLUE_3[1]))

    def test_decipherChar(self):
        self.assertEqual(CLUE_1[1], decipherChar(CLUE_1[0]))
        self.assertEqual(CLUE_2[1], decipherChar(CLUE_2[0]))
        self.assertEqual(CLUE_3[1], decipherChar(CLUE_3[0]))

    def test_decipherCharEdgeCases(self):
        self.assertEqual('a', decipherChar('y'))
        self.assertEqual('b', decipherChar('z'))
        self.assertEqual('c', decipherChar('a'))

    def test_skipCharacters(self):
        self.assertEqual(' ', decipherChar(' '))
        self.assertEqual('.', decipherChar('.'))
        self.assertEqual('\'', decipherChar('\''))
        self.assertEqual('(', decipherChar('('))
        self.assertEqual(')', decipherChar(')'))

    def test_decipherString(self):
        self.assertEqual('jam', decipherString('hyk'))
        self.assertEqual('toast', decipherString('rmyqr'))
        self.assertEqual('stuff.call()', decipherString('qrsdd.ayjj()'))

    def test_decipherText(self):
        assertionText = ("i hope you didnt translate it by hand. thats what "
                         "computers are for. doing  it in by hand is inefficient "
                         "and that's why this text is so long. using "
                         "string.maketrans() is recommended. now apply on the url.")
        self.assertEqual(assertionText, decipherString(CIPHER_TEXT))

if __name__ == '__main__':
    unittest.main()
