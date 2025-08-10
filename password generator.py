import random 
print("Welcome to the Python Password Generator!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
try:
    l=int(input("|How long your password should be??\"(4,6,8..):|"))

    print("_______________________________________________")
    i=int(input("|Enter the numbers of letters you want :|"))
    print("_______________________________________________")


    if i<=(l-2):
        a=""
        for y in range(i):
            r=random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            a=a+r
    else:
        print("Error: Your password must contain at least 2 numbers.")
        print("_______________________________________________")
        exit()
        


    j=int(input("|Enter the numbers of numbers you want :| "))
    print("_______________________________________________")
    if (i+j)<=l:
        b=""
        for z in range(j):
            c=random.randint(0,9)
            b=b+str(c)
    else:
        print("Error: Total letters and numbers exceed the password length limit.")
        print("_______________________________________________")
        exit()

    if (i+j)<l:
        k=int(input("|Would you like to include special characters? Enter 1 for Yes or 0 for No: |"))
        print("_______________________________________________")
        if k==1:
            g=""
            for x in range(l-(i+j)):
                v=random.choice("!@#$%^&*")
                g=g+v
            print(f"\nYour generated password is: {a+b+g} ")
            print("_______________________________________________")
    
        else:
            print("Invalid choice")
    else:
        
        print(f"\nYour generated password is: {a+b} ")
        print("_______________________________________________")


except :
    print("Invalid input. Please enter numeric values correctly.")
    print("_______________________________________________")

print("Thank you for using the generator!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")