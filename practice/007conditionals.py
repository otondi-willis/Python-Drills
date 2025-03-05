"""
Working with Conditionals
"""
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? ")

#Working with if statement
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
    
#Working with elif
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))

#Working with else statement
else:
    print("Thank you, please come again.")






