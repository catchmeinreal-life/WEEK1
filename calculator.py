def get_input():
    #fuction that gets user input; two integers and the operation  type.
    try:
        num1: int = input("ENTER num1: ")
        num2: int = input("ENTER NUM2: ")
        operation: str = input("TYPE OF OPERATION /,+,-,*: ")
    except ValueError:
        print("invalid input. Please enter valiid integers")
        return None, None, None
    return num1,num2,operation

def perform_operation(num1,num2,operation):
    #function performing operations depending  on thetype of inputed operation
    if operation  == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '**':
        return num1 ** num2
    elif  operation =='/':
        try:
            return num1 / num2
        except ZeroDivisionError:
            print("ERROR DIVISION BY ZERO")
            return None
    else:
        print("INVALID OPERATION. PLEASE ENTER ONE OF THE FOLLOWING OPERATIONS; +,-,*,/,** ")

def main():
    #main function to  run the calculator module
    num1,num2,operation = get_input()
    if num1 is  not None and num2  is  not None and operation is not None:
        result = perform_operation(num1,num2,operation)
        if result is  not None:
            print(f"the result of {num1}{operation}{num2}is:{result}")

if __name__ == "":
    main()