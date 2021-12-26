
import socket
import os
from IPy import IP
address=input("Enter IP Address to scan : ")
def port_scan(address,port):
   try:
       sock=socket.socket()
       sock.settimeout(1)
       sock.connect((address,port))
       print('port ' ,port, ' is open on ',address)
   except:
        print("Port ",port," is closed")
choice=int(input("type 1 for Specific port scan on same address \nType 0 for multiple port scan on Same Address \n"))
if choice==0:
     start=int(input('Enter your  starting range of part scan : '))
     end=int(input('Enter your Ending range of Port scan : '))
     for i in range(start,end+1):
         port_scan(address,i)
else:
    port=int(input("Enter Port to scan : "))
    port_scan(address,port)
os.system("pause")




    


    


    

    



    




