import sys, os
import time, datetime


def loaddata(symbol, length):
    market = symbol[-2:]

    os.chdir('D:\\data\\TOS\\' + market + '\\' + symbol)

    listd = os.listdir('D:\\data\\TOS\\' + market + '\\' + symbol)
    data = []
    for date in listd[-length:]:
        os.chdir(date)
        with open(symbol + '.txt') as fp:
            t = fp.readlines()

        os.chdir('D:\\data\\TOS\\' + market + '\\' + symbol)
        print len(data)
        data+=t
        time.sleep(1)

    return data
    #    for line in

if __name__ == "__main__":
    T=loaddata('3188.HK',3)
    time.sleep(0.02)
    for i in T:
        if i=='\n':
            T.remove(i)

    print T
    print type(T),len(T)
