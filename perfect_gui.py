from tkinter import Label,Entry,Text,Button,messagebox,filedialog,Tk,Menu,INSERT,DISABLED,FALSE, END, simpledialog
from PIL import Image, ImageTk
from threading import Thread, Timer, main_thread
import socket
import time
import sys
import pyttsx3 #pip install pyttsx3 , pip install -U pyttsx3==2.71 (For Speak)
import datetime 
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui #pip install pyautogui (For Screenshot)
import psutil #pip install psutil
import pyjokes #pip install pyjokes
import random
import string
import operator
import json
import wolframalpha
import time
from urllib.request import urlopen
import requests
import winshell

# few paths and APIs
videoFilesPath = r"C:\Users\z8003\Downloads\Video"
AudioFilesPath = r"C:\Users\z8003\Downloads\Music"
screeshotSavePath = r"C:\Users\{}\Downloads\{}.png".format(os.getenv('username'), ''.join(random.choices(string.ascii_letters + string.digits, k=20)))
wordAppLocation = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word 2016.lnk"

toiNewsapi = '<Your_Api>' # https://newsapi.org/
weatherApi = '<Your_Api>'  # https://openweathermap.org/api
wolframAlphaApi = '<Your_Api>' # https://products.wolframalpha.com/simple-api/documentation/

gmailLoginData = ('<Your_Email>', '<Your_pass>')


# voice code for output starts
engine = pyttsx3.init("sapi5")

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)
engine.setProperty('volume', 1)


def speak(audio):  #speak method defined
    engine.say(audio)
    engine.runAndWait()


# Code to check internet
def Isconnect():      #method to check internet 
    print("Checking Internet.....")
    try:
        socket.create_connection(("www.google.com", 80))
        neticon.config(image=connlogo)
        nettext.config(text="Connected :)", fg="green")
        return True
    except OSError:
        pass
    neticon.config(image=notconn)
    nettext.config(text="No Internet ;( ", fg="red")
    return False

defcolor = "blue"
# wishe me code here
def wisheme():       #method to wisheme at the beginning
    update("Welcome back MAK!", "green")
    speak("Welcome back MAK!")
    time_()
    date()
    hour = int(datetime.datetime.now().hour)
    if hour >=6 and hour<12:
        update("Good Morning Sir","green")
        speak("Good Morning Sir")
    elif hour >=12 and hour<18:
        update("Good Afternoon Sir!","green")
        speak("Good Afternoon Sir!")
    elif hour >=18 and hour <24:
        update("Good Evening Sir!","green")
        speak("Good Evening Sir!")
    else:
        update("Good Night Sir!","green")
        speak("Good Night Sir!")

    update("Jarvis at your service. Please tell me how can I help you?","yellow")
    speak("Jarvis at your service. Please tell me how can I help you?")


def update(message,color):           #method which update the message box
    msg.configure(state='normal')
    msg.delete('1.0', END)
    msg.insert('end', message)
    msg.configure(state='disabled')

    # msg.config(text=message,fg=color)


def TakeCommand():         #method which recives audio input
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        update("Listening....","green")
        speak("Listening.....")
        r.pause_threshold = 0.8
        
        r.energy_threshold = 500
        audio = r.listen(source,phrase_time_limit=5)
    try:
        update("Recognising....","orange")
        Isinternet = Isconnect()
        print("Connected" if Isinternet else "Not Connected")
        if (Isinternet):
            query = r.recognize_google(audio, language="en-IN")
        else:
            update("You are not connected to the internet.","yellow")
            speak("You are not connected to the internet.")
            return None

        print("You Said", query)
        update(f"You Said: {query} ","green")
        time.sleep(1)


    except Exception as e:
        print(e)
        print("say that again please...")
        update("Say That Again Please !!","red")
        speak("say that again please...")
        return None

    return query

def time_():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    Time12=datetime.datetime.now().strftime("%I:%M:%S")
    
    update(f"the current time is {strTime}  or   {Time12}","red")
    speak(f"the current time is {strTime}  or   {Time12}")

