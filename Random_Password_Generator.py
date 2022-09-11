import random

while True:
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    number = "0123456789"
    symbol = "!^#$%&()?*.@"

    string = upper + lower + number + symbol
    lenght = 16
    password = "".join(random.sample(string, lenght))

    print("Your New Password is: "+ password)

    generate_again = input("Are you want generate a new one Password? (y/n): ")
    if generate_again.lower() != "y":
        break