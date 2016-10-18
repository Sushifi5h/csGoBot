from selenium import webdriver
import time

def get_html_csgojackpot():
	#Main function is to get the HTML from the webpage

	#Make browser/go to website/assert to see right page
	browser = webdriver.Firefox()
	browser.get('https://csgojackpot.com/')
	assert 'CS:GO Jackpot' in browser.title


	#time out to collect data 60 = 1 min/ The more you wait the more datat
	time.sleep(60)


	#open file/write HTML from website to file/close file
	open('/Users/vikramsingh/Desktop/Pratice/get_html_csgojackpot.txt', 'w').close()
	HTML_file = open('/Users/vikramsingh/Desktop/Pratice/get_html_csgojackpot.txt', 'r+')
	HTML_file.write((browser.page_source).encode('utf-8'))
	HTML_file.close()

	#Degbugging print (browser.page_source).encode('utf-8')
	

	#quit the browser 
	browser.quit()





if __name__ == '__main__':
	get_html_csgojackpot()