#Rewriting pay computation to give employee 1.5 times
#the hourly rate for hours worked above 40 hours

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
fhrs = float(hours)
fr = float(rate)
if fhrs > 40:
    print("Overtime")
    reg = fhrs * fr
    otp = (fhrs-40) * 0.5 * fr
    pay = reg + otp
    
else:
    print("Regular")
    pay = fhrs * fr
    

print ("Pay:",pay)