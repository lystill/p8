from register_stock import *
#from socket_listen import *
from Queue import Queue, Empty
from threading import Thread
from eventEngine import *
import os,sys
import time,datetime
ee=EventEngine()
i=1
# while True:
#     ee.put('s'*i)
#     time.sleep(1)
#     i=i+1








import socket
HOST = '127.0.0.1'
PORT = 4413
stocklist=[
# 'N.CN','EAT.CN','MMJ.CN'
   'BMW.DE','DAI.DE','BAS.DE','BMW.DE'
    #'3188.HK','0939.HK','2327.HK','0175.HK','2899.HK'
]
url_L2='http://127.0.0.1:8080/Register?symbol=%s&feedtype=L2'
url_L1='http://127.0.0.1:8080/Register?symbol=%s&feedtype=L1'
url_TOS='http://127.0.0.1:8080/Register?symbol=%s&feedtype=TOS'
url_L1_Setuotput='http://127.0.0.1:8080/SetOutput?symbol=%s&feedtype=L1&output='+str(PORT)+'&status=on'
url_TOS_Setuotput='http://127.0.0.1:8080/SetOutput?symbol=%s&feedtype=TOS&output='+str(PORT)+'&status=on'
url_Deregister_TOS='http://127.0.0.1:8080/Register?symbol=%s&feedtype=TOS'
# for stock in stocklist:
#    register(url_Deregister_TOS,stock)
#
#
#
# for stock in stocklist:
#     register(url_TOS_Setuotput,stock)
    # register(url_L1_Setuotput,stock)
# def datarecoder(data):
#     symbol=data[3]
#     fd=os.open('tick.csv')
#     os.write(fd,data)






def listen(HOST,PORT):



    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((HOST,PORT))
    i=1
    while True:
        data, addr = s.recvfrom(2048)
        if not data:
            print "client has exist"
            break



        d= data.split(',')

        message= d[1][8:]
        symbol=d[3][7:]
        market=symbol[-2:]


        print message ,symbol ,market,datetime.datetime.now()
        print '================================================================================'

        if message=='TOS':

            os.chdir('d:\\data\\TOS')
            if not os.path.exists(symbol):
                os.makedirs(symbol)
                print '%s is not exits' % symbol
            os.chdir(symbol)


            fo = open(str(symbol) + '.txt', 'a+')
            fo.write(str(data) + '\n')
            fo.close()
            i = i + 1
            print i
            ee.put(data)

            # os.makedirs(t)

            # with open('/path/to/file', 'r') as f:
            #    print f.read()
            #    try:
            #    f = open('/path/to/file', 'r')
            #    print f.read()
            # finally:
            #    if f:
            #        f.close()

        # print d[12],d[3],d[5],d[6]
        #d12 symbol

      #  z=os.getcwd()
       # datarecoder(data)





       # print "received:", data, "from", addr

    s.close()


listen(HOST,PORT)