username = str(input("Enter username: "))
password = str(input("Enter password: "))

if username == "pradeep" and password == "1234":
    print("login susccessfully")
elif username == "pradeep" and password != "1234":
    print("wrong password")
elif username != "pradeep" and password == "1234":
    print("wrong username")
else:
    print("wrong username and wrong password")