def is_palindrome(text):
    """Checks whether a given text is a palindrome(True) or not(false)."""
    text = text.replace(" ", "")
    text = text.lower()

    # first find the middle of the word
    lenght = len(text)  
    middle = int(lenght / 2)
    
    first_part = text[:middle]
    second_part = text[middle:lenght]     
    if lenght % 2 != 0:        
        first_part = text[:middle]
        second_part = text[middle+1:lenght] 

    #loop and compare both ends
    #print(f" > {first_part} {second_part} <")
    palindrome = True
    left_index = 0
    right_index = 1
    for _ in range(len(first_part)):    
        if first_part[left_index] != second_part[-right_index]:
            palindrome = False
            break
        left_index += 1
        right_index += 1

    return palindrome 

import unittest


class PalindromeTestCase(unittest.TestCase):
    def test_with_long_palindrome(self):
        text = "Ten animals I slam in a net"

        result = is_palindrome(text)

        self.assertTrue(result)

    def test_with_long_not_palindrome(self):
        text = "Eleven animals I slam in a net"

        result = is_palindrome(text)

        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()

    text = "kawywak"
    if is_palindrome(text):
        print("It's a palindrome")
    else:
        print("It's not a palindrome")