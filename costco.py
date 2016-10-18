import mechanize
from bs4 import BeautifulSoup



def main():
	#Create Browser instance/load page
	print "Creating Browser and loading page."
	br = mechanize.Browser()
	br.set_handle_robots(False)   # ignore robots
	br.set_handle_refresh(False)  # can sometimes hang without this
	br.addheaders = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 8.0; Windows 98;)')] 
	print "Done."

	#http://www.costco.com/warehouse-coupon-offers.html
	print "Getting Response"
	response = br.open('http://www.costco.com/warehouse-coupon-offers.html')
	print 'Done.'

	

	#bs4
	print "BS4 step"
	soup = BeautifulSoup(response.read())

	soipie = removeNonAscii(soup)


	for i in soipie.find_all('img'):
		print (i.get('alt'))


def removeNonAscii(s): return "".join([x if ord(x) < 128 else '?' for x in s])













if __name__ == '__main__':
	if main():
		print 'Yes'