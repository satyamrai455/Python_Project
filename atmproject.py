PIN = 1234
balance= 1000
print("\n")
print ("--------------WELCOME TO CREATIVE BANK OF INDIA-------------------------\n")
p=eval(input("Enter Your PIN: "))
if (p==1234):
    while True:
        c = int(input(''' 
             1: DEPOSIT    
             2: WITHDRAW
             3: CHECK BALANCE
             4: EXIT
             ENTER YOUR CHOICE: 
    '''))

        if ( c == 1 ):
                p = eval(input("Enter amount to deposit: "))
                balance = p + balance
                print("Amount deposited! ")
        elif (c==2):
                q = eval(input("Enter amount to withdraw: "))
                balance = balance - q
        elif(c==3):
                print(balance,"is your final balance")
        elif (c==4):
                print(" Thank You For Using CREATIVE BANK OF INDIA :) ")
                break
        else:
             print("Invalid input !")
else:
    print("Incorrect PIN: ")