def date():
    year = (datetime.datetime.now().year)
    month = (datetime.datetime.now().month)
    date = (datetime.datetime.now().day)
    speak("the current date is")
    update(f"Date is {date}-{month}-{year}","red")
    speak(date)
    speak(month)
    speak(year)

def sendEmail(to, content):
    sender = gmailLoginData
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Enable low security in gmail 
    server.login(sender[0], sender[1])
    server.sendmail(sender[0], to, content)
    server.close()
def screenshot():
    img = pyautogui.screenshot()
    img.save(screeshotSavePath)
def cpu():
    usage = str(psutil.cpu_percent())
    battery = psutil.sensors_battery()
    update('CPU is at '+ str(usage) + "\nBattery is at " + str(battery.percent), 'yellow')
    speak('CPU is at'+ usage)
    speak("Battery is at")
    speak(battery.percent)
def jokes():
    update(pyjokes.get_joke(), 'yellow')
    speak(pyjokes.get_joke())

def Introduction():
    update("I am JARVIS 1.0 , Personal AI assistant ,\nI am created by MAK , \nI can help you in various regards , \nI can search for you on the Internet , \nI can also grab definitions for you from wikipedia , \nIn layman terms , I can try to make your life a bed of roses , \nWhere you just have to command me , and I will do it for you ",'yellow')

    speak("I am JARVIS 1.0 , Personal AI assistant , "
    "I am created by MAK , "
    "I can help you in various regards , "
    "I can search for you on the Internet , "
    "I can also grab definitions for you from wikipedia , "
    "In layman terms , I can try to make your life a bed of roses , "
    "Where you just have to command me , and I will do it for you , ")

def Creator():
    update("MAK is an extra-ordinary person ,\nHe has a passion for Robotics, Artificial Intelligence and Machine Learning ,\nHe is very co-operative ,\nIf you are facing any problem regarding the 'Jarvis', He will be glad to help you ",'yellow')
    speak("MAK is an extra-ordinary person ,"
    "He has a passion for Robotics, Artificial Intelligence and Machine Learning ,"
    "He is very co-operative ,"
    "If you are facing any problem regarding the 'Jarvis', He will be glad to help you ")
    
flag = 1
message = "OFF"
terminate = 0

