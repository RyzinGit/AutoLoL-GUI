import pyautogui
import time
import os
import threading
import tkinter as tk
from tkinter import ttk
from tkinter import *
import configparser
import sys


currentDir = os.getcwd()

def ApplyConfig(res,lang):
    global acceptPhoto,searchPhoto,normalRyzePhoto,grayRyzePhoto,grayLockinPhoto,blueLockinPhoto,redBanPhoto,grayBanPhoto,runePhoto,flashPhoto,ignitePhoto,saveNormalPhoto,saveGrayPhoto,exitButtonPhoto,ghostPhoto
    acceptPhoto = os.path.join(currentDir, "data", lang, res, "acceptButton.png")
    searchPhoto = os.path.join(currentDir,"data", lang, res, "searchButton.png")
    normalRyzePhoto = os.path.join(currentDir, "data", lang, res, "normalRyze.png")
    grayRyzePhoto = os.path.join(currentDir,"data", lang, res, "grayRyze.png")
    grayLockinPhoto = os.path.join(currentDir,"data", lang, res, "grayLockin.png")
    blueLockinPhoto = os.path.join(currentDir, "data", lang, res, "blueLockin.png")
    redBanPhoto = os.path.join(currentDir, "data", lang, res, "redBan.png")
    grayBanPhoto = os.path.join(currentDir,"data", lang, res, "grayBan.png")
    runePhoto = os.path.join(currentDir, "data", lang, res, "runePhoto.png")
    flashPhoto = os.path.join(currentDir, "data", lang, res, "flashPhoto.png")
    ignitePhoto = os.path.join(currentDir,"data", lang, res, "ignitePhoto.png")
    ghostPhoto = os.path.join(currentDir,"data", lang, res, "ghostPhoto.png")
    saveNormalPhoto = os.path.join(currentDir, "data", lang, res, "saveNormal.png")
    saveGrayPhoto = os.path.join(currentDir,"data", lang, res, "saveGray.png")
    exitButtonPhoto = os.path.join(currentDir,"data", lang, res, "exitButton.png")

icon = os.path.join(currentDir, "data", "LoLicon.ico")

status = "Not active"
pickList = []
autoRuneList = []
banList = []
stopSignal = False


def terminate():
    os._exit(0)

def Status_GUI():
    
    
    status_root = tk.Tk()
    status_root.geometry('200x100')
    status_root.title('Status')
    status_root.resizable(False,False)
    status_root.iconbitmap(icon)
    status_root.tk.call("source", "data\\azure.tcl")
    status_root.tk.call("set_theme", "dark")
    status_root.update()
    status_root.protocol('WM_DELETE_WINDOW', terminate)

    statusText = ttk.Label(status_root,text = "Status:",font = ('Ariel', 10, 'bold'))
    statusText.pack( ipadx = 1, ipady = 1)

    statusLabel = ttk.Label(status_root,text = status,font = ('Ariel', 15, 'bold'))
    statusLabel.pack(  ipadx = 3, ipady = 10)

    st = ttk.Style()
    st.configure('TButton', font=('Ariel',10 ,'bold'))

    exitButton = ttk.Button(status_root, text ="Exit", command = terminate, style='TButton',padding="1 1 1 1")
    exitButton.pack(ipadx = 1, ipady = 1)
    
    styleRed = ttk.Style()
    styleRed.configure("Red.TLabel", foreground="red")

    styleGreen = ttk.Style()
    styleGreen.configure("Green.TLabel", foreground="green")
    
    def update_label():

        global status
        statusLabel['text'] = status

        if(status == "Not active"):
            statusLabel.configure(style="Red.TLabel")
        else:
            statusLabel.configure(style= "Green.TLabel")

        status_root.after(100, update_label)

    update_label()
    status_root.mainloop()

