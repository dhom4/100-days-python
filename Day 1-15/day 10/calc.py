import art
print(art.logo)

def add(n1, n2):
    return n1 + n2
# TODO-1: sub, multiply
def sub(n1, n2):
    return n1 - n2
def mult(n1, n2):
    return n1 * n2
# TODO-2: division
def div(n1, n2):
    if n2 == 0:
        return "try agin"
    return n1 / n2

operations = {
     "+" : add,
     "-" :sub ,
     "*" : mult ,
     "/" : div
}

while True:
    num1 = float(input("the first number: "))

    should_accoumlate = True
    while should_accoumlate:
        for sym in operations:
            print(sym)
        operation_symbol = input("type a mathematical operator: ")
        num2 = float(input("the second number: "))

        '''actully without this you would go through alot of if's, it is good kinda'''
        result = operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")


        choice = input(f"Type 'y' to continue wiht {result} or 'n' to start restart: ")
        if choice == 'y':
            num1 = result
        else:
            should_accoumlate = False
            print("\n" * 20)
