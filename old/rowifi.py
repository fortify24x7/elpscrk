import sys, console, time, random, string, os, sound
from datetime import timedelta
name = 'wifipass' + '.data'
yn = raw_input("Educated Wifi Brute Force? y/n: ")
if yn != "y":
	sys.exit()
dell = raw_input("Delete Last Log? y/n: ")
if dell == "y":
	try:
		sound.play_effect("/System/Library/Audio/UISounds/payment_success.caf")
		os.remove(name)
	except:
		pass
if yn == "y":
	console.set_color(0,1,1)
	sys.stdout.write("elpscrk$: ")
	console.set_color()
	hint1 = raw_input("WiFi Name: ")
	hint1a = hint1.lower()
	hint1b = hint1.upper()
	console.set_color(0,1,1)
	sys.stdout.write("elpscrk$: ")
	console.set_color()
	hint2 = raw_input("Alternative Name: ")
	hint2a = hint2.lower()
	hint2b = hint2.upper()
	console.set_color(0,1,1)
	sys.stdout.write("elpscrk$: ")
	console.set_color()
	hint3 = raw_input("Owner: ")
	hint3a = hint3.lower()
	hint3b = hint3.upper()
	if hint1 == "''":
		hint1 = ''
	if hint2 == "''":
		hint2 = ''
	if hint3 == "''":
		hint3 = ''
start_time = time.time()
for i in range(1):
	combo = 1
	try:
		sys.stdout.write("\r" + "Running Loop " + str(i + 1) + " of " + str(combo))
		sys.stdout.flush()
		time.sleep(0.02)
		if yn == "y":
			a1 = hint1
			a2 = hint1a
			a3 = hint1b
			a4 = hint2
			a5 = hint2a
			a6 = hint2b
			a7 = "Wifi"
			a8 = a7.lower()
			a9 = a7.upper()
			a10 = "Password"
			a11 = a10.lower()
			a12 = a10.upper()
			a13 = "Guest"
			a14 = a13.lower()
			a15 = a13.upper()
			a16 = hint3
			a17 = hint3a
			a18 = hint3b
			b1 = hint1 + a7
			b2 = hint1 + a8
			b3 = hint1 + a9
			b4 = hint1a + a7
			b5 = hint1a + a8
			b6 = hint1a + a9
			b7 = hint1b + a7
			b8 = hint1b + a8
			b9 = hint1b + a9
			b10 = hint2 + a7
			b12 = hint2 + a8
			b13 = hint2 + a9
			b14 = hint2a + a7
			b15 = hint2a + a8
			b16 = hint2a + a9
			b17 = hint2b + a7
			b18 = hint2b + a8
			b19 = hint2b + a9
			b20 = hint3 + a7
			b21 = hint3 + a8
			b22 = hint3 + a9
			b23 = hint3a + a7
			b24 = hint3a + a8
			b25 = hint3a + a9
			b26 = hint3b + a7
			b27 = hint3b + a8
			b28 = hint3b + a9
			
			a7 = "_Wifi"
			a8 = a7.lower()
			a9 = a7.upper()
			a10 = "_Password"
			a11 = a10.lower()
			a12 = a10.upper()
			a13 = "_Guest"
			a14 = a13.lower()
			a15 = a13.upper()
			a16 = hint3
			a17 = hint3a
			a18 = hint3b
			
			c1 = hint1 + a7
			c2 = hint1 + a8
			c3 = hint1 + a9
			c4 = hint1a + a7
			c5 = hint1a + a8
			c6 = hint1a + a9
			c7 = hint1b + a7
			c8 = hint1b + a8
			c9 = hint1b + a9
			c10 = hint2 + a7
			c12 = hint2 + a8
			c13 = hint2 + a9
			c14 = hint2a + a7
			c15 = hint2a + a8
			c16 = hint2a + a9
			c17 = hint2b + a7
			c18 = hint2b + a8
			c19 = hint2b + a9
			c20 = hint3 + a7
			c21 = hint3 + a8
			c22 = hint3 + a9
			c23 = hint3a + a7
			c24 = hint3a + a8
			c25 = hint3a + a9
			c26 = hint3b + a7
			c27 = hint3b + a8
			c28 = hint3b + a9
			
			a7 = "-Wifi"
			a8 = a7.lower()
			a9 = a7.upper()
			a10 = "-Password"
			a11 = a10.lower()
			a12 = a10.upper()
			a13 = "-Guest"
			a14 = a13.lower()
			a15 = a13.upper()
			a16 = hint3
			a17 = hint3a
			a18 = hint3b
			
			e1 = hint1 + a7
			e2 = hint1 + a8
			e3 = hint1 + a9
			e4 = hint1a + a7
			e5 = hint1a + a8
			e6 = hint1a + a9
			e7 = hint1b + a7
			e8 = hint1b + a8
			e9 = hint1b + a9
			e10 = hint2 + a7
			e12 = hint2 + a8
			e13 = hint2 + a9
			e14 = hint2a + a7
			e15 = hint2a + a8
			e16 = hint2a + a9
			e17 = hint2b + a7
			e18 = hint2b + a8
			e19 = hint2b + a9
			e20 = hint3 + a7
			e21 = hint3 + a8
			e22 = hint3 + a9
			e23 = hint3a + a7
			e24 = hint3a + a8
			e25 = hint3a + a9
			e26 = hint3b + a7
			e27 = hint3b + a8
			e28 = hint3b + a9
			
			a7 = "Wifi"
			a8 = a7.lower()
			a9 = a7.upper()
			a10 = "Password"
			a11 = a10.lower()
			a12 = a10.upper()
			a13 = "Guest"
			a14 = a13.lower()
			a15 = a13.upper()
			a16 = hint3
			a17 = hint3a
			a18 = hint3b
			
			f1 = a1 + a7
			f2 = a1 + a8
			f3 = a1 + a9
			f4 = a1 + a10
			f5 = a1 + a11
			f6 = a1 + a12
			f7 = a1 + a13
			f8 = a1 + a14
			f9 = a1 + a15
			f10 = a1 + a16
			f11 = a1 + a17
			f12 = a1 + a18
			
			g1 = a2 + a7
			g2 = a2 + a8
			g3 = a2 + a9
			g4 = a2 + a10
			g5 = a2 + a11
			g6 = a2 + a12
			g7 = a2 + a13
			g8 = a2 + a14
			g9 = a2 + a15
			g10 = a2 + a16
			g11 = a2 + a17
			g12 = a2 + a18
	except:
		pass