def GUI_Func():

    pickGUI_root = tk.Tk()
    pickGUI_root.geometry('500x400')
    pickGUI_root.title('LoL Auto Pick Bot')
    pickGUI_root.resizable(False,False)
    pickGUI_root.iconbitmap(icon)
    pickGUI_root.tk.call("source", "data\\azure.tcl")
    pickGUI_root.tk.call("set_theme", "dark")
    pickGUI_root.update()
    pickGUI_root.protocol('WM_DELETE_WINDOW', terminate)
    
    pick1 = tk.StringVar()
    pick2 = tk.StringVar()
    pick3 = tk.StringVar()
    pick4 = tk.StringVar()
    pick5 = tk.StringVar()

    runeFlag1 = tk.IntVar()
    runeFlag2 = tk.IntVar()
    runeFlag3 = tk.IntVar()
    runeFlag4 = tk.IntVar()
    runeFlag5 = tk.IntVar()

    ban1 = tk.StringVar()
    ban2 = tk.StringVar()
    ban3 = tk.StringVar()
    ban4 = tk.StringVar()
    ban5 = tk.StringVar()

    resChoice = tk.StringVar()
    langChoice = tk.StringVar()

    config = configparser.ConfigParser()		
    config.read("config.ini")


    if not config.has_section("PICK"):
        config.add_section("PICK")
        config.set("PICK", "pick1", "") 
        config.set("PICK", "pick2", "")
        config.set("PICK", "pick3", "")
        config.set("PICK", "pick4", "")
        config.set("PICK", "pick5", "")

    if not config.has_section("RUNE"):
        config.add_section("RUNE")
        config.set("RUNE", "runeFlag1", "")
        config.set("RUNE", "runeFlag2","")
        config.set("RUNE", "runeFlag3","")
        config.set("RUNE", "runeFlag4","")
        config.set("RUNE", "runeFlag5","")

    if not config.has_section("BAN"):
        config.add_section("BAN")
        config.set("BAN", "ban1", "")
        config.set("BAN", "ban2", "")
        config.set("BAN", "ban3", "")
        config.set("BAN", "ban4", "")
        config.set("BAN", "ban5", "")

    if not config.has_section("RESOLUTION"):
        config.add_section("RESOLUTION")
        config.set("RESOLUTION", "Resolution", "1600x900")

    if not config.has_section("LANGUAGES"):
        config.add_section("LANGUAGES")
        config.set("LANGUAGES", "Language", "English")
        

    with open("config.ini", 'w') as configfile:
        config.write(configfile)



    picks = config['PICK']
    runes = config['RUNE']
    bans = config['BAN']
    resol = config['RESOLUTION']
    langs = config['LANGUAGES']
    
    pick1.set(picks["pick1"])
    pick2.set(picks["pick2"])
    pick3.set(picks["pick3"])
    pick4.set(picks["pick4"])
    pick5.set(picks["pick5"])

    if(runes["runeFlag1"] == "0" or runes["runeFlag1"] == "1"):
        runeFlag1.set(runes["runeFlag1"])
    if(runes["runeFlag2"] == "0" or runes["runeFlag2"] == "1"):
        runeFlag2.set(runes["runeFlag2"])
    if(runes["runeFlag3"] == "0" or runes["runeFlag3"] == "1"):
        runeFlag3.set(runes["runeFlag3"])
    if(runes["runeFlag4"] == "0" or runes["runeFlag4"] == "1"):
        runeFlag4.set(runes["runeFlag4"])
    if(runes["runeFlag5"] == "0" or runes["runeFlag5"] == "1"):
        runeFlag5.set(runes["runeFlag5"])

    ban1.set(bans["ban1"])
    ban2.set(bans["ban2"])
    ban3.set(bans["ban3"])
    ban4.set(bans["ban4"])
    ban5.set(bans["ban5"])

    resChoice.set(resol["Resolution"])
    langChoice.set(langs["Language"])
    


    left_frame = ttk.Frame(pickGUI_root, width=250, height=300)
    left_frame.grid(row=0, column=0, padx=10, pady=5,sticky= "w")

    right_frame = ttk.Frame(pickGUI_root, width=250, height=300)
    right_frame.grid(row=0, column=1, padx=30, pady=5,sticky= "e")

    bottom_frame = ttk.Frame(pickGUI_root, width=400, height=100)
    bottom_frame.grid(row=1, column=0, padx=10, pady=5,sticky= "w")

    confirm_frame = ttk.Frame(pickGUI_root, width=100, height=100)
    confirm_frame.grid(row=1, column=1, padx=0, pady=0)

    def SaveData():
        configEdit = configparser.ConfigParser()		
        configEdit.read("config.ini")

        pickList.clear()
        autoRuneList.clear()
        banList.clear()

        if(pick1.get() != None and pick1.get() != "" and len(pick1.get()) > 1):
            pickList.append(pick1.get())
        if(pick2.get() != None and pick1.get() != "" and len(pick2.get()) > 1):
            pickList.append(pick2.get())
        if(pick3.get() != None and pick1.get() != "" and len(pick3.get()) > 1):
            pickList.append(pick3.get())
        if(pick4.get() != None and pick1.get() != "" and len(pick4.get()) > 1):
            pickList.append(pick4.get())
        if(pick5.get() != None and pick1.get() != "" and len(pick5.get()) > 1):
            pickList.append(pick5.get())

        autoRuneList.append(runeFlag1.get())
        autoRuneList.append(runeFlag2.get())
        autoRuneList.append(runeFlag3.get())
        autoRuneList.append(runeFlag4.get())
        autoRuneList.append(runeFlag5.get())

        if(ban1.get() != None and ban1.get() != "" and len(ban1.get()) > 1):
            banList.append(ban1.get())
        if(ban2.get() != None and ban2.get() != "" and len(ban2.get()) > 1):
            banList.append(ban2.get())
        if(ban3.get() != None and ban3.get() != "" and len(ban3.get()) > 1):
            banList.append(ban3.get())
        if(ban4.get() != None and ban4.get() != "" and len(ban4.get()) > 1):
            banList.append(ban4.get())
        if(ban5.get() != None and ban5.get() != "" and len(ban5.get()) > 1):
            banList.append(ban5.get())

        
        with open("config.ini", 'w') as configfile:
            config['PICK']['pick1'] = pick1.get()
            config['PICK']['pick2'] = pick2.get()
            config['PICK']['pick3'] = pick3.get()
            config['PICK']['pick4'] = pick4.get()
            config['PICK']['pick5'] = pick5.get()

            config['RUNE']['runeFlag1'] = str(runeFlag1.get())
            config['RUNE']['runeFlag2'] = str(runeFlag2.get())
            config['RUNE']['runeFlag3'] = str(runeFlag3.get())
            config['RUNE']['runeFlag4'] = str(runeFlag4.get())
            config['RUNE']['runeFlag5'] = str(runeFlag5.get())

            config['BAN']['ban1'] = ban1.get()
            config['BAN']['ban2'] = ban2.get()
            config['BAN']['ban3'] = ban3.get()
            config['BAN']['ban4'] = ban4.get()
            config['BAN']['ban5'] = ban5.get()

            config["RESOLUTION"]["Resolution"] = resChoice.get()
            config["LANGUAGES"]["Language"] = langChoice.get()

            config.write(configfile)

        ApplyConfig(resChoice.get(),langChoice.get())

        if(len(pickList) == 0):
            terminate()

        pickGUI_root.destroy()



    s = ttk.Style()
    s.configure('TButton', font=('Ariel',10 ,'bold'))
        
    ttk.Label(left_frame, text="Champion Pick Preferance").grid(row=0, column=1, padx=5, pady=5)
    ttk.Label(left_frame, text="1.").grid(row=1, column=0, padx=5, pady=5)
    ttk.Label(left_frame, text="2.").grid(row=2, column=0, padx=5, pady=5)
    ttk.Label(left_frame, text="3.").grid(row=3, column=0, padx=5, pady=5)
    ttk.Label(left_frame, text="4.").grid(row=4, column=0, padx=5, pady=5)
    ttk.Label(left_frame, text="5.").grid(row=5, column=0, padx=5, pady=5)
    ttk.Entry(left_frame, textvariable = pick1).grid(row=1, column=1, padx=5, pady=5)
    ttk.Entry(left_frame, textvariable = pick2).grid(row=2, column=1, padx=5, pady=5)
    ttk.Entry(left_frame, textvariable = pick3).grid(row=3, column=1, padx=5, pady=5)
    ttk.Entry(left_frame, textvariable = pick4).grid(row=4, column=1, padx=5, pady=5)
    ttk.Entry(left_frame, textvariable = pick5).grid(row=5, column=1, padx=5, pady=5)
    ttk.Label(left_frame, text="Auto Rune").grid(row=0, column=2, padx=5, pady=5)
    ttk.Checkbutton(left_frame, variable = runeFlag1, onvalue = 1, offvalue = 0).grid(row=1, column=2, padx=5, pady=0)
    ttk.Checkbutton(left_frame, variable = runeFlag2, onvalue = 1, offvalue = 0).grid(row=2, column=2, padx=5, pady=0)
    ttk.Checkbutton(left_frame, variable = runeFlag3, onvalue = 1, offvalue = 0).grid(row=3, column=2, padx=5, pady=0)
    ttk.Checkbutton(left_frame, variable = runeFlag4, onvalue = 1, offvalue = 0).grid(row=4, column=2, padx=5, pady=0)
    ttk.Checkbutton(left_frame, variable = runeFlag5, onvalue = 1, offvalue = 0).grid(row=5, column=2, padx=5, pady=0)

    ttk.Label(right_frame, text="Champion Ban Preferance").grid(row=0, column=0, padx=5, pady=5)
    ttk.Entry(right_frame, textvariable = ban1).grid(row=1, column=0, padx=5, pady=5)
    ttk.Entry(right_frame, textvariable = ban2).grid(row=2, column=0, padx=5, pady=5)
    ttk.Entry(right_frame, textvariable = ban3).grid(row=3, column=0, padx=5, pady=5)
    ttk.Entry(right_frame, textvariable = ban4).grid(row=4, column=0, padx=5, pady=5)
    ttk.Entry(right_frame, textvariable = ban5).grid(row=5, column=0, padx=5, pady=5)

    ttk.Label(bottom_frame, text="Language").grid(row=0, column=0, padx=15, pady=5)
    ttk.Radiobutton(bottom_frame, text="English", variable=langChoice, value="English").grid(row=1, column=0, padx=5, pady=5)
    ttk.Radiobutton(bottom_frame, text="Turkish", variable=langChoice, value="Turkish").grid(row=2, column=0, padx=5, pady=5)

    ttk.Label(bottom_frame, text="Client Resolution").grid(row=0, column=1, padx=40, pady=5)
    ttk.Radiobutton(bottom_frame, text="1600x900", variable=resChoice, value="1600x900").grid(row=1, column=1, padx=5, pady=5)
    ttk.Radiobutton(bottom_frame, text="1280x720", variable=resChoice, value="1280x720").grid(row=2, column=1, padx=5, pady=5)

    ttk.Button(confirm_frame, text ="Confirm", command = SaveData, style='TButton').grid(row=0, column=0, padx=50, pady=0)


    pickGUI_root.mainloop()


