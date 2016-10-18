import re



def print_for_twitter():
	#Make file for so python can easily publish datat


	#Get losers
	losers = open("testing.txt","r")

	#write in new file
	print_for_twitter = open("new_test.txt","r+")

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
	print_for_twitter()