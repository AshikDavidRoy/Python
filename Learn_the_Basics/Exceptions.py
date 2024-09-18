try:    
    num = int(input("Enter a number: "))    
    result = 10 / num
except ValueError:    
    print("Invalid input! Please enter a valid number.")
except ZeroDivisionError:    
    print("Cannot divide by zero!")

try:    
    num = int(input("Enter a number: "))    
    result = 10 / num
except ZeroDivisionError:    
    print("Cannot divide by zero!")
finally:    
    print("This will always run.")