def AcceptGameListener():
    
    global stopSignal
    
    acceptLocation = pyautogui.locateCenterOnScreen(acceptPhoto, confidence= 0.8)
    stopSignal = False

    if(acceptLocation) != None:
        global status
        status = "Accepting"
        th = "None"

        for th in threading.enumerate():

            if th.name == "DeclareIntent_Thread" or th.name == "ChampSelectHandler_Thread" or th.name == "ChampBanHandler_Thread" or th.name == "GetPickLocationListener_Thread":
                stopSignal = True

        time.sleep(2)
        pyautogui.moveTo(acceptLocation)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveTo(0 , pyautogui.size().height/2)
        time.sleep(5)
        
        stopSignal = False
        threading.Thread(target=GetPickLocationListener,name="GetPickLocationListener_Thread").start()

    time.sleep(1)
    threading.Thread(target=AcceptGameListener ,name="AcceptGameListener_Thread").start()

def GetPickLocationListener():

    if(stopSignal):
        sys.exit()

    searchLocation = pyautogui.locateCenterOnScreen(searchPhoto, confidence= 0.8)

    if searchLocation != None:
        global status
        status = "Getting Pick Location"
        time.sleep(1)
        pyautogui.moveTo(searchLocation)
        pyautogui.click()
        time.sleep(0.2)
        pyautogui.typewrite("ryze")
        time.sleep(1)
        
        pickLocation = pyautogui.locateCenterOnScreen(grayRyzePhoto, confidence= 0.8)
        pickLocation = pyautogui.locateCenterOnScreen(normalRyzePhoto, confidence= 0.8)
        if(pickLocation != None ):
            threading.Thread(target=DeclareIntent,args=(pickLocation,searchLocation),name="DeclareIntent_Thread").start()
        else:
            time.sleep(2)
            pickLocation = pyautogui.locateCenterOnScreen(grayRyzePhoto, confidence= 0.8)
            pickLocation = pyautogui.locateCenterOnScreen(normalRyzePhoto, confidence= 0.8)
            if(pickLocation != None ):
                threading.Thread(target=DeclareIntent,args=(pickLocation,searchLocation),name="DeclareIntent_Thread").start()
            else:
                pyautogui.moveTo(searchLocation)
                pyautogui.click()
                time.sleep(0.2)
                pyautogui.hotkey("ctrl","a")
                pyautogui.hotkey("backspace")
                time.sleep(0.2)
                pyautogui.moveTo(0 , pyautogui.size().height/2)
                time.sleep(0.5)
                threading.Thread(target=GetPickLocationListener,name="GetPickLocationListener_Thread").start()
            
    else:
        time.sleep(0.5)
        threading.Thread(target=GetPickLocationListener,name="GetPickLocationListener_Thread").start()





