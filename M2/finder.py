def finder(word, text):
    """
    Find a string another string.

    It answer the question: are the characters comprising the first string
    hidden inside the second string?
    """
    word = word.lower()
    text = text.lower()
    # find index of first letter of word in text
    # then take second letter and find index from substring <-repeat
    it_contains = True
    start = 0

    for l in word:
        i = text.find(l, start)
        if i != -1:
            start = i + 1
        else:
            it_contains = False
            break

    return it_contains

if finder("dog", "vcxzxdcybfdstbywuefsas"):
    print("It's there")
else:
    print("No")

