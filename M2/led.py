patterns = [["###","# #","# #","# #","###"], [" # "," # "," # "," # ", " # "],
            ["###","  #","###","#  ","###"], ["###","  #","###","  #","###"],
            ["# #", "# #","###", "  #", "  #"], ["###", "#  ", "###", "  #", "###"],
            ["###", "#  ", "###", "# #", "###"], ["###", "  #",  "  #","  #","  #"], 
            ["###", "# #", "###", "# #", "###"], ["###", "# #", "###", "  #",  "  #"]]

def display_led(numbers):
    """
    a program which is able to simulate the work of a seven-display device
    """
    for i in range(0, 5):
        for number in numbers:
            print(patterns[int(number)][i], end=" ")
        print("\n")

display_led("0123456789")
display_led("123")