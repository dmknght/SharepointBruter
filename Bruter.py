#!/usr/bin/python

try:
	from lib import utils, wordlist, actions
except Exception as ImportErr:
	print("Error while importing modules\n%s" %(ImportError))
	
try:
	import sys, mechanize, ssl
except Exception as ImportErr:
	print("Error while importing system library\n%s" %(ImportErr))

ssl._create_default_https_context = ssl._create_unverified_context

RUNNING_MODE = "silent"

def help():
	return """Usage: python Bruter.py <URL> [MODE]\n
	URL:\t{required}\tTarget Homepage
	MODE:\t{optional}\t[verbose / silent]\t(Default: silent)
	"""

def main(base_url):
	try:
		for path in wordlist.listDefault().replace("\t", "").split("\n"):
			url = base_url + path
			actions.tryingURL(url, RUNNING_MODE)

		for line in wordlist.listSub().replace("\t", "").split("\n"):
			path, param = line.split("?")
			url = base_url + path
			actions.bruteID(url, RUNNING_MODE, param) if actions.tryingURL(url, RUNNING_MODE) < 300 else None
			
	except KeyboardInterrupt:
		utils.die("Stopped by user", "KeyboardInterrupt")
	except Exception as RuntimeErr:
		utils.die("Runtime error", RuntimeErr)


if __name__ == "__main__":
	if len(sys.argv) == 2:
		option = sys.argv[1]
	elif len(sys.argv) == 3:
		option = sys.argv[1]
		RUNNING_MODE = sys.argv[2] if sys.argv[2] in ("silent", "verbose") else utils.die("Invalid option", "Unknow mode")

	else:
		utils.die("Invalid option", help())
		
	if option == "help":
		utils.printf(help(), "good")
	else:
		if "http" not in option:
			option = "http://%s" %(option)
		if option[-1] != "/":
			option += "/"
		main(option)