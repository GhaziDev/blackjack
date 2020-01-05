import random

choice = ["paper", "scissor", "rock"]
c = random.choice(choice)
q = str(input("Paper,Scissor,or Rock?  "))
while (q != "paper" and q != "scissor" and q != "rock"):
    q = str(input("Paper,Scissor,or Rock?  "))
if (q == c):
    print(c)
    print("Draw!")

elif (q == "scissor" and c == "rock"):
    print(c)
    print("You lost")
elif (q == "rock" and c == "scissor"):
    print(c)
    print("You won")
elif (q == "paper" and c == "rock"):
    print(c)
    print("You won")
elif (q == "rock" and c == "paper"):
    print(c)
    print("You lost")
elif (q == "scissor" and c == "paper"):
    print(c)
    print("you won")
elif (q == "paper" and c == "scissor"):
    print(c)
    print("you lost")