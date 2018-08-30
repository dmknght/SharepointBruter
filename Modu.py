#!/usr/bin/python

try:
	from lib import utils, wordlist, actions
except Exception as ImportErr:
	print("Error while importing modules\n%s" %(ImportError))
	
try:
	import sys, mechanize, ssl
except Exception as ImportErr:
	print("Error while importing system library\n%s" %(ImportErr))
	

RUNNING_MODE = "silent"

ssl._create_default_https_context = ssl._create_unverified_context

def help():
	return 	"""USAGE: python Modu.py <URL> <MODULE>\n
	URL:\t{required}\tTarget Homepage
	MODULE:\t{required}\tModule name for testing
	\nEx: python Modu.py <URL> SystemAdmin,UserAccount,adduser
	"""

# def bruteID(base_url, param = "ID"):
# 	for _id in xrange(MAX_RANGE):
# 		url = "%s?%s=%s" %(base_url, param, _id)
# 		actions.tryingURL(url, RUNNING_MODE)


def main(base_url, test_modules):
	try:
		for module in test_modules:
			url = "%sLists/%s/AllItems.aspx" %(base_url, module)
			actions.tryingURL(url, RUNNING_MODE)
			
			url = "%sLists/%s/DispForm.aspx" %(base_url, module)

			actions.bruteID(url, RUNNING_MODE) if actions.tryingURL(url, RUNNING_MODE) < 300 else None

	except KeyboardInterrupt:
		utils.die("Stopped by user", "KeyboardInterrupt")
	except Exception as RuntimeErr:
		utils.die("Runtime error", RuntimeErr)

if __name__ == "__main__":
	if len(sys.argv) == 2 and sys.argv[1] == "help":
		utils.printf(help(), "good")
	elif len(sys.argv) == 3:
		target = sys.argv[1]
		module = sys.argv[2].split(",") if "," in sys.argv[2] else sys.argv[2].split()		
	else:
		utils.die("Invalid option", help())
		
	if "http" not in target:
		target = "http://%s" %(target)
	if target[-1] != "/":
		target += "/"
		
	main(target, module)
