import utils, mechanize

def createBrowser():
	proc = mechanize.Browser()
	proc.set_handle_robots(False)
	proc.set_handle_referer(True)
	proc.set_handle_redirect(False)
	proc.set_handle_equiv(True)
	proc.addheaders = [('User-Agent', "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.5) Gecko/20060127 Netscape/8.1")]
	return proc

def bruteID(base_url, mode, param = "ID"):
	MAX_RANGE = 50

	for _id in xrange(MAX_RANGE):
		url = "%s?%s=%s" %(base_url, param, _id)
		tryingURL(url, mode)


def tryingURL(url, mode):
	try:
		proc = createBrowser()
		proc.open(url)
		status_code, status = proc.response().code, "good"
		title = proc.title()

		if not title:
			status_code, status = "Empty page", "bad"
		elif title == "Error":
			status_code, status = "Error page", "bad"
			
		return status_code

	except KeyboardInterrupt:
		utils.die("Stopped by user", "KeyboardInterrupt")

	except Exception as err:
		status_code = err
		try:
			status_code = int(str(status_code).split(" ")[2][:-1])
			status = "warn" if status_code < 400 else "bad"
							
		except:
			pass		
		return status_code
		
	finally:
		try:
			if mode == "verbose": 
				utils.printf("%s %s" %(url, status_code), status)
			elif mode == "silent" and status == "good":
				utils.printf("%s || %s" %(url, title), status)
				
			proc.close()
		except:
			pass