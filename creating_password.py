#a program that allow the user to create a safe strong password
def create_password():#a sub programe to enable the user create a password
    symbls=["!","$","%","^","*","?","@"]
    digits=["1","2","3","4","5","6","7","8","9","0"]
    tryagain=True
    while tryagain==True:
        score=0#counting the correct takings
        correction1=False#we can take this to be for uppercase
        correction2=False#we can take this to be for lowercase
        correction3=False#we can take this to be for digits
        correction4=False#we can take this to be for symbols
        password=input("enter Password")
        length=len(password)
        if length>=8:#the length of the password must be greater than 8
            score+=1
        for x in password:#x is any induvidual character in the entered password
            if x.islower():
                correction2=True
            if x.isupper():
                correction1=True
            if x in symbls:
                correction3=True
            if x in digits:
                correction4=True
        if correction1==True:
            score+=1
        if correction2==True:
            score+=1
        if correction3==True:
            score+=1
        if correction4==True:
            score+=1
        if score==1 or score ==2:#the summed scores determine the strength of the password
            print("this is a weak password try again")
        if score ==3 or score ==4:
            print("this password could be improved")
            again=input('do u want to try for a strong password')#gives chance to the user to change the password
            again.lower()
            if again=="no":
                print("Your password is:",password)
                tryagain=False             
    return password
def main():
    create_password()
main()