def DeclareIntent(pickLoc,searchLoc):
    global status
    global stopSignal

    if(stopSignal):
        sys.exit()

    if (pyautogui.locateCenterOnScreen(redBanPhoto, confidence= 0.8) != None) or (pyautogui.locateCenterOnScreen(grayBanPhoto, confidence= 0.8) != None ):
        if(len(banList) > 0):
            threading.Thread(target=ChampBanHandler,args=(pickLoc,searchLoc,0),name="ChampBanHandler_Thread").start()
            threading.Thread(target=ChampSelectHandler,args=(pickLoc,searchLoc,0),name="ChampSelectHandler_Thread").start()
            sys.exit()
        else:
            threading.Thread(target=ChampSelectHandler,args=(pickLoc,searchLoc,0),name="ChampSelectHandler_Thread").start()
            sys.exit()
        

    if (pyautogui.locateCenterOnScreen(blueLockinPhoto, confidence= 0.8) != None) or (pyautogui.locateCenterOnScreen(grayLockinPhoto, confidence= 0.8) != None ):
        threading.Thread(target=ChampSelectHandler,args=(pickLoc,searchLoc,0),name="ChampSelectHandler_Thread").start()
        sys.exit()

 
    status = "Declaring Intent"

    pyautogui.moveTo(searchLoc)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.hotkey("ctrl","a")
    pyautogui.hotkey("backspace")
    pyautogui.typewrite(pickList[0])
    time.sleep(2)
    pyautogui.moveTo(pickLoc)
    pyautogui.click()
    time.sleep(1)
    if(len(banList) > 0):
        threading.Thread(target=ChampBanHandler,args=(pickLoc,searchLoc,0),name="ChampBanHandler_Thread").start()
        threading.Thread(target=ChampSelectHandler,args=(pickLoc,searchLoc,0),name="ChampSelectHandler_Thread").start()
    else:
        threading.Thread(target=ChampSelectHandler,args=(pickLoc,searchLoc,0),name="ChampSelectHandler_Thread").start()



    

