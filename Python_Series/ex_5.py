#Use of try and except for the program to handle non-numeric
#input gracefully

def computepay(hours,rate):
    if fhrs > 40:
        print("Overtime")
        reg = hours * rate
        otp = (hours-40) * 0.5 * rate
        pay = reg + otp
    
    else:
        print("Regular")
        pay = hours * rate

    return pay
    

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

#Error handling introduced for non numerical inputs
try:
    fhrs = float(hours)
    fr = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

    
gross_pay = computepay(fhrs,fr)
print ("Pay:",gross_pay)