import socket
from N4Tools.Design import *
c=Color()
t=Text()
print(t.Figlet("PortScanner",font="big"))
text=t.pos(c.rgb(203, type="FG")+"Enter Ip:",x=8,y=2)
while True:
    target=input(text)
    if target == 'exit' : break
    #p=80
    ports=[20,21,22,23,24,25,443,80,8080]
    for p in ports:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        r=s.connect_ex((target,p))
        if r == 0:
            service=socket.getservbyport(p)
            print(c.reader("-_-_-_-[[$RED] {} [$/]]-- is open ---> [$GREEN]{} [$/]"). format(p, service))
            s.close()
    print(c.RED+"Done....!")
    o=input(c.YELLOW+"Enter y for continue!")
    if o=='y':
                continue
    else:
                break
  

    