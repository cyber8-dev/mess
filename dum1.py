import os,sys,json,requests,re,time
from time import sleep as waktu 

M = '\x1b[1;91m' 
H = '\x1b[1;92m'
C = '\x1b[0m' 

banner = ('''

   D U M P 

''')

def folder():
	try:os.mkdir('DUMP')
	except:pass

id = []

def masuk():
	os.system('clear')
	cookie = input (f'\n masukan coki > ')
	if cookie =='':
		exit (f'{M} isi yg bener tolol{C}')
	with requests.Session() as REQ:
		try:
			get_tok = REQ.get('https://business.facebook.com/business_locations',headers = {"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
			token = re.search("(EAAG\w+)", get_tok.text).group(1)
			coki = {"cookie":cookie}
			open('coki.txt','w').write(cookie)
			open('token.txt','w').write(token)
			time.sleep(2)
			Menu(token,coki)
		except KeyError:
			os.system('rm -rf token.txt')
			os.system('rm -rf coki.txt')
			masuk()
def Menu(token,coki):
	os.system('clear')
	print (banner)
	try:
		r = requests.get(f'https://graph.facebook.com/me?access_token={token}',cookies=coki)
		c = json.loads(r.text)
		nama = c['name']
	except (KeyError):
		os.system('rm -rf token.txt')
		masuk()
	print (f'{C} halo {H}{nama}{C}\n ')
	try:
		folder()
		print (' isi me jika ingin dump teman sendiri ')
		uid = input (' masukan id publik : ')
		simpan = input (' simpan nama file : ')
		file = ('DUMP/'+simpan+'.txt').replace(' ', '_')
		cok = open(file, 'w')
		r = requests.get("https://graph.facebook.com/v13.0/%s?fields=friends.limit(5000)&access_token=%s"%(uid,token),cookies=coki)
		z = json.loads(r.text)
		for a in z['friends']['data']:
			id.append(a['id']+'|'+a['name'])
			cok.write(a['id']+'|'+a['name'] + '\n')
			sys.stdout.write (f'\r mengumpulkan id : {str(len(id))} ')
			sys.stdout.flush();waktu(000.01)
			
		cok.close()
		print ('\n\n berhasil dump id')
		print (f' file dump tersimpan : {file}')
		input (' ENTER')
		masuk()
	except Exception as e:
		exit (e)
		
		
masuk()