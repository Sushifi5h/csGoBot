import re




def compare_all_500_or_greater_to_winners():
	#THERE IS WAY TOO MUCH MAGIC FOR ME TO EXPLAIN


	#open both files
	all_500 = open("/Users/vikramsingh/Desktop/Pratice/find_all_500_or_higher_bets.txt","r")
	all_winners = open("/Users/vikramsingh/Desktop/Pratice/list_winners.txt","r")

	#new file to be written in
	open('/Users/vikramsingh/Desktop/Pratice/compare_winners_losers.txt', 'w').close()
	clean_name_money_winner =  open("/Users/vikramsingh/Desktop/Pratice/compare_winners_losers.txt","r+")

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
				if n in open('/Users/vikramsingh/Desktop/Pratice/list_winners.txt').read():
					pass
				else:
					losers.append(i)


	for i in losers:
		data = '%s \n' % (i)
		clean_name_money_winner.write(data)

	all_500.close
	all_winners.close
	clean_name_money_winner.close()


if __name__ == '__main__':
	compare_all_500_or_greater_to_winners()
