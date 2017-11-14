import sys, time, console, string, random, sound, os, argparse
time.sleep(0.2)
a = random.randint(1980, 2017)
start = "root@elliot:$ "

def help():
	time.sleep(3)
	sound.play_effect("/System/Library/Audio/UISounds/SIMToolkitNegativeACK.caf")
	print "  Usage:\n\n-u <File> -p <File>\n\n\n  RoBrute Usage:\n <word>;<word>;<word>;<word>;<symbol>"
	print "\n Read Usage.md for more information."
	sys.exit()

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--usr")
parser.add_argument("-p", "--pwd")
args = parser.parse_args()

if not args.usr or not args.pwd:
	help()
	sys.exit(0)

username = args.usr
password = args.pwd

console.set_color(0,1,1)
sys.stdout.write("root@elliot:$ ")
console.set_color()
time.sleep(1)
print "elpscrk"
sound.play_effect("/System/Library/Audio/UISounds/end_record.caf")
import elplogo
time.sleep(1)
combo = len("26829263")
print "List Count: " + str(combo) + " Type: Alphanum"
time.sleep(1)
import robrute
