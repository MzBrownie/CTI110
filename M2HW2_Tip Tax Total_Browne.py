# Total amunt of meal at a restaurant
# June 11, 2017
# CTI-110 M2HW2-Tip Tax Total
# Patrice Browne
#

# Bill tip is 18%
# Bill salestax is 7%

sub_total = int(input("Sub Total: $")) 

tip = sub_total * .18

sales_tax = sub_total * 0.07

print ("Your bill Total is: $", format (sub_total + tip + sales_tax, '.2f'))
