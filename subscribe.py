import urllib,urllib2,time
PORT=4413
eu=['BMW.DE','DAI.DE','BAS.DE','RNO.PA']
cn=['N.CN','EAT.CN','MMJ.CN']
hk=['3188.HK','0939.HK','2327.HK','0175.HK','2899.HK','1398.HK','3988.HK','0386.HK','0857.HK','0883.HK','2318.HK','2007.HK','0762.HK',
    '2628.HK','0836.HK','0992.HK','1928.HK','1088.HK','3328.HK']
jp=['8411.JP','8306.JP','6502.JP','7201.JP']
ol=['DNB.OL','MHG.OL','DNO.OL','STL.OL','GSF.OL']
stocklist=hk
url_L2='http://127.0.0.1:8080/Register?symbol=%s&feedtype=L2'
url_L1='http://127.0.0.1:8080/Register?symbol=%s&feedtype=L1'
url_TOS='http://127.0.0.1:8080/Register?symbol=%s&feedtype=TOS'
url_L1_Setuotput='http://127.0.0.1:8080/SetOutput?symbol=%s&feedtype=L1&output='+str(PORT)+'&status=on'
url_TOS_Setuotput='http://127.0.0.1:8080/SetOutput?symbol=%s&feedtype=TOS&output='+str(PORT)+'&status=on'
url_Deregister_TOS='http://127.0.0.1:8080/Register?symbol=%s&feedtype=TOS'


def register(url_type,stock):
    #resoponse=urllib2.Request(url_type%stock)


    req=urllib.urlopen(url_type%stock)
    print  req.getcode(),stock
    time.sleep(1)

for stock in stocklist:
   register(url_Deregister_TOS,stock)
#
#
#
for stock in stocklist:
    register(url_TOS_Setuotput,stock)