session=1
def runnow():        #method which starts execution on started method
    global session
    if session==1:
        # wisheme()
        session=0
    
    count = 0
    
    while 1:
        if main_thread().is_alive():
            pass
        else:
            break
        if terminate == 1:
            break
        query = TakeCommand()
        
        if query != None:
            query = query.lower()
            speak(f"You Said :{query} ")
        else:
            continue

        # All the commands said by user will be 
		# stored here in 'query' and will be 
		# converted to lower case for easily 
		# recognition of command 

        if 'time' in query:
            time_()
        elif 'date' in query:
            date()
        elif 'how are you' in query:
            update("I am fine, Sir Thanks for asking \nHow are you?", "yellow")
            speak("I am fine, Sir Thanks for asking")
            speak("How are you Sir?")
            query = TakeCommand()
            if query == None:
                continue
            elif 'fine' in query or "good" in query: 
                speak("It's good to know that your fine")
            elif query != None:
                speak("I hope you get well soon.")
        elif 'wikipedia' in query:
            update("Searching...",'yellow')
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            update(result,'yellow')
            speak(result)
        elif 'open youtube' in query:
            update("What should I search?",'yellow')
            speak("What should I search?")
            Search_term = TakeCommand()
            update("Here we go to Youtube\n",'yellow')
            speak("Here we go to Youtube\n")
            wb.open("https://www.youtube.com/results?search_query="+Search_term)
            time.sleep(5)

        elif 'search google' in query:
            update("What should I search?",'yellow')
            speak("What should I search?")
            Search_term = TakeCommand().lower()
            wb.open('https://www.google.com/search?q='+Search_term)
        
        #elif 'search' in query: 
            #query = query.replace("query","")
            #wb.open(query)
        
        elif "who am i" in query:
            update("If you can talk, then definitely you are a human",'yellow')
            speak("If you can talk, then definitely you are a human")
        elif "why you came to this world" in query:
            update("Thanks to MAK. further it is a secret",'yellow')
            speak("Thanks to MAK. further it is a secret")
        elif 'word' in query:
            update("opening MS Word",'yellow')
            speak("opening MS Word")
            word = wordAppLocation
            os.startfile(word)

        elif 'what is love' and 'tell me about love' in query:
            update("It is 7th sense that destroy all other senses \nAnd I think it is just a mere illusion \nIt is waste of time",'yellow')
            speak("It is 7th sense that destroy all other senses , "
            "And I think it is just a mere illusion , "
            "It is waste of time")

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            update("Recycle Bin Recycled",'yellow') 
            speak("Recycle Bin Recycled") 

        elif 'send email' in query:
            try:  
                update("What should I say?",'yellow')
                speak("What should I say?")
                content = TakeCommand()
                update("Who is the Reciever?",'yellow')
                speak("Who is the Reciever?")

                # new win 
                newWin = Tk()
                newWin.withdraw()
                retVal = simpledialog.askstring("Enter Value","Enter recieptant's email",parent=newWin)
                newWin.destroy()

                print(retVal)
                to = (retVal)
                sendEmail(to,content)
                update(content,'yellow')
                speak(content)
                update("Email has been sent.",'yellow')
                speak("Email has been sent.")
            except Exception as e:
                print(e)
                update("Unable to send the email.",'yellow')
                speak("Unable to send the email.")

        elif 'search in chrome' in query:
            update("What should I search ?",'yellow')
            speak("What should I search ?")
            chromepath = r'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = TakeCommand()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'log out' in query:
            os.system("shutdown -l")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        
        
        
        elif 'play songs' in query:
            video = videoFilesPath
            audio = AudioFilesPath
            update("What songs should i play? Audio or Video",'yellow')
            speak("What songs should i play? Audio or Video")
            ans = (TakeCommand().lower())
            while(ans != 'audio' and ans != 'video'):
                update("I could not understand you. Please Try again.",'yellow')
                speak("I could not understand you. Please Try again.")
                ans = (TakeCommand().lower())
        
            if 'audio' in ans:
                    songs_dir = audio
                    songs = os.listdir(songs_dir)
                    print(songs)
            elif 'video' in ans:
                    songs_dir = video
                    songs = os.listdir(songs_dir)
                    print(songs)
                
            update("select a random number",'yellow')
            speak("select a random number")
            rand = TakeCommand()
            if rand == None:
                continue
            rand = rand.lower()
            while('number' not in rand and rand != 'random'):                       #used while loop to keep the jarvis on the speak command untill req. command is given.
                speak("I could not understand you. Please Try again.")          #first used 'rand' before while then again after, so that rand is already defind, and Input is taken and then checked if it is according to reuirement or not. And if it is not which means while loop is true, then commands under 'while loop' will execute untill desired approach.As it will again ask the user for input in the same block. 
                rand = (TakeCommand().lower())

            if 'number' in rand:
                    rand = int(rand.replace("number ",""))
                    os.startfile(os.path.join(songs_dir,songs[rand]))
                    continue                                                    #'continue' is used, so that after executing the commands in 'if' or 'elif' block, it will move to the next part of execution (or code). but in this case as this is the last execution of related function then it will move to the next function (i.e. in this code, it will be TakeCommand() )
            elif 'random' in rand:
                    rand = random.randint(1,219)
                    os.startfile(os.path.join(songs_dir,songs[rand]))
                    continue
                


            
        elif 'remember that' in query:
            update("What should I remember ?",'yellow')
            speak("What should I remember ?")
            memory = TakeCommand()
            update("You asked me to remember that"+memory, 'yellow')
            speak("You asked me to remember that"+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif 'do you remember anything' in query:
            remember =open('memory.txt', 'r')
            data = remember.read()
            update("You asked me to remeber that {}".format(data),'yellow')
            speak("You asked me to remeber that {}".format(data))
        
        
        elif "write a note" in query:
            update("What should i write, sir",'yellow')
            speak("What should i write, sir")
            note = TakeCommand()
            file = open('note.txt', 'w')
            update("Sir, Should i include date and time",'yellow')
            speak("Sir, Should i include date and time")
            dt = TakeCommand()
            if 'yes' in dt or 'sure' in dt:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                update('done', 'yellow')
                speak('done')
            else:
                file.write(note)
                
        elif "show note" in query:
            update("Showing Notes",'yellow')
            speak("Showing Notes")
            file = open("note.txt", "r")
            data = file.read()
            update(data,'yellow') 
            speak(data) 

        elif "weather" in query: 
			
			# Google Open weather website 
			# to get API of Open weather
            api_key = weatherApi
            # base_url = "http://api.openweathermap.org/data/2.5/weather?q="
            update(" City name ",'yellow')
            speak(" City name ")
            print("City name : ")
            city_name = TakeCommand()
            # complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            complete_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city_name,api_key)
            response = requests.get(complete_url)
            x = response.json()
            
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                update(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description), 'yellow')
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
                time.sleep(5)
                
            else:
                update(" City Not Found ", 'yellow') 
                speak(" City Not Found ") 





        elif 'news' in query:
            
            try:
                # https://newsapi.org/ : get api from this link
                jsonObj = urlopen('https://newsapi.org/v2/everything?q=tesla&from=2021-05-16&sortBy=publishedAt&apiKey={}'.format(toiNewsapi))
                data = json.load(jsonObj)
                i = 1  
                speak('here are some top news from the times of india')             
                for item in data['articles']:
                    if i== 5:
                        break
                    update('''=============== TOP HEADLINES ============'''+ '\n' + str(i) + '. ' + item['title'] + '\n' + item['description'] + '\n','yellow')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
                
            except Exception as e:
                print(str(e)) 


                
        
        elif 'take a screenshot' in query:
            screenshot()
            update("Done!") #Download folder    
            speak("Done!") #Download folder    
        elif 'cpu' in query:
            cpu()
        elif 'joke' in query:
            jokes()
        elif 'tell me about yourself' and 'who are you' in query:
            Introduction()
        elif 'tell me about mac' and 'creator' in query:
            Creator()
        
        #show location on map
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            update("User asked to Locate : " + str(location),'yellow')
            speak("User asked to Locate")
            speak(location)
            wb.open("https://www.google.com/maps/place/" + location + "")

        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:
            update("I'm not sure about, may be you should give me some time",'yellow')
            speak("I'm not sure about, may be you should give me some time")
            
        elif "i love you" in query:
            update("It's hard to understand, I am still trying to figure this out.",'yellow')
            speak("It's hard to understand, I am still trying to figure this out.")
        

        #calculation
        elif "calculate" in query:
            
            app_id = wolframAlphaApi
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            update("The answer is " + str(answer), 'yellow')
            speak("The answer is " + str(answer)) 

        #General Questions
        elif "what is" in query or "who is" in query: 
			
			# Use the same API key 
			# that we have generated earlier
            client = wolframalpha.Client(wolframAlphaApi)
            res = client.query(query)
            
            try:
                update(str(next(res.results).text),'yellow')
                speak (next(res.results).text)
            except StopIteration:
                update("No results",'yellow') 
                speak("No results") 




        #sleep-time
        elif "don't listen" in query or "stop listening" in query:
            update("for how much seconds you want me to stop listening commands",'yellow')
            speak("for how much seconds you want me to stop listening commands")
            a = int(TakeCommand())
            time.sleep(a)
            print(a)

        #quit
        elif 'offline' in query:
            update("going Offline",'yellow')
            speak("going Offline")
            quit()




