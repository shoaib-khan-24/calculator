import art
print(art.logo)

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+":add ,
    "-":subtract ,
    "*":multiply ,
    "/":divide,
}

start_over = False
first_number = int(input("Enter the first number: "))
while True:
    if start_over:
        print(art.logo)
        first_number = int(input("Enter the first number: "))
    print("+\n-\n*\n/")
    current_operator = input("Pick an operation you want to apply: ")
    second_number = int(input("Enter the second number:  "))

    result = operations[current_operator](first_number , second_number)
    print(f"{first_number} {current_operator} {second_number} = {result}")
    quit_calculator = input("\nTo quit the calculator, press Q.\nOtherwise press any random key:\n")
    if quit_calculator == "Q":
        print("Exiting the calculator.")
        break

    choice = input(f"\nDo you wanna continue with the previous result {result}? yes or no: ")
    if choice == "yes":
        first_number = result
        start_over = False
    elif choice == "no":
        print("\n"*25)
        start_over = True



