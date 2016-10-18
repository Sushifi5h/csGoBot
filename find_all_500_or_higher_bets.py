import re







def find_all_500_or_higher_bets():
	#look at clean_name_money_winners.txt & pull out all bets higher than 500


	#open file containing all names
	all_names = open("/home/vik/Projects/Pratice/clean_name_money_winner.txt","r")

	#new file to be written also clean file
	open('/home/vik/Projects/Pratice/find_all_500_or_higher_bets.txt', 'w').close()
	all_500_or_higher = open("/home/vik/Projects/Pratice/find_all_500_or_higher_bets.txt","r+")


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
		else: 
			pass
			print 1

	all_names.close()
	all_500_or_higher.close


if __name__ == '__main__':
	find_all_500_or_higher_bets()