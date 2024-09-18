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


def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    return age

try:
    print(check_age(-5))
except ValueError as e:
    print(e)
