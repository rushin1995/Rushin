def add(a, b):  
    sum = a + b  
    print(a, "+", b, "=", sum)  
  
  
def subtract(a, b):  
    difference = a - b  
    print(a, "-", b, "=", difference)  
  
 
def multiply(a, b):  
    product = a * b  
    print(a, "x", b, "=", product)  
  
  
def divide(a, b):  
    division = a / b  
    print(a, "/", b, "=", division)  
  
 
print("SIMPLE CALCULATOR")  
  
# using the while loop to print menu list  
while True:  
    print("\nMENU")  
    print("1. ADDITION")  
    print("2. SUBTRACTION")  
    print("3. MULTIPLICATION")  
    print("4. DIVISION")  
    print("5. EXIT")  
    choice = int(input("\nEnter the Choice: "))  
  
# using if-elif-else statement to pick different options  
    if choice == 1:  
        print( "\nADDITION\n")  
        a = int( input("First Number: "))  
        b = int( input("Second Number: "))  
        add(a, b)  
  
    elif choice == 2:  
        print( "\nSUBTRACTION\n")  
        a = int( input("First Number: "))  
        b = int( input("Second Number: "))  
        subtract(a, b)  
  
    elif choice == 3:  
        print( "\nMULTIPLICATION\n")  
        a = int( input("First Number: "))  
        b = int( input("Second Number: "))  
        multiply(a, b)  
  
    elif choice == 4:  
        print( "\nDIVISION\n")  
        a = int( input("First Number: "))  
        b = int( input("Second Number: "))  
        divide(a, b)  
  
    elif choice == 5:  
        break  
      
    else:  
        print( "Please Provide a valid Input!")  