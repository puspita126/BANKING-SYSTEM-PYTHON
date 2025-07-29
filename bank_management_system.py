import csv
import random
import time
import sys
acount_data = "customer.csv"
print("welcome to my bank management system")  
def create_acount():
        name = input("enter your name?")
        mobilenumber = input("enter your mobile number?")
        type_of_account = input("type of acount(current/saving?)")
        account_number = account_number_generator()
        balance = input("Enter initial deposit amount: ")
        print(f"\n Account successfully created!\n Your account number is: {account_number}")
        print(" Visit us again!\n")
        with open(acount_data,mode="a",newline="")as file:
            writer=csv.writer(file)
            writer.writerow([name , mobilenumber, type_of_account, account_number ,balance])
def verify(account_number):
     with open(acount_data,mode="r")as file:
          reader=csv.reader(file)
          header=next(reader)
          for row in reader:
               if row[3]== account_number:
                    return True
     return False           


def deposit_amount(account_number):
    rows=[]
    is_verified=verify(account_number)
    if is_verified==True:
        deposit_money=int(input("enter your deposit value"))
        with open(acount_data,mode="r")as file:
          reader=csv.reader(file)
          for row in reader:
               if row[3]== account_number:
                    print(type(row[4]))  
                    print(type(deposit_money))
                    
                    row[4]=int(row[4])+deposit_money
               rows.append(row)
        with open(acount_data,mode="w",newline="")as file:
            writer=csv.writer(file)
            writer.writerows(rows) 


def withdraw_amount(account_number):
    rows=[]
    is_verified=verify(account_number)
    if is_verified==True:
        withdraw_money =int(input("enter your withdraw value"))
        with open(acount_data,mode="r")as file:
          reader=csv.reader(file)
          for row in reader:
               if row[3]== account_number:
                  print(type(row[4]))  
                  print(type(withdraw_money))
                  row[4] =int(row[4])-withdraw_money
               rows.append(row)
        with open(acount_data,mode="w",newline="")as file:
            writer=csv.writer(file)
            writer.writerows(rows)  
            
                 
        with open(acount_data,mode="w",newline="")as file:
            writer=csv.writer(file)
            writer.writerows(rows)

def check_balance(account_number):
    is_verify= verify(account_number) 
    if is_verify== True:
        print("your account is verified")
        print("proccessing your balance please wait.......")
        time.sleep(5)
        with open(acount_data,mode="r")as file:
            reader=csv.reader(file)
            for row in reader:
                if row[3]==account_number:
                    balance=row[4]
        print(f"your account balance is : {balance}")    


# def delete_acc(account_number):
#     [row]
#     is_verified=verify(account_number)
#     if is_verified == True:
#         with open(acount_data,mode="w")as file:
#             writer=csv.writer(file)
#             for row in writer:

#                 if row[3]== account_number:
                    
#                     writer.writerows(rows)

#                     row[3]!= "0"

def delete_acc(account_number):
     is_verified=verify(account_number)
     if is_verified == True:
    
        with open(acount_data, "r") as file:
         
         reader = csv.reader(file)
         rows = list(reader)
        header = rows[0]
        new_rows = [row for row in rows if row[3] != account_number or row == header]
        with open(acount_data, "w", newline="") as file:
            csv.writer(file).writerows(new_rows)
        print("Account deleted successfully" if len(rows) != len(new_rows) else "Account not found")

                                    



                   


def account_number_generator():
      number = random.randint(1000000000,9999999999)
      return number



while True:
    print("\n choose an option:")
    print("1. create an acount")    
    print("2. deposit money")
    print("3. withdraw money")
    print("4. check acount balance")
    print("5. delete exsisting acount")
    print("6. exit")
    choice = input("enter your choice(1-6):")
    if choice== "1":
        create_acount()
    elif choice == "2":
        acc_num = input("enter account number") 
        deposit_amount(acc_num)   
    elif choice == "3":
         acc_numb =input("enter your account number")
         
         withdraw_amount(acc_numb)    
    elif choice == "4":
         acc_numbe =input("enter your account number")
         check_balance(acc_numbe)
    elif choice == "5":
         acc_number =input("enter your account number")
         delete_acc(acc_number)
    elif choice == "6":
        sys.exit(0)

    else:
        print("choose a VALID OPTION ABOVE")    


#MINI AC VALUE MUST BE 500,

               
        