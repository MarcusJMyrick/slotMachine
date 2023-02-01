import random as rd

maxLines = 3
maxBet = 100
minBet = 1

rows = 3
cols = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
    "E": 10,

}

def getSlotMachineSpin(rows, cols, symbols):
    allSymbols = []
    for symbol, symbol_count in symbols.items():
        for i in range(symbol_count):
            allSymbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        currentSymbols = allSymbols[:]
        for _ in range(rows):
            value = rd.choice(allSymbols)
            currentSymbols.remove(value)
            column.append(value)
        
        columns.append(column)
        
def printSlotMachine(columns):
    

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

def getBet():
    while True:
        amount = input("What would you like to bet? $ ")
        if amount.isdigit():
            amount = int(amount)
            if minBet <= amount <= maxBet:
                break
            else:
                print(f"amount must be between. ${minBet} - ${maxBet}.")
        else:
            print("Please enter a number.")

    return amount

def main():
    balance = deposit()
    lines = getNumberOfLines()
    while True:
        bet = getBet()
        total = lines * bet

        if total > balance:
            print(f"Your total bet is ${total}. You only have ${balance}. Please enter a valid bet.")
        else:
            balance -= total
            break
    print(F"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total}")


main()