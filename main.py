import random
import time

list1=[1,2,3]

print("Welcome to Rock Paper Scissors game\nGAME BEGİNS !!")

user = int(input("Write 1 for Rock \nWrite 2 for Paper \nWrite 3 for Scissors\n"))

print("Rock")
time.sleep(1)
print("Paper")
time.sleep(1)
print("Scissors")
time.sleep(1)

computer = random.choice(list1)

if user==1:
    if computer == 1:
        print(" \t\tRock----------Rock\n\t\t\tDraw")
    if computer == 2:
        print(" \t\tRock----------Paper\n\t\t\tYou Lose") 
    if computer == 3:
        print(" \t\tRock----------Scissors\n\t\t\tYou Win")
if user==2:
    if computer == 1:
        print(" \t\tPaper----------Rock\n\t\t\tYou Win")
    if computer == 2:
        print(" \t\tPaper----------Paper\n\t\t\tDraw") 
    if computer == 3:
        print(" \t\tPaper----------Scissors\n\t\t\tYou Lose")
if user==3:
    if computer == 1:
        print(" \t\tScissors----------Rock\n\t\t\tYou Lose")
    if computer == 2:
        print(" \t\tScissors----------Paper\n\t\t\tYou Win") 
    if computer == 3:
        print(" \t\tScissors----------Scissors\n\t\t\tDraw")               
        




