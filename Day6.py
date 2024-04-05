# Design a Python program to execute division on two predefined numbers, while considering the possibility of a division by zero error. Ensure that the program handles this exception gracefully, providing a clear error message in such cases.

# Output:
# Error: Division by zero is not allowed.

# Explanation:
# The program takes two predetermined numbers and attempts to perform division. A try-except mechanism is implemented to catch and manage the ZeroDivisionError if the denominator is zero. In the event of such an error, the program displays a clear and informative message indicating that division by zero is not allowed.

dividend = int(input("Enter dividend:"))
divisor = int(input("Enter divisor:"))

try:
    output = dividend/divisor
    print(f"The quotient is {output}" )

except:
    if(divisor==0):
        print("Error: Division by zero is not allowed.")
