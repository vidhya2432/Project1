import os 
os.system("cls")
cash_box = {500:8,200:3,100:4}
def cash_available():
    cash_value = 0
    for note_value in cash_box:
        cash_value = cash_value + (cash_box[note_value]*note_value)
    return cash_value
def display_cash_box():
    print("ATM")
    print("---------------------------")
    for note in cash_box:
        print(note, cash_box[note])
    print("---------------------------")
    print("TOTAL:",cash_available())
def is_valid_amount(amount):
    if amount%100 == 0:
        return True
    return False
def denom(amount):
    possible_denom = {500:0,200:0,100:0}
    while(amount>0):
        if (amount>500):
            possible_denom[500]+=1
            amount-=500
            continue
        elif(amount>200):
            possible_denom[200]+=1
            amount-=200
        else:
            possible_denom[100]+=1
            amount-=100
    print("possible denom:",possible_denom)
    return possible_denom

def withdraw(amount_req):
     global cash
     if( not is_valid_amount(amount_req)):
         return -1
     possible_amount = denom(amount_req)
 
     if(amount_req<= cash_available()):
         for note in possible_amount:
             for i in range(possible_amount[note]):
                 cash_box[note] = cash_box[note]-1
     return possible_amount
display_cash_box()
amount_req = int(input("Please enter the amount:"))
amount = withdraw(amount_req)
if (amount==-1):
    print("Invalid Amount")
elif(len(amount)>0):
    print("In dispenser:",amount)
else:
    print("I don'y have much cash")
display_cash_box()