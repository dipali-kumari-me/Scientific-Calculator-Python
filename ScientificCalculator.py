import math

def scientific_calculator():
    print("===== SCIENTIFIC CALCULATOR =====")
    print("Made by: DIPALI KUMARI")
    
    while True:
        print("\n--- MENU ---")
        print("1. Add         2. Subtract    3. Multiply    4. Divide")
        print("5. Power       6. Square Root 7. Sin         8. Cos")
        print("9. Tan         10. Log        11. Exit")
        
        choice = input("Enter your choice (1-11): ")
        
        if choice == '11':
            print("Thank you for using the calculator!")
            break
        
        # Operations with 2 numbers
        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
        # Operations with 1 number
        elif choice in ['6', '7', '8', '9', '10']:
            num1 = float(input("Enter number: "))
        
        # Calculation
        if choice == '1':
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
            else:
                print("Error! Cannot divide by zero")
        elif choice == '5':
            print(f"Result: {num1}^{num2} = {math.pow(num1, num2)}")
        elif choice == '6':
            print(f"Result: sqrt({num1}) = {math.sqrt(num1)}")
        elif choice == '7':
            print(f"Result: sin({num1}°) = {math.sin(math.radians(num1))}")
        elif choice == '8':
            print(f"Result: cos({num1}°) = {math.cos(math.radians(num1))}")
        elif choice == '9':
            print(f"Result: tan({num1}°) = {math.tan(math.radians(num1))}")
        elif choice == '10':
            print(f"Result: log({num1}) = {math.log10(num1)}")
        else:
            print("Invalid choice! Please try again")


scientific_calculator()
