"""
Working with For Loops
"""

print("Count to 10!")

#Writing the for loop
"""
The for statement uses the for … in keywords to tell the computer 
to go through the list. A list is generated by the range() function.
The range() function takes a starting number and an ending number, 
but the ending number is not inclusive. Therefore, you pass in 11 
to have the function stop counting at 10. The letter x acts as a 
variable. Each time through the loop, the variable x is assigned 
to the next variable in the loop and is printed out to the screen.
"""
for x in range (0,11):
    print(x)


