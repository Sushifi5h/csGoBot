from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re
import tweepy



def get_html_csgojackpot():
	#Main function is to get the HTML from the webpage

	#Make browser/go to website/assert to see right page
	browser = webdriver.Firefox()
	browser.get('https://csgojackpot.com/')
	assert 'CS:GO Jackpot' in browser.title


	#time out to collect data 60 = 1 min/ The more you wait the more datat
	time.sleep(900)


	#open file/write HTML from website to file/close file
	open('/home/vik/Projects/CSGO_LOSERS/get_html_csgojackpot.txt', 'w').close()
	HTML_file = open('/home/vik/Projects/CSGO_LOSERS/get_html_csgojackpot.txt', 'r+')
	HTML_file.write((browser.page_source).encode('utf-8'))
	HTML_file.close()

	#Degbugging print (browser.page_source).encode('utf-8')
	

	#quit the browser 
	browser.quit()

def pars_csgojacpot_html_for_name_deposits():
	#Main function is to pars the main HTML file

	#original html from get_html_csgojackpot.py opened in read
	html_file = open("/home/vik/Projects/CSGO_LOSERS/get_html_csgojackpot.txt", "r")

	#using beautiful soup to pars
	soup = BeautifulSoup(html_file)

	#New file to put the pars data
	open('/home/vik/Projects/CSGO_LOSERS/pars_csgojackpot_html_for_name_deposits.txt', 'w').close()
	parsed_file = open("/home/vik/Projects/CSGO_LOSERS/pars_csgojackpot_html_for_name_deposits.txt","r+")

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

def get_name_deposit():
	#Main function is to only name and deposit from parsed html file
	#Name: name Desposit: money
	#Name: name Desposit: name <- winner


	#open parsed_csgojackpot_html
	parsed_csgojackpot_html = open("/home/vik/Projects/CSGO_LOSERS/pars_csgojackpot_html_for_name_deposits.txt","r")


	#open new file to be written in
	open('/home/vik/Projects/CSGO_LOSERS/clean_name_money_winner.txt', 'w').close()
	clean_name_money_winner =  open("/home/vik/Projects/CSGO_LOSERS/clean_name_money_winner.txt","r+")


	#loop through file 
	for i in parsed_csgojackpot_html.readlines():
		#split and put everything in a list
		make_list = re.sub("[^\w]", " ",  i).split()
		#print i
		data = 'Name: %s Deposit: $ %s \n' % (make_list[1], make_list[-2])
		clean_name_money_winner.write(data)

	#close files
	parsed_csgojackpot_html.close()
	clean_name_money_winner.close()

def find_all_500_or_higher_bets():
	#look at clean_name_money_winners.txt & pull out all bets higher than 500


	#open file containing all names
	all_names = open("/home/vik/Projects/CSGO_LOSERS/clean_name_money_winner.txt","r")

	#new file to be written also clean file
	open('/home/vik/Projects/CSGO_LOSERS/find_all_500_or_higher_bets.txt', 'w').close()
	all_500_or_higher = open("/home/vik/Projects/CSGO_LOSERS/find_all_500_or_higher_bets.txt","r+")


	#split file in a list
	for i in all_names.readlines():
		#make list
		make_list = re.sub("[^\w]", " ",  i).split()
		#compare list to see if digit or string
		if make_list[-1].isdigit() == True:
			#if digit & greater than 500
			if int(make_list[-1]) >= 500:
				#take name and money 
				data = "%s %s\n" % (make_list[1], make_list[-1])
				all_500_or_higher.write(data)
		else: pass

	all_names.close()
	all_500_or_higher.close

def list_winners():
	#Main function is to list winners

	#open all names deposits
	all_names = open("/home/vik/Projects/CSGO_LOSERS/clean_name_money_winner.txt","r")

	#new file to be written in
	open('/home/vik/Projects/CSGO_LOSERS/list_winners.txt', 'w').close()
	clean_name_money_winner =  open("/home/vik/Projects/CSGO_LOSERS/list_winners.txt","r+")


	#FUCKEN MAGIC
	for i in all_names.readlines():
		make_list = re.sub("[^\w]", " ",  i).split()
		if make_list[-1].isdigit() == True:
			pass
		else: 
			data = "%s\n" % (make_list[1])
			clean_name_money_winner.write(data)

	#close files
	all_names.close()
	clean_name_money_winner.close()

