import random as rd

maxLines = 3
maxBet = 100
minBet = 1

rows = 3
cols = 3

symbol_count = {
    "A": 10,
    "B": 8,
    "C": 6,
    "D": 4,
    "E": 3,

}

def checkWinnings(columns, lines, bet, values):
    winnings = 0
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbolToCheck = column[line]
            if symbolToCheck != symbol:
                break
        else:
            winnings += values[symbol] * bet
    return winnings

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
        
    return columns
        
def printSlotMachine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end= " | ")
            else:
                print(column[row], end="")

        print()    
        

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

    slots = getSlotMachineSpin(rows, cols, symbol_count)
    printSlotMachine(slots)
    winnings = checkWinnings(slots, lines, bet, symbol_count)
    print(f"You won ${winnings}")

main()