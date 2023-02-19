patterns = ["###\n# #\n# #\n# #\n###", 
            "#\n#\n#\n#\n#\n#", "###\n  #\n###\n#  \n###", "###\n  #\n###\n  #\n###",
            "# #\n# #\n###\n  #\n  #", "###\n#  \n###\n  #\n###", "###\n#  \n###\n# #\n###",
            "###\n  #\n  #\n  #\n  #", "###\n# #\n###\n# #\n###", "###\n# #\n###\n  #\n  #"]

def display_led(str):
    for n in str:
        print(patterns[int(n)])

display_led("123")