
from urllib_personal import page_crawl_pick



regular_expression = '<li><a href="/pdf/web/viewer\.html\?file=(.+\.pdf)" target="_blank">(.+)Vs\. (.+)</a><br>\r\n.+G\.R\. No\. (\d+)\. (\w+) (\d+), (\d+)</li>'
## will generate 
## pdf link - ('/jurisprudence/2016/february2016/204970.pdf',
## prosecutor and defense - 'Spouses Claudio and Carmencita Trayvilla Vs. Bernardo Sejas and Juvy Paglinawan represented by Jessie Paglinawan',
## G R NO - '204970',
## Date - 'February 1, 2016')

#('/jurisprudence/2016/february2016/198994.pdf', 'Iris Morales Vs. Ana Maria Olondriz, et al.', '198994', 'February', '3', '2016')

#('/jurisprudence/2016/february2016/199371.pdf', 'Petron LPG Dealers Association and Total Gaz LPG Dealers Association ', 'Nena C. Ang, et al.', '199371', 'February', '3', '2016')

#('/jurisprudence/2016/february2016/213910.pdf', 'Vinson D. Young, et al. Vs. People of the Philippines', '213910', 'February 3, 2016')

url = 'http://sc.judiciary.gov.ph/jurisprudence/2016/toc/february.php'


var = page_crawl_pick(url, regular_expression)
print var
