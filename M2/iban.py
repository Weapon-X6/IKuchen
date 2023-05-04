# IBAN Validator.

def check_iban(iban):
    """Validate an iban, return wheter is valid(True) or not(False).
    
    Keyword arguments:
    iban -- a string
    """
    is_valid = False
    iban = iban.replace(' ','')

    if not iban.isalnum():
        print("You have entered invalid characters.")
    elif len(iban) < 15:
        print("IBAN entered is too short.")
    elif len(iban) > 31:
        print("IBAN entered is too long.")
    else:
        iban = (iban[4:] + iban[0:4]).upper()
        iban2 = ''
        for ch in iban:
            if ch.isdigit():
                iban2 += ch
            else:
                iban2 += str(10 + ord(ch) - ord('A'))
        iban = int(iban2)
        if iban % 97 == 1:
            print("IBAN entered is valid.")
            is_valid = True
        else:
            print("IBAN entered is invalid.")
    return is_valid

import unittest

class IbanTestCase(unittest.TestCase):
    def test_british_iban_is_correct(self):
        iban = "GB72 HBZU 7006 7212 1253 00"
        result = check_iban(iban)
        self.assertTrue(result)

    def test_french_iban_is_correct(self):
        iban = "FR76 30003 03620 00020216907 50"
        result = check_iban(iban)
        self.assertTrue(result)

    def test_german_iban_is_correct(self):
        iban = "DE02100100100152517108"
        result = check_iban(iban)
        self.assertTrue(result)

if __name__ == "__main__":
    #unittest.main()
    iban = input("Enter IBAN, please: ")    
    check_iban(iban)