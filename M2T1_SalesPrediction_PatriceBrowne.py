# Calulate Annual Profit
# June 14, 2017
# CTI-110 M2T1 - Sales Prediction
# Patrice Browne
#

total_sales = int(input("Total sales:$ "))

# profit = 0.23

profit = total_sales * .23

annual_profit = total_sales - profit

print ('The annual profit is $', format (annual_profit, '.2f'))

