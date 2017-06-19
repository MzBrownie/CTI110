# Calculating Body Mass Index
# 14 June 2017
# CTI-110 M3HW2 - Body Mass Index
# Patrice Browne
#

#BMI = weight * 703/height squared

weight = int(input("What is your weight?: "))

height = int(input("What is your height?: "))

bmi = weight * 703 / height**2

print ("Your BMI is: ",format(bmi, '.0f'))


if bmi >=18.5 and bmi <=25:
    print ("Your is optimal.")
    
elif bmi <18.5:
    print ("You are underweight.")
    
elif bmi >25:
    print ("You are overweight")

print ("-Done-")
