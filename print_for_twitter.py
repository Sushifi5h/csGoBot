import re



def print_for_twitter():
	#Make file for so python can easily publish datat


	#Get losers
	losers = open("/Users/vikramsingh/Desktop/Pratice/compare_winners_losers.txt","r")

	#write in new file
	print_for_twitter = open("/Users/vikramsingh/Desktop/Pratice/print_for_twitter.txt","r+")

	#Trying some magic
	for i in losers.readlines():
		x = re.sub("[^\w]", " ",  i).split()
		text = '%s just lost $ %s worth of skins RIP SKINS (https://csgojackpot.com/).\n' % (x[0], x[1])
		print_for_twitter.write(text)

	#close files
	losers.close()
	print_for_twitter.close()















if __name__ == '__main__':
	print_for_twitter()