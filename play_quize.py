print("lets Play the quiz" )
player = input("do you want to play yes/no ")

if player != "yes":
    quit()
print("lets start the quiz")
score = 0
print("LEVEL 01 ")

print("Question No 1")

answer = input("what is capital of india ?")
if answer == "Delhi":
    print("CORRECT")
    score += 1
else:
    print("INCORRECT")

print("Question No 2")


answer = input("what is the national bird of india ?" )
if answer == "Peacock":
    print("CORRECT")
    score += 1
else:
    print("INCORRECT")

print("Question No 3")
    
answer = input("what is the national animal of india ?") 
if answer == "Tiger":
    print("CORRECT")
    score += 1
else:
    print("INCORRECT")

print("Question No 4")

    
answer = input("what is the national anthum of india ?" )
if answer == "jana gana mana":
    print("CORRECT")
    score += 1
else:
    print("INCORRECT")

print("congratulation you completed the level 1 :) " )
#level_02
print( "LEVEL 02 - 'TRUE OR FALSE'")
#question_no_1
print("Question no 01 ")

answer = input("15 august is a republicday it is true or fulse ?" )
if answer == "false":
    print("TRUE")
    score += 1
else:
    print("FALSE")
#question_no_2
print("Question mo 02")

answer = input("football is a national sports of india its true or false?" )
if answer == "false":
    print("TRUE")
    score += 1
else:
    print("FULSE")
#question_no_3
print("Question mo 03")


answer = input("guwahati os the capital of assam its true or fulse ?" )
if answer == "true":
    print("TRUE")
    score += 1
else:
    print("FULSE")
#question_no_4
print("Question mo 04")

answer = input("mahatma gandhi is first primeminister of india its or false?" )
if answer == "false":
    print("TRUE")
    score += 1
else:
    print("FULSE") 

print("your final score "+str(score))
print("you got" +str((score/8)* 100)+ "%")





    


