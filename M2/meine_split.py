import unittest

def meinesplit(strng):
    if strng.isspace() or strng == '':
        return []
    strng = strng.strip()
    l = list()
   
    if strng.find(" ") == -1:
        l.append(strng)
        return l

    # handle cases where there is other than spaces or empty strings
    temp = ""
    for s in strng:
        if s.isspace():
            l.append(temp)
            temp = ""
        else:
            temp += s
    l.append(strng[(strng.rfind(' ') + 1):])       
        
    return l


class SplitTestCase(unittest.TestCase):
    def test_complex1(self):
        str = "To be or not to be, that is the question"
        result = meinesplit(str)
        self.assertEqual(result, ['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question'])

    def test_complex2(self):
        str = "To be or not to be,that is the question"
        result = meinesplit(str)
        self.assertEqual(result, ['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question'])

    def test_whitespaces(self):
        str = "   "
        result = meinesplit(str)
        self.assertEqual(result, [])

    def test_leading_and_traling_spaces(self):
        str = " abc "
        result = meinesplit(str)
        self.assertEqual(result, ['abc'])

    def test_empty_string(self):
        str = ""
        result = meinesplit(str)
        self.assertEqual(result, [])    

if __name__ == "__main__":
    unittest.main()
