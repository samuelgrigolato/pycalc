def menu():
    print("### Menu ###")
    for idx, operation in enumerate(["Exit", "Sum", "Subtraction", "Multiplication", "Division"]):
        print(f"[{ idx }] - { operation }")

def calc():
    a = int(input("Value 1: "))
    b = int(input("Value 2: "))

    if (option == 1):
        print(a + b)
    elif (option == 2):
        print(a - b)
    elif (option == 3):
        print(a * b)
    elif (option == 4):
        print("Error" if b == 0 else a / b)

try:
    while (True):
        menu()
        option = int(input())
        if(option > 0 and option < 5):
            calc()
        else:
            break
except ValueError:
    print("Type only numbers!!!!!!!")