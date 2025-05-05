# This program determines if an email address is valid seeking the characters "@", and "."
def main ():
    #User input
    address = input("Please enter email address to check validity ")
    print (" The address entered is:" + address)
    addressVal(address)

def addressVal(address):
    dot = address.find(".")
    at = address.find("@")
    if (dot ==-1):
        print("Invalid")
    elif (at == -1):
        print("invalid")
    else:
        print("valid")
        

main()