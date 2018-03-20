from register_stock import *
#from socket_listen import *
from Queue import Queue, Empty
from threading import Thread
from eventEngine import *
from strategy import *
import os,sys
import time,datetime
ee=eventEngine()

i=1
# while True:
#     ee.put('s'*i)
#     time.sleep(1)
#     i=i+1








import socket
HOST = '127.0.0.1'
PORT = 4413



    # register(url_L1_Setuotput,stock)
# def datarecoder(data):
#     symbol=data[3]
#     fd=os.open('tick.csv')
#     os.write(fd,data)


s1=strategy(ee)


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
        date=d[-1][5:15]
        print date


        print message ,symbol ,market,datetime.datetime.now()
        print '================================================================================'

        if message=='TOS':

            os.chdir('d:\\data\\TOS')
            if not os.path.exists(market):
                os.makedirs(market)
                print '%s is not exits' % market
            os.chdir(market)
            if not os.path.exists(symbol):
                os.makedirs(symbol)
                print '%s is not exits' % symbol
            os.chdir(symbol)
            if not os.path.exists(date):
                os.makedirs(date)
                print '%s is not exits' % date
            os.chdir(date)



            fo = open(str(symbol) + '.txt', 'a+')
            fo.write(str(data) + '\n')
            fo.close()
            i = i + 1
            print i

            d1=data.split(',')
            tickdata={}
            tickdata['symbol']=d1[3][7:]

            tickdata['price']=d1[5][6:]
            event= Event();
            event.type_='tick'
            event.dict_=tickdata



            ee.put(event)

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