# Calulate Amount of Pay In Pennies
# Earned Over A Period Of Time
# Doubling Over Time
# With Dollar Amount As Output
# 19 June 2017
# CTI-110 M4HW2 - Pennies for Pay 
# Patrice Browne
#

num_of_days = int(input("Enter days worked: "))

for day in range(num_of_days):
    print ("Day:", day + 1)
pennies = 2 ** day

print ("Your Salary is: $",format(pennies/100,'.2f'))
print ("Done.")
