# encoding: UTF-8

from eventEngine import *
import  pandas as pd
import numpy as np
class strategy(object):

    def __init__(self,eventEngine):



        self.symbol=[]
        self.eventEngine=eventEngine
       # self.symboldict={}
        self.registerEvent()
        self.po={}

    # def putSpreadPosEvent(self, spread):
    #     """发出价差持仓事件"""
    #     event1 = Event(EVENT_SPREADTRADING_POS + spread.name)
    #     event1.dict_['data'] = spread
    #     self.eventEngine.put(event1)
    #
    #     event2 = Event(EVENT_SPREADTRADING_POS)
    #     event2.dict_['data'] = spread
    #     self.eventEngine.put(event2)
    #
    #     # ---------------------------------------------------------]
    #     # -------------

    def registerEvent(self):


        # self.eventEngine.register(EVENT_TICK, self.processTickEvent)
        self.eventEngine.register('tick', self.processTickEvent)
        self.eventEngine.register('zhishutick', self.processzhishuTickEvent)
        # self.eventEngine.register(EVENT_TRADE, self.processTradeEvent)
        # self.eventEngine.register(EVENT_POSITION, self.processPosEvent)
    def processTickEvent(self,event):

        print "processTickEvent"
        # print event.dict_['symbol']
        self.po[event.dict_['symbol']]=event.dict_['price']
        # print self.po
        print len(self.po)
        #hecheng
        if len(self.po)>2:
            z=0.0
            valueList=[]
            for s in self.po.iterkeys():

                t=float(self.po[s])
                valueList.append(t)
                z=z+t

            print valueList,z
            fo = open('d:\\zhishu.txt', 'a+')
            fo.write(str(z) + '\n')
            fo.close()



            event= Event();
            event.type_='zhishutick'
            event.dict_={'zhishu':z}
            self.eventEngine.put(event)
    def processzhishuTickEvent(self,event):

        print "process zhishu tick event",event.dict_


















