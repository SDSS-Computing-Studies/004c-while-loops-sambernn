##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Acces denied
"""
count = 0
un = ""
pw = ""
   
while un != "admin" and pw != "12345":
    un = input("enter your username:")
    pw = input("enter your password:")
    if un != "admin" and pw != "12345":
        print("Access denied")
        count = count + 1
    if count > 2:
        print ("Too many attempts")
        exit()

print("Access granted")