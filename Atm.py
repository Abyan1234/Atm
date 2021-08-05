class Atm:
    def __init__(self,cardNum,pinNum):
        self.cardNum=cardNum
        self.pinNum=pinNum

    def check_balance(self):
        print("Your Balance is 5000")

    def withdrawl(self,amount):
        new_amount=5000-amount
        print("You have withdrawn amount" +str(amount) + ". Your remaining balance is:- " + str(new_amount))


def main():
    card_num=input("insert your card number:- ")
    pin_num=input("insert your pin number:- ")

    new_user=Atm(card_num,pin_num)

    print("Choose your activity:-")
    print("1.Balance Enquiery 2.Widthrawl")   
    activity=int(input("Enter Activity Number:-"))

    if(activity==1):
        new_user.check_balance()
    elif(activity==2):
        amount=int(input("Enter amount you want to withdraw:- "))
        new_user.withdrawl(amount)
    else:
        print("Enter a valid number")

if __name__=="__main__":
    main()    


    
    


    

    

            
