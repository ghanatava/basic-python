def sum(*args):
    sum=0
    for i in args:
        sum+=i
    print(sum)
sum(0,2,3)
#kwargs
def add(**kwargs):
    print(kwargs)
add(surname='Uchiha',name='Itachi',nickname='Kinslayer')
def members(*kara,**akatsuki):
    print(kara)
    print('The GOATS',akatsuki)
members('jigen','kashinkoji','code',
akatsuki=['PAIN','KONAN','UCHIHA ITACHI','UCHIHA OBITO','HOSHIGAKI KISAME','OROCHIMARU'])
