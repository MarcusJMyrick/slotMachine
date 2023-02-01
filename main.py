maxLines = 3

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a positive number.")
        else:
            print("Please enter a number.")

    return amount

def getNumberOfLines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(maxLines) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= maxLines:
                break
            else:
                print("Please enter a valid number if lines.")
        else:
            print("Please enter a number.")

    return lines


def main():
    balance = deposit()
    lines = getNumberOfLines()
    print(balance, lines)

main()