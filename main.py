#cdr must be decimal value from 0.00 -> 1.00
def cdrToAh(cdr):
    return 100 * ((1/(1-cdr)) - 1)


def ahToCdr(ah):
    return  1 - (1/(1+(ah/100)))

loop = True

while loop:
    choice = input("Type x to calculate cdr; y to calculate ah ")
    if choice == 'x':
        ah = int(input("Enter your ability haste "))
        print(ahToCdr(ah) * 100, '% cdr')
    elif choice == 'y':
        cdr = float(input("Enter your cdr ")) * 0.01
        print(cdrToAh(cdr), 'ability haste')
    else:
        print("Error. Invalid choice ")


