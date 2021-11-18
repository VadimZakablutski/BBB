from module import*
users=["Vadim"]
passwords=["321321"]

password=passauto()

print(password)
while True:
    print("Reg - 1, Avt - 2, Välja - 3")
    v=int(input())
    if v==1:
        v=input("Sisestage nimi")
    elif v==2:
        v=input("Sisesta salasõna")
    elif v==3:
        print("Välja")
    else:
        print("On vaja valida 1,2 või 3.")