def ChampBanHandler(pickLoc,searchLoc,banIterate):

    global stopSignal
    
    if(stopSignal) or (pyautogui.locateCenterOnScreen(blueLockinPhoto, confidence= 0.8) != None) or (pyautogui.locateCenterOnScreen(grayLockinPhoto, confidence= 0.8) != None ):
        sys.exit()

    if((pyautogui.locateCenterOnScreen(redBanPhoto, confidence= 0.8) != None) or (pyautogui.locateCenterOnScreen(grayBanPhoto, confidence= 0.8) != None )):
        
        global status

        if((banIterate + 1) > len(banList)):
            sys.exit()

        status = "Ban phase"
        pyautogui.moveTo(searchLoc)
        pyautogui.click()
        time.sleep(0.2)
        pyautogui.hotkey("ctrl","a")
        pyautogui.hotkey("backspace")
        pyautogui.typewrite(banList[banIterate])
        time.sleep(2)
        pyautogui.moveTo(pickLoc)
        pyautogui.click()
        time.sleep(1)
        banLoc = pyautogui.locateCenterOnScreen(redBanPhoto, confidence= 0.8)

        if(banLoc != None):
            pyautogui.moveTo(banLoc)
            pyautogui.click()
            time.sleep(0.2)
            pyautogui.moveTo(searchLoc) #to move mouse away from image
            time.sleep(2.5)
            if((pyautogui.locateCenterOnScreen(redBanPhoto, confidence= 0.8) != None) or (pyautogui.locateCenterOnScreen(grayBanPhoto, confidence= 0.8) != None )):
                banIterate+=1
                time.sleep(0.2)
                threading.Thread(target=ChampBanHandler,args=(pickLoc,searchLoc,banIterate),name="ChampBanHandler_Thread").start()
            else:
                sys.exit()
        else:
            banIterate+=1
            time.sleep(0.2)
            threading.Thread(target=ChampBanHandler,args=(pickLoc,searchLoc,banIterate),name="ChampBanHandler_Thread").start()
    else:
        time.sleep(0.5)
        threading.Thread(target=ChampBanHandler,args=(pickLoc,searchLoc,banIterate),name="ChampBanHandler_Thread").start()

