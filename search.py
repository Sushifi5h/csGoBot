import mechanize

def main():
	br = mechanize.Browser()
	url = br.open("http://www.yourhtmlsource.com/myfirstsite/")

	return "begin" in url.read()


if __name__ == '__main__':
	if main() == True:
		print 1
	else:
		print 0