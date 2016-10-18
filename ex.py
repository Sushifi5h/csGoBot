import mechanize
#url
URL = "http://www.reddit.com/r/pcgaming"

def main():
	print "Working...."
	
	#Create Browser instance/load page
	print "Creating Browser and loading page."
	br = mechanize.Browser()
	br.set_handle_robots(False)   # ignore robots
	br.set_handle_refresh(False)  # can sometimes hang without this
	br.addheaders = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 8.0; Windows 98;)')] 
	print "Done."

	#Try to recieve response
	print"Trying to get response"
	response = br.open(URL)
	print "Got response"

	#Print all forms
	# print "Print forms for selection."
	# for form in br.forms():
	# 	print form.name
	# 	print form

	#select form
	print "Selected Form"
	br.select_form(nr=0)
	print "Done"
	
	#Fill out form
	print "Trying to fill form"
	br['q'] = 'home'
	print "Done."
	br.submit()
	print "submited"


	#write in file
	print "Writing to file."
	write_file = open("/home/vik/Projects/Pratice/a.txt","w")


	for link in br.links():
		write_file.write("%s: " % link.text)
		write_file.write("%s" % link.url)
		write_file.write("\n")



		
	write_file.close

	print "finished writing to file."








if __name__ == "__main__":
	#cleans file
	open('/home/vik/Projects/Pratice/a.txt', 'w').close()
	#Run main()
	main()