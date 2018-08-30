import sys

def printf(mtext, mtype = 'warn'):
	############################################
	#	Print text w/ color
	#
	###########################################

	print(craft_msg(mtext, mtype))

def craft_msg(mtext, mtype = 'warn'):
	####################################################
	#	create text message with color
	#	bad: red
	#	warn: yellow
	#	good: light green
	#	This functions is using for Linux terminal only
	####################################################

	mtext = {
		'bad': '\033[91m{}\033[00m'.format(mtext),
		'warn': '\033[93m{}\033[00m'.format(mtext),
		'good': '\033[92m{}\033[00m'.format(mtext),
	}
	return (mtext[mtype])
	
def die(msg, error):
	printf(msg, "bad")
	printf(error, "bad")
	sys.exit(1)
	