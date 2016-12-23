
import urllib
import re 

blah = 'test'

def page_crawl_pick(url, regular_expression):
	"""
	using regular expression, scan url page
	then save desired in variable
	"""

	comp = re.compile(regular_expression)
	socket = urllib.urlopen(url)
	var = comp.findall(socket.read())
	socket.close()

	return var
