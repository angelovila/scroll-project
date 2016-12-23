
import urllib
import re 

comp = re.compile('<li><a href="/pdf/web/viewer\.html\?file=(.+\.pdf)" target="_blank">(.+)</a><br>\r\n.+G\.R\. No\. (\d+)\. (.+)</li>')
url = 'http://sc.judiciary.gov.ph/jurisprudence/2016/toc/february.php'
sock = urllib.urlopen(url)
li = comp.findall(sock.read())
sock.close()
print li

