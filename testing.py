import re


losers = open("compare_winners_losers.txt", "r")
everyone = open("pars_csgojackpot_html_for_name_deposits.txt", "r")
open("testing.txt", "r+").close()
testing = open("testing.txt", "r+")


for i in losers.readlines():
	make = re.sub("[^\w]", " ",  i).split()
	with open("pars_csgojackpot_html_for_name_deposits.txt") as f:
		for line in f:
			search = "(valued at $" + make[1]
			if search in line:
				testing.write(line)


losers.close()
everyone.close()
testing.close()