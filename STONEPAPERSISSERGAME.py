import random
print("----------STONE PAPER SISSER GAME----------")
List = ["STONE","PAPER","SISSOR"]
User=input("Enter \"Start\" to play or Enter \"Exit\" to exist:")
comp=0
user=0
while(User!="EXIT"):
    User=input("Your play:")
    Computer= random.choice(List)
    print("Computer Play:",Computer);
    if(Computer=="STONE" and User=="SISSOR"):
        comp+=1
        print("Computer own")
        print("User points:",user)
        print("Computer points:",comp)
    elif(Computer=="PAPER"and User=="STONE"):
        comp+=1
        print("Computer own")
        print("User points:",user)
        print("Computer points:",comp)
    elif(Computer=="SISSOR"and User=="PAPER"):
        comp+=1
        print("Computer own")
        print("User points:",user)
        print("Computer points:",comp)
    elif(User=="STONE"and Computer=="SISSOR"):
        user+=1
        print("You own")
        print("User points:",user)
        print("Computer points:",comp)
    elif(User=="PAPER"and Computer=="STONE"):
        user+=1
        print("You own")
        print("User points:",user)
        print("Computer points:",comp)
    elif(User=="SISSOR" and Computer=="PAPER"):
        user+=1
        print("You own")
        print("User points:",user)
        print("Computer points:",comp)
    else:
        print("Draw")
        print("User points:",user)
        print("Computer points:",comp)
if(user>comp):
    print("You won the game!")
else:
    print("System own the match!")


