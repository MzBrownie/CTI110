# Convert int and calculate total
# 5 July 2017
# CTI-110 M6T1 - File Display
# Patrice Browne
#



def main():
    total = 0.0


    myFile = open("numbers.txt","r")

        

    for line in myFile:
        amount = int(line)
        total += amount
        print(amount)
    myFile.close()

    print (format(total, ',.2f'))
#except Exception as err:
    #print(err)



main()
