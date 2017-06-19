# Calculate the area of rectangles
# 12 June 2017
# CTI-110 M3T1 - Areas of Rectangles
# Patrice Browne
#

# Area of rectangle is length * width

first_rectangle_length = int (input ("First Rectangle Length? "))
first_rectangle_width = int (input ("First Rectangle Width? "))
second_rectangle_lenth = int (input ("Second Rectangle Length? "))
second_rectangle_width = int (input ("Second Rectangle Width? "))

first_area =  first_rectangle_length * first_rectangle_width
second_area = second_rectangle_lenth * second_rectangle_width
if (first_area  > second_area):
    print ("First Rectangle is Bigger." )
elif (first_area  < second_area):
    print ("Second Rectangle is Bigger.")
else:
    print ("They are equal!")
print ("Done.")
