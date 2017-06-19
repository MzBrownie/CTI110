# Identify a Persons age Bracket 
# June 13, 2017
# CTI-110 M3HW1 - Age Classifier
# Patrice Browne
#

age = int(input("What is your age? "))

if age >=20:
    print ("Adult")
elif age >= 13:
    print ("Teenager")
elif age > 1:
    print ("Child")
elif age <=1:
    print ("Infant")



