import random
def passauto(users: str,passwords: str):
    """������ ��������� �������
    """
    str0 = ".,:;!_*-+()/#�%&"
    str1 = "123456789"
    str2 = "qwertyuiopasdfghjklzxcvbnm"
    str3 = str2.upper()
    print(str3) # 'QWERTYUIOPASDFGHJKLZXCVBNM'
    str4 = str0+str1+str2+str3
    print(str4)
    ls = list(str4)
    print(ls)
    random.shuffle(ls)
    print(ls)
    # ��������� �� ������ 12 ������������ ��������
    psword = ''.join([random.choice(ls) for x in range(12)])
    # ������ �����
    print(psword)
