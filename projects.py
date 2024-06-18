###                     Rock, Paper n scissors

"""
import random

print("Rules:\n1. R v S = R\n2. S v P = S\n3. P v R = P\n")
print("Options are:\n1. Rock\n2. Paper\n3. Scissors\n")
x = int(input("Enter your choice(1-3): "))
while True:
    if x > 3  or x < 1:
        print("Invalid Option")
        x = int(input("Enter another number:"))

    if x == 1:
        x_n = "Rock"
    elif x == 2:
        x_n = "Paper"
    else :
        x_n = "Scissors"

    print("User's choice is:\t",x_n)
    print("Computer's Turn to choose a number:")

    y = random.randint(1,3)

    while y == x:
        y = random.randint(1,3)
    print("Computer's number: ",y)

    
    if y==1:
        y_n = "Rock"
    elif y == 2:
        y_n = "Paper"
    else :
        y_n = "Scissors"

    if x==y:
        print("Draw")
    elif (x == 1 and y == 2):
        print("Computer won")
    elif (x == 2 and y == 1):
        print("User won")
    elif (x == 2 and y == 3):
        print("Computer won")
    elif (x == 3 and y == 2):
        print("User won")
    elif (x == 3 and y == 1):
        print("Computer won")
    elif (x == 1 and y == 3):
        print("User won")

    print("Do you want to continue: y/n");
    ans = input()

    if ans == "n":
        break;
"""


###             Hand Cricket

###             Hand Cricket


"""
import random

def batfirst(count, flag):
    while True:
        w = int(input("Enter runs: "))
        z = comp_chance()
        if w == z:
            print("Out!!!, Brilliant run-out")
            print("Total score is:", count)
            print("Computer will bat now")
            print("Switching Sides....Please wait.")
            #SWITCHING SIDES(Bat -> Bowl)
            while True:
                t = int(input("Enter runs to be defended:"))
                u = comp_chance()
                if t == u:
                    if (count > flag):
                        print("Out")
                        print("You Won!!!")
                        break
                    elif(count == flag):
                        print("It is draw")
                    
                else:
                    flag += u
                    
                    print("Computer's score is",flag)
                    print("Remaining Runs:", count - flag)
                    if(count < flag):
                        print("You lost, Better luck next time <3.")
                        break
                
            break
        else:
                    count += w
                    print("Score is",count)

def bowlfirst(count, flag):
    while True:
        w = int(input("Enter the runs to be defended:"))
        z = comp_chance()
        if w == z:
            print("Out!!!")
            print("Target = ", flag)
            print("User will bat now")
            print("Switching sides...Please wait")
            #SWITCHING SIDES(Bowl -> Bat)                    
            while True:
                b = int(input("Enter runs:"))
                v = comp_chance()
                if b == v:
                    if (count < flag):
                        print("Out")
                        print("Better luck next time.")
                        break
                    elif(count == flag):
                        print("It is draw")
                    
                else:
                    count += b 
                    print("User's score is",count)
                    print("Remaining Runs:", flag - count)
                    if(count > flag):
                        print("Victory!!!") 
                        break
        else:
            flag += z
            print("Score is",flag)

def comp_chance():
    k = random.randint(1,6)
    print("Computer's choice is ", k)
    return (k)

def toss_check(choice_by_user, user, comp):
    if (user+comp)%2==0:
        if  choice_by_user=="even":
            return 0
        else:
            return 1
    if (user+comp)%2!=0:
        if  choice_by_user=="odd":
            return 0
        else:
            return 1

count = 0 # User score
flag = 0 # Computer score
print("Welcome all,\ntoday we all have gathered here to spectate an exciting match between\nUser XI and Posionous Python.")
print("Captain to User XI to make a call.")
x = input("Choose Odd or Even: ")
print("Smart move by the captain to choose: ",x)
y = int(input("Enter a number between 1 - 6: "))

#using 0 for user and 1 for computer from now on
z = comp_chance()
who_won = toss_check(x,y,z)

while True:
    if who_won==0:
        print("User XI won the toss")
        a = input("Choose Bat/bowl: ")
        if a == "bat":
            print("We reacher in the bat first")
            batfirst(count, flag)
            break
        elif a == "bowl":
            print("We reacher in the bowl first")
            bowlfirst(count, flag)
            break

    #If computer won the toss
    else:
        print("computer won toss")
        v = random.choice(["bat", "bowl"])
        print("Computer opt to: ", v)

        if v == "bat":
            bowlfirst(count, flag)
            break
        else:
            batfirst(count, flag)
            break        

"""


###             Hand Cricket

