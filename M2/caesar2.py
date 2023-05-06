def caesar(text, shift):
    """Caesar cipher.
    
    - Preserve the letters' case.
    - All non-alphabetical characters remain untouched.
    
    keyword arguments:
    text -- the string to encode
    shift -- an integer number from the range 1..25 
    """
    if shift not in range (1, 26):
        return "Shift value must be in the range 1..25"
    cipher = ''
    for char in text:
        if char.isalpha():
           cp = ord(char) 
           new = cp + shift 
           if char.isupper() and new > 90: 
              # A-Z -> 65-90
              new = new % 65 - 25
              new = 64 + new
           if char.islower() and new > 122: 
              # a-z -> 97-122
              new = new % 97 - 25
              new = 96 + new
           char = chr(new)
        cipher += char
    return cipher

import unittest

class CaesarTest(unittest.TestCase):
    def test_caesar_with_small_shift(self):
        text = "abcxyzABCxyz 123"
        shift = 2

        result = caesar(text, shift)

        self.assertEqual(result, "cdezabCDEzab 123")

    def test_caesar_with_largest_shift(self):
        text = "The die is cast"
        shift = 25

        result = caesar(text, shift)

        self.assertEqual(result, "Sgd chd hr bzrs")

if __name__ == "__main__":
    #unittest.main()
    text = input("Enter your message: ")
    shift = int(input("Enter the shif: "))
    print(caesar(text, shift))