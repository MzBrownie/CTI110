# Calculation a running total
# 15 June 2017
# CTI-110 M4T1 - Bug Collector
# Patrice Browne
#

# determin how many bugs caught in 5 days

total = 0

for days in range(1,6):
    value = int(input("Enter bugs caught: "))
    total = total + value
print ("Total bugs caught after five days:",total)
print ("Done.")
