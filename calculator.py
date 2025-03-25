#ask the user for input

def get_input():
    #get two integers and an expression
    try:
        num1 = int(input("Enter num1: "))
        num2 = int(input("Enter num2: "))
        operation = input("Enter the operation: ")
    except ValueError:
        print("Invalid input. enter valid integers.")
        return None, None, None
    return num1, num2, operation
# print(get_input())

def perform_operation(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        try:
            return num1/num2
        except ZeroDivisionError:
            print(f"{num1} is not divisible by {num2}")
            return None
    else:
        print(f"{operation}: is invalid enter another opertation")
        
def main():
    # main function to run the program
    num1, num2, operation = get_input()
    if num1 is not None and num2 is not None and operation is not None:
        result = perform_operation(num1, num2, operation)
        if result is not None:
            print(f"{num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    main() 
