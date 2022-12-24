import random
p1=input("select rock paper or scissor").lower()
p2=random.choice(["rock","paper","scissor"])
print("player 2 selected: ",p2)

if p1==p2:
    print("both of them selected",p1)

elif p1=="rock" and p2=="scissor":
    print("p1","win")

elif p1=="rock" and p2=="paper":
    print("p2","win")

elif p1=="scissor" and p2=="rock":
    print("p2","win")

elif p1=="scissor" and p2=="paper":
    print("p1","win")

elif p1=="paper" and p2=="rock":
    print("p1","win")

elif p1=="paper" and p2=="scissor":
    print("p2","win")


