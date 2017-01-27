import sys, time, console, string, random, sound, os
time.sleep(0.2)
a = random.randint(1980, 2017)
start = "root@elliot:$ "
if sys.argv[1] != str("-usr"):
	time.sleep(3)
	sound.play_effect("/System/Library/Audio/UISounds/SIMToolkitNegativeACK.caf")
	print "  Usage:\n\n-usr <File> -pwd <File>\n\n\n  RoBrute Usage:\n <word>;<word>;<word>;<word>;<symbol>"
	sys.exit()
if sys.argv[3] != "-pwd":
	time.sleep(3)
	sound.play_effect("/System/Library/Audio/UISounds/SIMToolkitNegativeACK.caf")
	print "  Usage:\n\n-usr <File> -pwd <File>\n\n\n  RoBrute Usage:\n <word>;<word>;<word>;<word>;<symbol>"
	sys.exit()
sys.argv[1] = str("-usr")
sys.argv[3] = str("-pwd")
username = sys.argv[2]
password = sys.argv[4]
pwords = open(sys.argv[4], "r").readlines()
console.set_color(0,1,1)
sys.stdout.write("root@elliot:$ ")
console.set_color()
time.sleep(1)
print "elpscrk"
sound.play_effect("/System/Library/Audio/UISounds/end_record.caf")
import elplogo
time.sleep(1)
combo = len(pwords)
print "List Count: " + str(combo) + " Type: Alphanum"
time.sleep(1)
import robruteelp
