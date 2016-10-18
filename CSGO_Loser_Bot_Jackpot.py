from selenium import webdriver
import time
from bs4 import BeautifulSoup
import tweepy

def get_html_csgojackpot():
	#Main function is to get the HTML from the webpage

	#Make browser/go to website/assert to see right page
	browser = webdriver.Firefox()
	browser.get('https://csgojackpot.com/')
	assert 'CS:GO Jackpot' in browser.title


	#time out to collect data 60 = 1 min/ The more you wait the more datat
	print "Start : %s" % time.ctime()
	time.sleep( 15 )
	print "End : %s" % time.ctime()


	#open file/write HTML from website to file/close file
	open('get_html_csgojackpot.txt', 'w').close()
	HTML_file = open('get_html_csgojackpot.txt', 'r+')
	HTML_file.write((browser.page_source).encode('utf-8'))
	HTML_file.close()

	#Degbugging print (browser.page_source).encode('utf-8')
	

	#quit the browser 
	browser.quit()

def pars_main_html():
	#Variable for Soup
	un_souped = open('get_html_csgojackpot.txt', 'r+')

	#file to put stuff for now
	open('pars_csgojackpot_html_for_name_deposits.txt', 'w').close()
	parsed_file = open("pars_csgojackpot_html_for_name_deposits.txt","r+")

	#souped
	soup = BeautifulSoup(un_souped)

	#Magic
	for i in soup.findAll("div", {"style": "opacity: 1;"}):
		if i.find("div", {"class": "activity user-deposit"}) != None:
			#       Player Name SLink Money Items#
			player_info = "||||||||Player|||||||| ||||||||%s|||||||| ||||||||%s|||||||| ||||||||%s|||||||| ||||||||%s|||||||| \n" % \
					(i.find("a",{"target": "_blank"}).contents[0] ,\
					 i.find("a",{"target": "_blank"})["href"],\
					 i.find("div",{"class": "text"}).contents[1][32:-2:],\
					 i.find("div",{"class": "text"}).contents[1][11:13:] )

			parsed_file.write(player_info.encode("utf-8"))
		if i.find("span", {"class": "label-winner"}) != None:
			#    Winner Name Slink Money 
			winner_info = "||||||||%s|||||||| ||||||||%s|||||||| ||||||||%s|||||||| ||||||||%s|||||||| \n" % \
					(i.find("span", {"class": "label-winner"}).contents[0], \
					i.find("a", {"target": "_blank"}).contents[0],\
					i.find("a", {"target": "_blank"})['href'], \
					i.find("div", {"class": "text winner"}).contents[2][28:-13:])
			parsed_file.write(winner_info.encode("utf-8"))
			

	#if file/
	un_souped.close()
	parsed_file.close()

def clean_no_winner_and_last_winner():
	#file to put stuff for now
	parsed_file = open("pars_csgojackpot_html_for_name_deposits.txt","r+")
	#lines = parsed_file.readlines()

	everyone = []

	for i in parsed_file:
		everyone.append(i.split("||||||||"))

	#values need for triming from counter
	trim_value = []
	counter = 0

	for i in everyone:
		if i[1] == "Player":
			counter += 1
		else:
			counter += 1
			trim_value.append(counter)


	# makes clean list
	clean_list = everyone[trim_value[0]-1:trim_value[-1] - 1:]

	#filters targets we care about
	filtered_list = []

	for i in clean_list:
		make_int = float(i[7])
		if i[1] == "WINNER":
			filtered_list.append(i)
		elif i[1] == "Player" and make_int >= 500:
			filtered_list.append(i)
		else:
			pass



	#Losers_list
	Losers_list = []

	winner = " "
	players = " "

	for i in filtered_list:
		

		if i[1] == "WINNER":
			winner = " "
			players = " "
			winner = i[3]
		elif i[1] == "Player" and i[3] == winner:
			pass
		else:
			Losers_list.append(i)



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




	# for i in Losers_list:
	# 	tweet = """%s (%s) just LOST %s skins valued at $%s. (https://csgojackpot.com/)"""\
	# 	 % (i[3], i[5],i[9], i[7])
	# 	api.update_status(status=tweet)

	print "=" * 25

	for i in Losers_list:
		tweet = """%s (%s) just LOST %s skins valued at $%s. (https://csgojackpot.com/) \n"""\
		 % (i[3], i[5],i[9], i[7])
		print tweet

	print "=" * 25







	#Find where the cutoffs for winners and losers are 

	#values need for triming from counter
	# filtered_trim_value = []
	
	# counter = 0

	# for i in filtered_list:
	# 	if i[1] == "Player":
	# 		counter += 1
	# 	else:
	# 		counter += 1
	# 		filtered_trim_value.append(counter)


	# len_flitered_trim_value = len(filtered_trim_value)



	# for i in range(0, len_flitered_trim_value):
	# 	winner = []
	# 	player = []

	# 	if filtered_list[filtered_trim_value[i] - 1][1] == "WINNER":
	# 		winner.append(filtered_list[filtered_trim_value[i] - 1])
	# 	else:
	# 		pass


	# 	print winner
	# 	print player

	# for i in filtered_list:
	# 	winner = []
	# 	players = []
	# 	if i[1] == "WINNER":
	# 		winner.append(i)
	# 	elif i[1] == "Player":
	# 		player.append(i)

	# 	print winner
	# 	print players
			




			

			
			





	parsed_file.close()





if __name__ == '__main__':
	get_html_csgojackpot()
	pars_main_html()
	try:
		clean_no_winner_and_last_winner()
	except Exception, e:
		pass




























	
