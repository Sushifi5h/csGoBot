from bs4 import BeautifulSoup



def pars_csgojacpot_html_for_name_deposits():
	#Main function is to pars the main HTML file

	#original html from get_html_csgojackpot.py opened in read
	html_file = open("/Users/vikramsingh/Desktop/Pratice/get_html_csgojackpot.txt", "r")

	#using beautiful soup to pars
	soup = BeautifulSoup(html_file)

	#New file to put the pars data
	open('/Users/vikramsingh/Desktop/Pratice/pars_csgojackpot_html_for_name_deposits.txt', 'w').close()
	parsed_file = open("/Users/vikramsingh/Desktop/Pratice/pars_csgojackpot_html_for_name_deposits.txt","r+")

	#go into <div style='opacity1;'
	for i in soup.findAll('div', style="opacity: 1;"):
		#find all and loop through <div class='text'
		for div in i.findAll('div', attrs ={'class': 'text'}):

			try: 
				data = "Name: (%s) (%s) (%s) \n" % (div.find('a').contents[0].encode('utf8'), div.find('a')['href'].encode('utf8'), div.contents[1].encode('utf8'))
				parsed_file.write(data)
			# for debugging print div.find('a')['href'], div.find('a').contents[0].encode('utf8'), div.contents[1]
			except: pass


	#close both files
	html_file.close()
	parsed_file.close()




if __name__ == '__main__':
	pars_csgojacpot_html_for_name_deposits()