import re




def get_name_deposit():
	#Main function is to only name and deposit from parsed html file
	#Name: name Desposit: money
	#Name: name Desposit: name <- winner


	#open parsed_csgojackpot_html
	parsed_csgojackpot_html = open("/Users/vikramsingh/Desktop/Pratice/pars_csgojackpot_html_for_name_deposits.txt","r")


	#open new file to be written in
	open('/Users/vikramsingh/Desktop/Pratice/clean_name_money_winner.txt', 'w').close()
	clean_name_money_winner =  open("/Users/vikramsingh/Desktop/Pratice/clean_name_money_winner.txt","r+")


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




if __name__ == '__main__':
	get_name_deposit()