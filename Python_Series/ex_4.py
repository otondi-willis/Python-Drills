#Use of try and except for the program to handle non-numeric
#input gracefully



hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

#Error handling introduced for non numerical inputs
try:
    fhrs = float(hours)
    fr = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

if fhrs > 40:
    print("Overtime")
    reg = fhrs * fr
    otp = (fhrs-40) * 0.5 * fr
    pay = reg + otp
    
else:
    print("Regular")
    pay = fhrs * fr
    

print ("Pay:",pay)