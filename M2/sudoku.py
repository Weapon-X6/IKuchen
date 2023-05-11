def check_digits(sudorow):
    if len(sudorow) > 9:
        return False

    has_all_digits = True
    for n in range(1,10):
        if str(n) not in sudorow:
            has_all_digits = False
            break
    return has_all_digits

def check_tiles(sudosubrows):
    n1 = ""
    n2 = ""
    n3 = ""
    for r in sudosubrows:
        n1 += r[:3]
        n2 += r[3:6]
        n3 += r[6:9]       

    if not check_digits(n1) or not check_digits(n2) or not check_digits(n3):
        return False   
    return True

def check_sudoku(sudoku):
    is_sudoku = True
    if len(sudoku) != 9:
        return

    # check digits in rows
    for r in sudoku:
        if not check_digits(r):
            is_sudoku = False
            break
       
    # check digits in columns
    columns = []
    for i in range(9):
        e = ""
        for j in sudoku:
            e += j[i]
        columns.append(e)
    for c in columns:
        if not check_digits(c):
            is_sudoku = False
            break

 
    tiles = []

    if not check_tiles(sudoku[:3]) \
        or not check_tiles(sudoku[3:6]) \
        or not check_tiles(sudoku[6:]):
        is_sudoku = False

    return is_sudoku

sudo = [
    "295743861",
    "431865927",
    "876192543",
    "387459216",
    "612387495",
    "549216738",
    "763524189",
    "928671354",
    "154938672"
]

not_sudo = [
    "195743862",
    "431865927",
    "876192543",
    "387459216",
    "612387495",
    "549216738",
    "763524189",
    "928671354",
    "254938671"
]

print(check_sudoku(sudo))
print(check_sudoku(not_sudo))