def digit_of_life(birthday):
    """Calculates the digit of life. 

    key arguments:
    - birthday: represented in the format "YYYYMMDD"
    """
    digit = 0
    for n in birthday:
        digit += int(n)

    while digit > 9:
        new_digit = 0
        for i in str(digit):
            new_digit += int(i)
        digit = new_digit

    return digit

if __name__ == "__main__":
    # digit_of_life("19880520") 
    # digit_of_life("20011012") 
    b = input("Enter birthday(YYYYMMDD): ")
    print(digit_of_life(b))

