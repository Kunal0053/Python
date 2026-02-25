import random
a=random.randint(0,100)
while True:
    x=input("Want to play..?(Y-Yes/N-No) : ").lower()
    if(x=="y" or x=="yes"):
        t=0
        while(True):
            t=t+1
            n=int(input("Enter your guess: "))
            if n==a:
                print(f"YAY!!! You Won in {t} guesses.")
                break
            elif n>a:
                print("Too High!!, Try Again.. :(")
            else:
                print("Too Low!!, Try Again.. :(")
    elif x=="n" or x=="no":
        print("Exiting Game..!! BYE :)")
        break
    else:
        print("Enter Valid Option")

            
