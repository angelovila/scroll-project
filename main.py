
from urllib_personal import page_crawl_pick



regular_expression = '<li><a href="/pdf/web/viewer\.html\?file=(.+\.pdf)" target="_blank">(.+)</a><br>\r\n.+G\.R\. No\. (\d+)\. (.+)</li>'
url = 'http://sc.judiciary.gov.ph/jurisprudence/2016/toc/february.php'


var = page_crawl_pick(url, regular_expression)
print var
