from tkinter import *
import webbrowser as wb
import subprocess
import tkinter
import ctypes
from pyautogui import click
from pyautogui import press
from keyboard import write
from time import sleep
from PIL import ImageTk, Image
import pyautogui
import speech_recognition as sr
import time
import os
import winshell
a=Tk()
#a.geometry("1260x700")
#a.geometry("1366x768+0+0")
a.minsize(1260,700)
a.maxsize(1260,700)
a.title("Search Engine")
a.iconbitmap("ico.ico")
image1 = Image.open('google4.jpg').resize((1260,700))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=0, y=-115)
def take():
            r=sr.Recognizer()
            with sr.Microphone() as source:
                print("    listening.....")
                r.pause_threshold=1
                audio=r.listen(source,timeout=1,phrase_time_limit=5)
            try:
                print("    Recognizing......")
                recog=r.recognize_google(audio,language='en-in')
                print(f"    You said : - {a}\n")
            except:
                    print("Say that again please")
                    return "none"
            return recog
def speak():
    a=take()
    wb.open(a)
def news():
    wb.open("https://www.amarujala.com/")
    wb.open("https://www.jagran.com/sports-news-hindi.html?itm_medium=sports&itm_source=dsktp&itm_campaign=hamburger")
    wb.open("https://epaper.timesgroup.com/TOI/TimesOfIndia/index.html?a=c#")
    wb.open("https://epaper.livehindustan.com/")
def whatsapp():
    wb.open("https://web.whatsapp.com/")
def search():
    x=var.get()
    wb.open(x)
def restart():
    os.system("shutdown /r /t 1")
def sleep():
    os.system("rundll32.exe powerprof.dll,SetSuspendState 0,1,0")
def sc_shot():
    name="sanju.png"
    time.sleep(2)
    img=pyautogui.screenshot()
    img.show()
def music():
    wb.open("https://wynk.in/music")
def st_over():
    wb.open("www.stackoverflow.com")
def sw_window():
    pyautogui.keyDown("alt")
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.keyUp("alt")
def cl_window():
    pyautogui.keyDown("alt")
    pyautogui.press("f4")
    time.sleep(1)
    pyautogui.keyUp("alt")
def st_down():
    os.system("shutdown /s /t 1")
def notepad():
    subprocess.call("notepad.exe")
def you_tube():
    wb.open("https://www.youtube.com/")
def facebook():
    wb.open("https://www.facebook.com/")
def instagram():
    wb.open("https://www.instagram.com/accounts/login/")
def gmail():
    wb.open("https://mail.google.com/mail/?authuser=0&ogbl")
def chrome():
    subprocess.call("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
def edge():
    subprocess.call("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
def dev():
     subprocess.call("C:\Program Files (x86)\Dev-Cpp\devcpp.exe")
def win_lock():
    ctypes.windll.user32.LockWorkStation()
def amazon():
    wb.open("https://www.amazon.com/")
def flipcart():
    wb.open("https://www.flipkart.com/")
lb=Label(a,text="Search Engine",bg="#FFFFFD",font=("Arial",30,"bold")).place(x=520,y=10)
var=StringVar()
et=Entry(a,fg="green",font=("Arial",25),borderwidth = 8,textvariable=var)
et.insert(1,"Search By Google")
et.place(x=460,y=160)

btn=Button(a,text="Search",bd=7,font=("Arial",18,"bold"),command=search).place(x=860,y=160)
bt1=Button(a,text="Speak",bd=7,font=("Arial",18,"bold"),command=speak).place(x=990,y=160)
btn1=Button(a,text="YouTube",bd=7,font=("Arial",18,"bold"),command=you_tube).place(x=40,y=280)
btn1=Button(a,text="Facebook",bd=7,font=("Arial",18,"bold"),command=facebook).place(x=315,y=280)
btn1=Button(a,text="Instagram",bd=7,font=("Arial",18,"bold"),command=instagram).place(x=560,y=280)
btn1=Button(a,text="Gmail",bd=7,font=("Arial",18,"bold"),command=gmail).place(x=870,y=280)
btn1=Button(a,text="Chrome",bd=7,font=("Arial",18,"bold"),command=chrome).place(x=1100,y=280)

btn1=Button(a,text="Edge",bd=7,font=("Arial",18,"bold"),command=edge).place(x=55,y=380)
btn1=Button(a,text="Dev C++",bd=7,font=("Arial",18,"bold"),command=dev).place(x=325,y=380)
btn1=Button(a,text="Window Lock",bd=7,font=("Arial",18,"bold"),command=win_lock).place(x=540,y=380)
btn1=Button(a,text="Amazon",bd=7,font=("Arial",18,"bold"),command=amazon).place(x=870,y=380)
btn1=Button(a,text="Flipcart",bd=7,font=("Arial",18,"bold"),command=flipcart).place(x=1100,y=380)

btn1=Button(a,text="Stack Overflow",bd=7,font=("Arial",18,"bold"),command=st_over).place(x=10,y=480)
btn1=Button(a,text="Switch Window",bd=7,font=("Arial",18,"bold"),command=sw_window).place(x=280,y=480)
btn1=Button(a,text="Notepad",bd=7,font=("Arial",18,"bold"),command=notepad).place(x=575,y=480)
btn1=Button(a,text="Close Window",bd=7,font=("Arial",18,"bold"),command=cl_window).place(x=835,y=480)
btn1=Button(a,text="Shut Down",bd=7,font=("Arial",18,"bold"),command=st_down).place(x=1080,y=480)

btn1=Button(a,text="Restart",bd=7,font=("Arial",18,"bold"),command=restart).place(x=50,y=580)
btn1=Button(a,text="Sleep",bd=7,font=("Arial",18,"bold"),command=sleep).place(x=335,y=580)
btn1=Button(a,text="News",bd=7,font=("Arial",18,"bold"),command=news).place(x=590,y=580)
btn1=Button(a,text="Whatsapp",bd=7,font=("Arial",18,"bold"),command=whatsapp).place(x=865,y=580)
btn1=Button(a,text="Music",bd=7,font=("Arial",18,"bold"),command=music).place(x=1110,y=580)
a.mainloop()
