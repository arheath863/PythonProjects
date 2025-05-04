# This program determines if an email address is valid seeking the characters "@", and "."

def addressVal(address):
    dot = address.find(".")
    at = address.find("@")
    if (dot == -1):
        print("Error")
    elif (at == -1):
        print ("Error")
    else:
        print ("Valid")

    print("This program will determine if input os a valid email address")
    while(True):
        print("A valid email address needs an '@' and an '.'")
        x = input("Input yout email address:")

        addressVal(x)