def split():
    print("WELCOME TO SPLIT EMAILS")
    print
    email =input("ENTER YOUR EMAILS:")

    
    (username , domain) = email.split("@")
    (domain , extention ) = domain.split(".")

    print("Username:" , username)
    print("Domain:" , domain)
    print("Extention:" , extention)
while True:
    split()