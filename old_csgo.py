import mechanize
from bs4 import BeautifulSoup



def main():
	#Create Browser instance/load page
	print "Creating Browser and loading page."
	br = mechanize.Browser()
	br.set_handle_robots(False)   # ignore robots
	br.set_handle_refresh(False)  # can sometimes hang without this
	#br.addheaders = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 8.0; Windows 98;)')]
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')] 
	print "Done."

	print "Getting Response"
	response = br.open('https://csgojackpot.com/')
	print 'Done.'
	print response.code


	#print response.read()


	
	
	
	soup = BeautifulSoup(response.read())

	mydivs_0 = soup.findAll("div", { "class" : "activity-status" })
	mydivs_1 = soup.findAll("div", { "class" : "modal fade modal-confirm-deposit" })

	for div in mydivs_0:
		print div

	print ""
	print ""
	print ""
	print ""

	for div in mydivs_1:
		print div

















if __name__ == '__main__':
	if main():
		print 'Yes'