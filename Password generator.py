import string
import secrets
import math


def User_Input() :
    Characters_Pool = ""
    print("Password generator initiated ")
    Length = int(input("Enter length of password you want : "))
    while Length < 8 :
        Length = int(input("Enter length again! The length must be greater than 7 : "))

    Amount = int(input("How many passwords do you want :  "))  
    while Amount <= 0 :
          Amount = int(input("Enter Again how many passwords do you want! It must be greater than zero :  "))

    while Characters_Pool == "" :
        Lower = input("Do you want Lower Case characters in password. Enter Y/N ").lower()
        if Lower == "y" :
            Characters_Pool =  Characters_Pool + string.ascii_lowercase

        Upper = input("Do you want Upper Case characters in password. Enter Y/N ").lower()
        if Upper == "y" :
            Characters_Pool =  Characters_Pool + string.ascii_uppercase

        Number = input("Do you want Numbers in password. Enter Y/N ").lower()
        if Number == "y" :
            Characters_Pool =  Characters_Pool + string.digits

        Special = input("Do you want special characters in password. Enter Y/N ").lower()
        if Special == "y" :
            Characters_Pool =  Characters_Pool + string.punctuation   

        if Characters_Pool == "" :
            print("You need to select atleast one category")      

    return Characters_Pool , Length , Amount


def Generate_Password(Charcters_Availabe , Length , Amount) : 
    for C in range(Amount) :
        Password = ""
        for L in range(Length) :
            Password = Password + secrets.choice(Charcters_Availabe)
        print(f"{C+1}  -  {Password}")

def Password_Strength(Charcters_Availabe , Length) :   
    Strength_Score = Length * math.log2(len(Charcters_Availabe))
    print("\nSecurity Profile of Passwords")
    if Strength_Score < 40 :
        print("Strength : Very Weak ")
    elif Strength_Score >= 40 and Strength_Score <= 59 :
        print("Strength : Weak ")
    elif Strength_Score >= 60 and Strength_Score <= 79 :
        print("Strength : Strong ")      
    else :
        print("Strength : Very Strong ")     
         



        
Pool , Length , Amount = User_Input()
Generate_Password(Pool , Length , Amount)
Password_Strength(Pool , Length)

