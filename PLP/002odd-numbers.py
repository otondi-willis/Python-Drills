#Function to check whether an integer is odd or even

def is_even():
    num = int(input("Enter an integer: "))
    if num%2 == 0:
        print(f"The integer {num} is an Even Number")
    else:
        print(f"The integer {num} is an Odd Number")
is_even()