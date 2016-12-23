
import urllib
import re 
pat = re.compile('<DT><a href="[^"]+">(.+?)</a>')

#compile [<pdf link>, <prosecutor vs defense name>, <GR and date>]
comp = re.compile('<li><a href="/pdf/web/viewer.html?file=[^"]+">(.+?)" target="_blank">(.+?)</a><br>(.+?)</li>')

#url = 'http://www.infolanka.com/miyuru_gee/art/art.html'
url = 'http://sc.judiciary.gov.ph/jurisprudence/2016/toc/february.php'
sock = urllib.urlopen(url)
#li = pat.findall(sock.read())
li = comp.findall(sock.read())
sock.close()
print li