"""
import random

def batfirst(count, flag):
    while True:
        w = int(input("Enter runs: "))
        z = comp_chance()
        if w == z:
            print("Out!!!, Brilliant run-out")
            print("Total score is:", count)
            print("Computer will bat now")
            print("Switching Sides....Please wait.")
            #SWITCHING SIDES(Bat -> Bowl)
            while True:
                t = int(input("Enter runs to be defended:"))
                u = comp_chance()
                if t == u:
                    if (count > flag):
                        print("Out")
                        print("You Won!!!")
                        break
                    elif(count == flag):
                        print("It is draw")
                    
                else:
                    flag += u
                    
                    print("Computer's score is",flag)
                    print("Remaining Runs:", count - flag)
                    if(count < flag):
                        print("You lost, Better luck next time <3.")
                        break
                
            break
        else:
                    count += w
                    print("Score is",count)

def bowlfirst(count, flag):
    while True:
        w = int(input("Enter the runs to be defended:"))
        z = comp_chance()
        if w == z:
            print("Out!!!")
            print("Target = ", flag)
            print("User will bat now")
            print("Switching sides...Please wait")
            #SWITCHING SIDES(Bowl -> Bat)                    
            while True:
                b = int(input("Enter runs:"))
                v = comp_chance()
                if b == v:
                    if (count < flag):
                        print("Out")
                        print("Better luck next time.")
                        break
                    elif(count == flag):
                        print("It is draw")
                    
                else:
                    count += b 
                    print("User's score is",count)
                    print("Remaining Runs:", flag - count)
                    if(count > flag):
                        print("Victory!!!") 
                        break
        else:
            flag += z
            print("Score is",flag)

def comp_chance():
    k = random.randint(1,6)
    print("Computer's choice is ", k)
    return (k)

def toss_check(choice_by_user, user, comp):
    if (user+comp)%2==0:
        if  choice_by_user=="even":
            return 0
        else:
            return 1
    if (user+comp)%2!=0:
        if  choice_by_user=="odd":
            return 0
        else:
            return 1

count = 0 # User score
flag = 0 # Computer score
print("Welcome all,\ntoday we all have gathered here to spectate an exciting match between\nUser XI and Posionous Python.")
print("Captain to User XI to make a call.")
x = input("Choose Odd or Even: ")
print("Smart move by the captain to choose: ",x)
y = int(input("Enter a number between 1 - 6: "))

#using 0 for user and 1 for computer from now on
z = comp_chance()
who_won = toss_check(x,y,z)

while True:
    if who_won==0:
        print("User XI won the toss")
        a = input("Choose Bat/bowl: ")
        if a == "bat":
            print("We reacher in the bat first")
            batfirst(count, flag)
            break
        elif a == "bowl":
            print("We reacher in the bowl first")
            bowlfirst(count, flag)
            break

    #If computer won the toss
    else:
        print("computer won toss")
        v = random.choice(["bat", "bowl"])
        print("Computer opt to: ", v)

        if v == "bat":
            bowlfirst(count, flag)
            break
        else:
            batfirst(count, flag)
            break


"""


###             Hand Cricket

import random

def batfirst(count, flag):
    while True:
        w = int(input("Enter runs: "))
        z = comp_chance()
        if w == z:
            print("Out!!!, Brilliant run-out")
            print("Total score is:", count)
            print("Computer will bat now")
            print("Switching Sides....Please wait.")
            #SWITCHING SIDES(Bat -> Bowl)
            while True:
                t = int(input("Enter runs to be defended:"))
                u = comp_chance()
                if t == u:
                    if (count > flag):
                        print("Out")
                        print("You Won!!!")
                        break
                    elif(count == flag):
                        print("It is draw")
                    
                else:
                    flag += u
                    
                    print("Computer's score is",flag)
                    print("Remaining Runs:", count - flag)
                    if(count < flag):
                        print("You lost, Better luck next time <3.")
                        break
                
            break
        else:
                    count += w
                    print("Score is",count)

def bowlfirst(count, flag):
    while True:
        w = int(input("Enter the runs to be defended:"))
        z = comp_chance()
        if w == z:
            print("Out!!!")
            print("Target = ", flag)
            print("User will bat now")
            print("Switching sides...Please wait")
            #SWITCHING SIDES(Bowl -> Bat)                    
            while True:
                b = int(input("Enter runs:"))
                v = comp_chance()
                if b == v:
                    if (count < flag):
                        print("Out")
                        print("Better luck next time.")
                        break
                    elif(count == flag):
                        print("It is draw")
                    
                else:
                    count += b 
                    print("User's score is",count)
                    print("Remaining Runs:", flag - count)
                    if(count > flag):
                        print("Victory!!!") 
                        break
        else:
            flag += z
            print("Score is",flag)

def comp_chance():
    k = random.randint(1,6)
    print("Computer's choice is ", k)
    return (k)

def toss_check(choice_by_user, user, comp):
    if (user+comp)%2==0:
        if  choice_by_user=="even":
            return 0
        else:
            return 1
    if (user+comp)%2!=0:
        if  choice_by_user=="odd":
            return 0
        else:
            return 1

count = 0 # User score
flag = 0 # Computer score
print("Welcome all,\ntoday we all have gathered here to spectate an exciting match between\nUser XI and Posionous Python.")
print("Captain to User XI to make a call.")
x = input("Choose Odd or Even: ")
print("Smart move by the captain to choose: ",x)
y = int(input("Enter a number between 1 - 6: "))

#using 0 for user and 1 for computer from now on
z = comp_chance()
who_won = toss_check(x,y,z)

while True:
    if who_won==0:
        print("User XI won the toss")
        a = input("Choose Bat/bowl: ")
        if a == "bat":
            print("We reacher in the bat first")
            batfirst(count, flag)
            break
        elif a == "bowl":
            print("We reacher in the bowl first")
            bowlfirst(count, flag)
            break

    #If computer won the toss
    else:
        print("computer won toss")
        v = random.choice(["bat", "bowl"])
        print("Computer opt to: ", v)

        if v == "bat":
            bowlfirst(count, flag)
            break
        else:
            batfirst(count, flag)
            break