def started():     #method which start on click of microphone icon
    global terminate,flag
    if flag==1:
        l1.config(image=stop)
        
        
        try:
            terminate=0
            t1 = Thread(target=runnow)
            t1.start()
            update("I am Jarvis!! .How May I help You","white")
            flag=0
        except RuntimeError:
            update(RuntimeError,"red")
    else:
        update("Stoped","red")
        l1.config(image=play)
        flag = 1
        terminate = 1
        

def colorchange():          #method which change color of the backgroud of the window randomly

    color1="#123456"
    color2="#75ff33"
    color3="#33ffbd"
    color4="#33ff57"
    color5="#eef9bf"
    
    colors=[color1,color2,color3,color4,color5,"#a7e9af","#6a8caf","#fd5e53","#f9fcfb","#b0eacd","#21bf73","#be8abf","#ea9abb","#fea5ad","#f8c3af"]
    color=random.choice(colors)
    msgcolor=random.choices(colors)
    root.config(background=color)
    l1.config(background=color)
    neticon.config(background=color)
    nettext.config(background=color)
    logolab.config(background=color)
    msg.config(background=msgcolor)
    ccb.config(background=random.choice(colors),fg=msgcolor)

def helpwindow():        #method which open the help window
    helproot =Tk()
    # helproot.geometry("500x400")
    textarea=Text(helproot,height="30",width="80")
    textarea.pack(padx=20,pady=20)
    with open('helpfile.txt','r') as target:
        textarea.insert(INSERT,target.read())

    textarea.config(state=DISABLED)
    helproot.mainloop()



