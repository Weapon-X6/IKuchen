'''
simple method allowing you to input a line filled with numbers, and to process them easily. 
Note: the routine input() function, combined together with the int() or float() functions, 
is unsuitable for this purpose.
'''
def string2float():
    line = input("Enter a line of numbers - separate them with spaces: ")
    strings = line.split()
    total = 0
    try:
        for substr in strings:
            total += float(substr)
        print("The total is:", total)
    except:
        print(substr, "is not a number.")

if __name__ == "__main__":
    string2float()