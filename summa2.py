salary=int(input("salary:"))
age=int(input("Age:"))
if(salary>=20000 or age<=25):
    loan=int(input("loan"))
    if(loan>50000):
        print("max loan is 50000")
    print("you are elegible")
else:
    print("you are not elegible")
