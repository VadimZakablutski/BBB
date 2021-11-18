import random
def passauto()->str:
    str0 = ".,:;!_*-+()/#¤%&"
    str1 = "123456789"
    str2 = "qwertyuiopasdfghjklzxcvbnm"
    str3 = str2.upper()
    print(str3)
    str4 = str0+str1+str2+str3
    print(str4)
    ls = list(str4)
    print(ls)
    random.shuffle(ls)
    print(ls)
    psword = ''.join([random.choice(ls) for x in range(12)])
    return(psword)
def passcontrol(psword)->str:
    psword=list(psword)
    for i in psword:
        if i.isdigit()== True:
            digit="True"
        if i.isalpha()== True:
            alpha="True"
        if i.isupper()== True:
            upper="True"
        if i.islower()== True:
            lower="True"
        if i in [".","_","/","@"]:
            synbl="True"
    if digit=="True" and upper=="True" and alpha=="True" and lower=="True" and synbl=="True":
        ctr=True 
    else:
        ctr=False
