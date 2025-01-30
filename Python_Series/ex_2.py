#A program to prompt the user for hours and rate per hour
#to compute gross pay

hours=input("Enter Hours: ")
rate=input("Enter Rate: ")
pay= float(hours) * float(rate)

print("Gross pay: ", pay)
type(pay)