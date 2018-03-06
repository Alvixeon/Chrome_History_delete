import getpass,os
global PTHC

username = getpass.getuser()
PTHC = "C:\\Users\\%s\\AppData\\Local\\Google\\Chrome\\User Data\\Default" % username

def Delete_History():
    cdir = os.getcwd()
    if cdir != PTHC:
        os.chdir(PTHC)
    else:
        pass
    PTHCLS = os.listdir(os.getcwd())
    for i in PTHCLS:
        if i == "History":
            try:
                os.remove(i)
            except:
                try:
                    os.system("taskkill /IM chrome.exe /F")
                except:
                    pass
    
Delete_History()