def Exit():                #method to exit
    sys.exit(1)



if __name__ == "__main__":  
    root = Tk()
    root.iconbitmap("images/icon.ico")
    netlogo = Image.open("images/defaulticon.png")
    netlogo = netlogo.resize((30, 30), Image.ANTIALIAS)
    netlogo = ImageTk.PhotoImage(netlogo)

    connlogo = Image.open("images/connected.png")
    connlogo = connlogo.resize((30, 30), Image.ANTIALIAS)
    connlogo = ImageTk.PhotoImage(connlogo)

    notconn = Image.open("images/notconnected.png")
    notconn = notconn.resize((30, 30), Image.ANTIALIAS)
    notconn = ImageTk.PhotoImage(notconn)

    logo = Image.open("images/icon.ico")
    logo = logo.resize((60, 60), Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(logo)

    root.geometry("800x550")
    root.resizable(FALSE, FALSE)
    root.title("Jarvis")

    play = Image.open("images/microphone.png")
    play = play.resize((100, 120), Image.ANTIALIAS)
    play = ImageTk.PhotoImage(play)
    stop = Image.open("images/stop.png")
    stop = stop.resize((100, 100), Image.ANTIALIAS)
    stop = ImageTk.PhotoImage(stop)
    # menu code started......
    menu=Menu(root)
    root.config(menu=menu)
    submenu=Menu(menu,tearoff=False)
    menu.add_cascade(label="Options",menu=submenu)
    submenu.add_command(label="About us")
    submenu.add_separator()
    submenu.add_command(label="Exit",command=Exit)
    helpmenu=Menu(menu,tearoff=False,bg="white")
    menu.add_cascade(label="Help",menu=helpmenu)
    helpmenu.add_command(label="help",command=helpwindow)

    
    # menu code ends.......
    root.config(background="#123456")
    l1 = Button(root, image=play, bg="#123456", command=started, borderwidth=0)
    l1.place(x=350, y=300)
    msg = text = Text(root, state='disabled', width=52, height=6, font="bell 16 italic", bg="#123487", fg="gray")
    # msg = Label(root, text=message, height="2",width="50", font="bell 16 italic", bg="#123487", fg="Blue")
    msg.place(x=80, y=120)
    neticon = Label(root, image=netlogo, bg="#123456")
    neticon.place(x=620, y=10)
    nettext = Label(root, text="Checking...", bg="#123456", fg="Yellow", font="bell 10 bold")
    nettext.place(x=665, y=15)
    logolab=Label(root,image=logo,bg="#123456")
    logolab.place(x=20,y=10)
    Timer(1.0, Isconnect).start()
    ccb=Button(root,text="Change Color",font="comic 12 bold italic",bg="#75ff33",border=0.3,command=colorchange)
    ccb.place(x=350,y=500)
    root.mainloop()


