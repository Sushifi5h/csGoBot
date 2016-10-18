import re





def list_winners():
	#Main function is to list winners

	#open all names deposits
	all_names = open("/Users/vikramsingh/Desktop/Pratice/clean_name_money_winner.txt","r")

	#new file to be written in
	open('/Users/vikramsingh/Desktop/Pratice/list_winners.txt', 'w').close()
	clean_name_money_winner =  open("/Users/vikramsingh/Desktop/Pratice/list_winners.txt","r+")


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

if __name__ == '__main__':
	list_winners()