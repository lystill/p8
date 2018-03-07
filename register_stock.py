import urllib,urllib2

def register(url_type,stock):
    resoponse=urllib2.Request(url_type%stock)

    urllib2.urlopen(resoponse)


   # print  resoponse.getcode()


