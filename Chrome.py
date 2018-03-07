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
    PTHC_LS = os.listdir(os.getcwd())
    for i in PTHC_LS:
        if i == "History":
            try:
                os.remove(i)
            except:
                try:
                    os.system("taskkill /IM chrome.exe /F")
                    Delete_History()
                except:
                    pass
    
Delete_History()
