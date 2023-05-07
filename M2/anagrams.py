def is_anagram(text1, text2):
    """
    Checks if a given pair of texts are anagrams(True) or not(False).
    """
    text1 = text1.lower().replace(" ", "")
    text2 = text2.lower().replace(" ", "")

    if len(text1) != len(text2) or len(text1) == 0 or len(text2) == 0:
        return False
   
    for i in range(len(text1)):
        text2 = text2.replace(text1[i], "")

    if len(text2) == 0:
        return True
    

if is_anagram("", ""):
    print("Anagrams")
else:
     print("Not")