extrovert_points = 0
introvert_points = 0 

#question 1
answer = input ("Do you have A) 5+ friends,or B) <5 friends?") 
if answer == "A":
        extrovert_points += 1
elif answer == "B":
        introvert_points += 1

#question 2
answer = input ("On a friday night would you rather A) go out with friends, or B) stay in and read/watch a movie?")
if answer == "A":
        extrovert_points += 1
elif answer == "B":
        introvert_points += 1 

#question 3
answer = input ("Are you A) louder,or B) quieter?")
if answer == "A":
        extrovert_points += 1
elif answer == "B":
        introvert_points += 1

#question 4
answer = input (" Do you prefer A) cats, or B) dogs?")
if answer == "A":
        introvert_points += 1
elif answer == "B":
        extrovert_points += 1

#question 5
answer = input ("Would you consider yourself an assertive person? A) yes, or B) no?")
if answer == "A":
        extrovert_points += 1
elif answer == "B": 
        introvert_points += 1

#end of quiz 
if extrovert_points > introvert_points : 
        print("You are an extrovert")
if extrovert_points < introvert_points :
        print("You are an introvert")