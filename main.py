
from urllib_personal import page_crawl_pick



regular_expression = '<li><a href="/pdf/web/viewer\.html\?file=(.+\.pdf)" target="_blank">(.+)</a><br>\r\n.+G\.R\. No\. (\d+)\. (.+)</li>'
## will generate 
## pdf link - ('/jurisprudence/2016/february2016/204970.pdf',
## prosecutor and defense - 'Spouses Claudio and Carmencita Trayvilla Vs. Bernardo Sejas and Juvy Paglinawan represented by Jessie Paglinawan',
## G R NO - '204970',
## Date - 'February 1, 2016')

url = 'http://sc.judiciary.gov.ph/jurisprudence/2016/toc/february.php'


var = page_crawl_pick(url, regular_expression)
print var
