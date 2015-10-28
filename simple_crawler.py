import urllib2
from urllib2 import Request
req = Request("http://www.bilibili.com/ranking")
res = urllib2.urlopen(req)
print res.read().decode('UTF-8')
