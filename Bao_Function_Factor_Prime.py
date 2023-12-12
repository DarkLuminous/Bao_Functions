import os

def In_Outro():
    print("\n\nCS112: COMPUTER PROGRAMMING 1 - Factor of n and Prime numbers of range")
    print("CREATED BY: ROGER E. BAO JR.\n")


In_Outro()
print("PROBLEM: Modify your code from your previous activity about finding the smallest factor of n and prime numbers of range using functions. \n")
print("RULES TO CONSIDER:")
print("[1] If the user selects 1, the code for  finding the smallest factor of n will invoked.")
print("[2] If the user selects 2, the code for  finding the prime numbers of range will invoked.")

def smallestFacttor():
    while True:
        n = int(input("Enter Integer:"))
        i = 1
        if n >= 2:
            while True:
                i = i + 1
                factor = n % i
                prime = n // i

                if (prime == 1):
                    print(f"{n} is a Prime number")
                    break
                elif (factor == 0):
                    print(f"The Smallest Factor of {n} other than 1 is: {i}")
                    break
        else:
            print("invalid Number. Enter a number greater than 1.")
            break
def primeRanged():

    while True:
        input("\n\nPress Enter to Continue . . .")
        os.system('cls')

        start = input("Enter a Number [start]\n=")

        if int(start) < 0:
            print("Enter a non-negative number.")
            continue

        if int(start) == 0:
            print("Enter zero again to Exit")

        end = input("Enter a Number [end]\n=")

        if int(end) < 0:
            print("Enter a non-negative number.")
            continue

        if int(end) < int(start):
            print(f"Enter a number greather than {start}.")
            continue

        if int(start or end) == 0:
            In_Outro()
            main()

        print(f"\n############################\n\nPrime numbers between {start} and {end} are:")
        for num in range(int(start), int(end) + 1):
            if num > 1:
                primeCheck = True
                for i in range(2, int(num ** 0.5) + 1):
                    if num % i == 0:
                        primeCheck = False
                        break
                if primeCheck:
                    print(num, end=" ", )

def main():
    while True:
        choice = int(input("\nPLEASE ENTER A CHOICE \n[1]Smallest Factor or [2]Prime Range and [0]Exit: "))
        if choice == 1:
            smallestFacttor()

        elif choice == 2:
            primeRanged()

        elif choice == 0:
            In_Outro()
            exit()

        else:
            print("INVALID CHOICE!!! \nPlease Enter [1] [2] [0] only!")
            input("Press Enter To Continue . . .")
            os.system('cls')
main()