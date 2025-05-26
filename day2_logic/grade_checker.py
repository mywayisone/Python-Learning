# This program computes the grade of a student from 
# the score between 1 - 100

score = input("Enter the score: ")

if score.isdigit():
    score = int(score)
    if score >= 0 and score <= 100:
        if score >= 75:
            print("Your grade is A")
        elif score >= 60 and score < 75:
            print("Your grade is B")
        elif score >= 50 and score < 60:
            print("Your grade is C")
        elif score >= 45 and score < 50:
            print("Your grade is D")
        else: print("Your grade is F")
    else: print("Your score cannot be above 100")
else: print("Enter a valid score value")