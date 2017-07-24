def main():
    # get scores
    print ("Enter grade: ")
    score1 = int(input(" "))
    score2 = int(input(" "))
    score3 = int(input(" "))
    score4 = int(input(" "))
    score5 = int(input(" "))
    #calculate average
    average = (score1+score2+score3+score4+score5) / 5
    print ("Average is: ",average)
    return average
    

score = int(input("Enter Score: "))
if score >= 90:
    print ("letterGrade = A")
elif score >= 80:
    print ("letterGrade = B")
elif score >= 70:
    print ("letterGrade = C")
elif score >= 60:
    print ("letterGrade = D")
elif score >= 50:
    print ("letterGrade = F")
else:
    print ("Fail. Try again")


   
def calc_average(firstScore, secondScore, thirdScore, fourthScore, fifthScore):
        score1 = int(input("Enter First Score: "))
        print (determine_grade (score1))
        score2 = int(input("Enter Second Score: "))
        print (determine_grade (score2))
        score3 = int(input("Enter Third Score: "))
        print (determine_grade (score3))
        score4 = int(input("Enter Forth Score: "))
        print (determine_grade (score4))
        score5 = int(input("Enter Fifth Score: "))
        print (determine_grade (score5))
        average = calc_average(score1+score2+score3+score4+score5) / 5
        print ("Your average is: ",average)
        return average
    


def determine_grade(score):
    if score >= 90:
        print ("letterGrade = A")
    elif score >= 80:
        print ("letterGrade = B")
    elif score >= 70:
        print ("letterGrade = C")
    elif score >= 60:
        print ("letterGrade = D")
    elif score >= 50:
        print ("letterGrade = F")
    else:
        letterGrade = "Unsatifactory"
        print ("Fail. Try again")

main()
