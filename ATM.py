# declearation of my data

name = "onwugharam chibuike"
pin = 5050
amountInAccount = 15000000
#balance = ''
currentAmount = 15000000

# ATM machine proper

pinFromUser = int(input('enter ur pin '))

while pinFromUser == pin:
    print("welcome" + " " + name + " " + "what action do u want to perform")
    print("enter 1 to withdraw \nenter 2 to check balance \nenter 3 transfer")
    withdraw = int(input())
    if withdraw == 1:
        amountNeeded = int(input("enter amount u want to withdraw "))
        if amountNeeded <= amountInAccount:
            print("please collect ur cash")
            currentAmount = amountInAccount - amountNeeded
        else:
            print("insufficient fund")
        break
    balance = int(input())
    if balance == 2:
        print(currentAmount)
        break
    