def ChampSelectHandler(pickLoc,searchLoc,champIterate):

    global stopSignal
    if(stopSignal):
        sys.exit()

    if((pyautogui.locateCenterOnScreen(blueLockinPhoto, confidence= 0.8) != None) or (pyautogui.locateCenterOnScreen(grayLockinPhoto, confidence= 0.8) != None )):
        global status
        status = "Selecting Champion"
        time.sleep(0.3)
        pyautogui.moveTo(searchLoc)
        pyautogui.click()
        time.sleep(0.2)
        pyautogui.hotkey("ctrl","a")
        pyautogui.hotkey("backspace")
        if((champIterate + 1) > len(pickList)):
            champIterate = 0
        pyautogui.typewrite(pickList[champIterate])
        time.sleep(1.5)
        pyautogui.moveTo(pickLoc)
        pyautogui.click()
        time.sleep(0.3)
        lockinLoc = pyautogui.locateCenterOnScreen(blueLockinPhoto, confidence= 0.8)
        if(lockinLoc != None):
            pyautogui.moveTo(lockinLoc)
            pyautogui.click()
            time.sleep(0.2)
            pyautogui.moveTo(searchLoc) #to move mouse away from image
            time.sleep(1)

            if((pyautogui.locateCenterOnScreen(blueLockinPhoto, confidence= 0.8) != None) or (pyautogui.locateCenterOnScreen(grayLockinPhoto, confidence= 0.8) != None )):
                champIterate+=1
                threading.Thread(target=ChampSelectHandler,args=(pickLoc,searchLoc,champIterate),name="ChampSelectHandler_Thread").start()

            elif autoRuneList[champIterate] == 1:
                AutoRuneFunc()
            else:
                sys.exit()
                
        else:
            champIterate+=1
            time.sleep(0.2)
            threading.Thread(target=ChampSelectHandler,args=(pickLoc,searchLoc,champIterate),name="ChampSelectHandler_Thread").start()
    else:
        time.sleep(0.2)
        threading.Thread(target=ChampSelectHandler,args=(pickLoc,searchLoc,champIterate),name="ChampSelectHandler_Thread").start()

def AutoRuneFunc():

    global stopSignal
    if(stopSignal):
        sys.exit()

    runPhotoLoc = pyautogui.locateCenterOnScreen(runePhoto, confidence= 0.8)


    if(runPhotoLoc != None):
        global status
        status = "Selecting Rune"
        pyautogui.moveTo(runPhotoLoc)
        pyautogui.click()
        time.sleep(2.5)
        
        flashPhotoLoc = pyautogui.locateCenterOnScreen(flashPhoto, confidence= 0.8)
        ignitePhotoLoc = pyautogui.locateCenterOnScreen(ignitePhoto, confidence= 0.8)
        ghostPhotoLoc = pyautogui.locateCenterOnScreen(ghostPhoto, confidence= 0.8)
        chooseRuneLoc = None

        if flashPhotoLoc != None:
            chooseRuneLoc = flashPhotoLoc
        elif ignitePhotoLoc != None:
            chooseRuneLoc = ignitePhotoLoc
        elif ghostPhotoLoc != None:
            chooseRuneLoc = ignitePhotoLoc
        
        if(chooseRuneLoc != None):

            pyautogui.moveTo(chooseRuneLoc)
            pyautogui.click()
            time.sleep(2)

            saveNormalPhotoLoc = pyautogui.locateCenterOnScreen(saveNormalPhoto, confidence= 0.8)
            saveGrayPhotoLoc = pyautogui.locateCenterOnScreen(saveGrayPhoto, confidence= 0.8)
            saveLoc = None

            if saveNormalPhotoLoc != None:
                saveLoc = saveNormalPhotoLoc
            elif saveGrayPhotoLoc != None:
                saveLoc = saveGrayPhotoLoc

            if(saveLoc != None):
                pyautogui.moveTo(saveLoc)
                pyautogui.click()
                time.sleep(0.5)
                exitButtonPhotoLoc = pyautogui.locateCenterOnScreen(exitButtonPhoto, confidence= 0.8)
                if(exitButtonPhotoLoc != None):
                    pyautogui.moveTo(exitButtonPhotoLoc)
                    pyautogui.click()
                    sys.exit()

ApplyConfig("1600x900","English")
GUI_Func()
threading.Thread(target=Status_GUI,name="Status_GUI_Thread").start()
threading.Thread(target=AcceptGameListener ,name="AcceptGameListener_Thread").start()
threading.Thread(target=GetPickLocationListener,name="GetPickLocationListener_Thread").start()
status = "Active"