def compare_all_500_or_greater_to_winners():
	#THERE IS WAY TOO MUCH MAGIC FOR ME TO EXPLAIN


	#open both files
	all_500 = open("/home/vik/Projects/CSGO_LOSERS/find_all_500_or_higher_bets.txt","r")
	all_winners = open("/home/vik/Projects/CSGO_LOSERS/list_winners.txt","r")

	#new file to be written in
	open('/home/vik/Projects/CSGO_LOSERS/compare_winners_losers.txt', 'w').close()
	clean_name_money_winner =  open("/home/vik/Projects/CSGO_LOSERS/compare_winners_losers.txt","r+")

	fo_e_with_deposit = []
	fo_w = []
	fo_e_name = []


	for i in all_500:
		fo_e_with_deposit.append(re.sub("[^\w]", " ",  i).split())

	for i in all_winners:
		fo_w.append(re.sub("[^\w]", " ",  i).split())



		
	losers = []



	for i in fo_e_with_deposit:
		for n in i:
			if n.isdigit() == True:
				pass
			else:
				if n in open('/home/vik/Projects/CSGO_LOSERS/list_winners.txt').read():
					pass
				else:
					losers.append(i)


	for i in losers:
		data = '%s \n' % (i)
		clean_name_money_winner.write(data)

	all_500.close
	all_winners.close
	clean_name_money_winner.close()




def tweeting():

	#open losers
	losers = open("/home/vik/Projects/CSGO_LOSERS/print_for_twitter.txt","r")



	# == OAuth Authentication ==
	#
	# This mode of authentication is the new preferred way
	# of authenticating with Twitter.

	# The consumer keys can be found on your application's Details
	# page located at https://dev.twitter.com/apps (under "OAuth settings")
	consumer_key="evPYTGEq7ePIiHTF4IxbkTNQM"
	consumer_secret="hHwQt6PurP6zWg736PjDKvXUGB6N1dnb6tKgT5nmyaz5B7EiRq"

	# The access tokens can be found on your applications's Details
	# page located at https://dev.twitter.com/apps (located
	# under "Your access token")
	access_token="3152622859-PUtvHsNUA5NIG0RE4hCbenLdlZrrSPKiyMsEUV5"
	access_token_secret="hjsU7ULNqiYuOjBsVEVn4xsKsumtGZpMMnNTXW4vyErhO"

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.secure = True
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)

	# If the authentication was successful, you should
	# see the name of the account print out
	#print(api.me().name)

	# If the application settings are set for "Read and Write" then
	# this line should tweet out the message to your account's
	# timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
	for i in losers:
		api.update_status(status=i)
	losers.close()


def get_more_info_losers(): 

	losers = open("/home/vik/Projects/CSGO_LOSERS/compare_winners_losers.txt", "r")
	everyone = open("/home/vik/Projects/CSGO_LOSERS/pars_csgojackpot_html_for_name_deposits.txt", "r")
	open("/home/vik/Projects/CSGO_LOSERS/testing.txt", "w").close()
	testing = open("/home/vik/Projects/CSGO_LOSERS/testing.txt", "r+")


	for i in losers.readlines():
		make = re.sub("[^\w]", " ",  i).split()
		with open("/home/vik/Projects/CSGO_LOSERS/pars_csgojackpot_html_for_name_deposits.txt") as f:
			for line in f:
				search = "(valued at $" + make[1]
				if search in line:
					testing.write(line)


	losers.close()
	everyone.close()
	testing.close()


def print_for_twitter():
	#Make file for so python can easily publish datat


	#Get losers
	losers = open("/home/vik/Projects/CSGO_LOSERS/testing.txt","r")

	#write in new file
	open('/home/vik/Projects/CSGO_LOSERS/print_for_twitter.txt', 'w').close()
	print_for_twitter = open("/home/vik/Projects/CSGO_LOSERS/print_for_twitter.txt","r+")

	loser_list = []

	#Trying some magic
	for i in losers.readlines():
		for word in i.split("("):
			loser_list.append(word[0:-2])


	while 'Name' in loser_list:
		loser_list.remove('Name')

	Names = loser_list[::4]
	steam_links = loser_list[1::4]
	value = loser_list[3::4]


	for i in range(0,len(Names)):
		data = "%s(%s) just LOST skins %s. \n" % (Names[i], steam_links[i], value[i][:-3])
		print_for_twitter.write(data)

	#close files
	losers.close()
	print_for_twitter.close()







if __name__ == '__main__':
	while True:	
		print "Starting Scrapper."
		get_html_csgojackpot()
		print "Finished Scrapping."
		print "Parsing raw HTML."
		pars_csgojacpot_html_for_name_deposits()
		print "Finished parsing raw HTML."
		print "Cleaning parsed file."
		get_name_deposit()
		print "Finished cleaning parsed file."
		print "Find everyone with a bet of 500 or higher."
		find_all_500_or_higher_bets()
		print "Finished finding everyone with a bet higher than 500."
		print "Find all winners."
		list_winners()
		print "Finished finding all winners."
		print "Comparing everyone with a bet of 500 or higher against winners."
		compare_all_500_or_greater_to_winners()
		print "Finished comparing everyone against winners."
		print "Extracting tweets and printing tweets."
		get_more_info_losers()
		print_for_twitter()
		print "Finished sorting tweets."
		print "Tweeting to CS:GO JACKPOT LOSERS"
		tweeting()
		print "Done."
		