file = file(name,'a')
n = "\n"
list1 = a1 + n + a2 + n + a3 + n + a4 + n + a5 + n + a6 + n + a7 + n + a8 + n + a9 + n + a10 + n + a11 + n + a12 + n + a13 + n + a14 + n + a15 + n + a16 + n + a17 + n + a18 + n + b1 + n + b2 + n + b3 + n + b4 + n + b5 + n + b6 + n + b7 + n + b8 + n + b9
list2 = b10 + n + b12 + n + b13 + n + b14 + n + b15 + n + b16 + n + b17 + n + b18 + n + b19 + n + b20 + n + b21 + n + b22 + n + b23 + n + b24 + n + b25 + n + b26 + n + b27  + n + b28
list3 = c1 + n + c2 + n + c3 + n + c4 + n + c5 + n + c6 + n + c7 + n + c8 + n + c9 + n + c10 + n + c12 + n + c13 + n + c14 + n + c15 + n + c16 + n + c17 + n + c18 + n + c19 + n + c20 + n + c21 + n + c22 + n + c23 + n + c24 + n + c25 + n + c26 + n + c27 + n + c28
list4 = e1 + n + e2 + n + e3 + n + e4 + n + e5 + n + e6 + n + e7 + n + e8 + n + e9 + n + e10 + n + e12 + n + e13 + n + e14 + n + e15 + n + e16 + n + e17 + n + e18 + n + e19 + n + e20 + n + e21 + n + e22 + n + e23 + n + e24 + n + e25 + n + e26 + n + e27 + n + e28
list5 = f1 + n + f2 + n + f3 + n + f4 + n + f5 + n + f6 + n + f7 + n + f8 + n + f9 + n + f10 + n + f11 + n + f12 + n + g1 + n + g2 + n + g3 + n + g4 + n + g5 + n + g6 + n + g7 + n + g8 + n + g9 + n + g10 + n + g11 + n + g12
file.write(list1)
file.write(list2)
file.write(list3)
file.write(list4)
file.write(list5)
file.write("""\n----------------------------\n\n       LEAVE ME HERE!\n
----------------------------\n
""")
file.close()
elapsed_time = time.time() - start_time
print "\n"
time.sleep(0.5)
times = str(timedelta(seconds=elapsed_time))
console.set_color(0,1,1)
sys.stdout.write("Time Elapsed: ")
console.set_color()
sys.stdout.write(str(times))
