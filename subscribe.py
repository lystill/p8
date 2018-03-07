import urllib,urllib2
PORT=4413
eu=['BMW.DE','DAI.DE','BAS.DE','BMW.DE']
cn=['N.CN','EAT.CN','MMJ.CN']
hk=['3188.HK','0939.HK','2327.HK','0175.HK','2899.HK']
stocklist=hk


def register(url_type,stock):
    #resoponse=urllib2.Request(url_type%stock)
    req=urllib.urlopen(url_type%stock)




    print  req.getcode()
url_L2='http://127.0.0.1:8080/Register?symbol=%s&feedtype=L2'
url_L1='http://127.0.0.1:8080/Register?symbol=%s&feedtype=L1'
url_TOS='http://127.0.0.1:8080/Register?symbol=%s&feedtype=TOS'
url_L1_Setuotput='http://127.0.0.1:8080/SetOutput?symbol=%s&feedtype=L1&output='+str(PORT)+'&status=on'
url_TOS_Setuotput='http://127.0.0.1:8080/SetOutput?symbol=%s&feedtype=TOS&output='+str(PORT)+'&status=on'
url_Deregister_TOS='http://127.0.0.1:8080/Register?symbol=%s&feedtype=TOS'
for stock in stocklist:
   register(url_Deregister_TOS,stock)
#
#
#
for stock in stocklist:
    register(url_TOS_Setuotput,stock)