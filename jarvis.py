import pyttsx3 #Text to speech 
import datetime #Dt and Time
import speech_recognition as sr #speech recognition
import wikipedia #wikipedia
import smtplib #sent email
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes
import random
import pywin32_system32
import shutil
import ctypes
import subprocess
import winshell
import json
from urllib.request import urlopen
import openai
from config import apikey
import cv2
from requests import get
import pywhatkit as kit
import requests
import PyPDF2
import operator
from playsound import playsound
from googletrans import Translator
from pywikihow import search_wikihow
import pywhatkit 
import speedtest
from geopy.geocoders import Nominatim
from geopy import distance
from quote import quote
from forex_python.converter import CurrencyRates
import sys





#Test To Speech ----->
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)

#engine.say("Hello, this is Jarvis, What can I do for you")
#engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
#speak("Hello, this is Jarvis, What can I do for you")

def startup():
    speak("Initializing Jarvis")
    speak("Starting all systems applications")
    speak("Installing and checking all drivers")
    speak("Caliberating and examining all the core processors")
    speak("Checking the internet connection")
    speak("Wait a moment sir")
    speak("All drivers are up and running")
    speak("All systems have been activated")
    speak("Now I am online")

#Date And Time ----->
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    print("The current time is ", Time)
#time()

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)
    print("The current date is " + str(day) + "/" + str(month) + "/" + str(year))
#date()

#Greetings ----->
def wishme():
    print("Welcome Back Sir !!!")
    speak("Welcome Back Sir !!!")
    #time()
    #date()
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<=12:
        print("Good Morning Sir!!")
        speak("Good Morning Sir!!")
        
    elif hour>=12 and hour<18:
        print("Good Afternoon Sir!!")
        speak("Good Afternoon Sir!!")
        
    elif hour>=18 and hour<24:
        print("Good Evening Sir!!")
        speak("Good Evening Sir!!")
        
    else:
        speak("Good Night Sir")
        
    print("Jarvis at your service sir, please tell me how may I help you.")
    speak("Jarvis at your service sir, please tell me how may I help you.")
    
#wishme()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1    #wait for 1 sec
        audio = r.listen(source) #source =  microphone
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please")
        return "None"
        
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com, 587')
    server.ehlo()
    server.starttls()
    server.login('abc@gmail.com', '123')
    server.sentmail('abc@gmail.com', to, content)
    server.close()
    
def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\sahil\\OneDrive\\Desktop\\Jarvis\\ss\\ss.png")
    
def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+usage)
    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent)
    
def jokes():
    speak(pyjokes.get_joke())
    
def username():
	speak("What should i call you sir")
	uname = takeCommand()
	speak("Welcome Mister")
	speak(uname)
	columns = shutil.get_terminal_size().columns
	
	print("#####################")
	print("Welcome Mr.", uname)
	print("#####################")
	
	speak("How can i Help you, sir")
 
def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for prompt: {prompt} \n ************************\n\n"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("OpenAI"):
        os.mkdir("OpenAI")
        
    #with open(f"OpenAI/prompt- {random.randint(1, 2343434356)}", 'w') as f:
    with open(f"OpenAI/{prompt[0:60]}.txt", 'w') as f:
        f.write(text)
        
chatStr=""

def chat(query):
    global chatStr
    openai.api_key = apikey
    chatStr += f"You: {query}\n Jarvis:"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    speak(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]
    
        
    #with open(f"OpenAI/prompt- {random.randint(1, 2343434356)}", 'w') as f:
    with open(f"OpenAI/{prompt[0:60]}.txt", 'w') as f:
        f.write(text)
        
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=3e8a98729b98442d978bfd17421187d5' #newsapi
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head=[]
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        print(f"Today's {day[i]} news is: {head[i]}")
        speak(f"Today's {day[i]} news is: {head[i]}")
        
'''def TakeHindi():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1    #wait for 1 sec
        audio = r.listen(source) #source =  microphone
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please")
        return "None"
        
    return query

def Tran():
    speak("Tell me line")
    line = TakeHindi()
    traslate = Translator()
    result = traslate.translate(line)
    Text = result.text
    speak(Text)
        
        

def pdf_reader():
    book = open('Python.pdf', 'rb')
    pdfreader = PyPDF2.PdfFileReader(book)
    pages = pdfreader.numPages
    speak(f"Total numbers of pages in this book {pages}")
    speak("sir please enter the page number i have to read")
    pg = int(input("please enter the page number: "))
    page = pdfreader.getPage(pg)
    text = page.extractText()
    speak(text)      
'''    
    
    
    
 

 
    
    
#takeCommand()
#================================================================

#main
if __name__ == "__main__":
    startup()
    wishme()
    username()
    while True:
        query = takeCommand().lower()
        home_user_dir = os.path.expanduser("~")
        if 'time' in query:
            time()
            
        elif 'date' in query:
            date()
            
        elif "who are you" in query:
            speak("I'm JARVIS created by Mr. Kishan and I'm a desktop voice assistant.")
            print("I'm JARVIS created by Mr. Kishan and I'm a desktop voice assistant.")

        elif "how are you" in query:
            speak("I'm fine sir, What about you?")
            print("I'm fine sir, What about you?")

        elif "fine" in query:
            speak("Glad to hear that sir!!")
            print("Glad to hear that sir!!")

        elif "good" in query:
            speak("Glad to hear that sir!!")
            print("Glad to hear that sir!!")
            
        elif 'wikipedia' in query:
            try:
                speak("Ok wait sir, I'm searching...")
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except:
                speak("Can't find this page sir, please ask something else")
                
        elif "open youtube" in query:
            wb.open("youtube.com") 

        elif "open google" in query:
            print("Opening Google...?")
            print("What should i search on Google?")
            speak("What should i search on Google?")
            cm = takeCommand().lower()
            wb.open(f"{cm}") 
   
        elif "open stack overflow" in query:
            wb.open("stackoverflow.com")
            
        elif 'what`s the time' in query:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")
            speak(f"Sir, the time is {strTime}")
            
        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query
            
        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")
            
        elif "what's your name" in query or "what is your name" in query:
            print("I am Jarvis")
            speak("I am Jarvis")
            
        elif 'alexa' in query:
            speak("I don't know Alexa, but I've heard of Alexa. If you have Alexa, "
                        "I may have just triggered Alexa. If so, sorry Alexa.")

        elif 'google assistant' in query:
            speak("He was my classmate, too intelligent guy. We both are best friends.")

        elif 'siri' in query:
            speak("Siri, She's a competing virtual assistant on   a competitor's phone. "
                        "Not that I'm competitive or anything.")

        elif 'cortana' in query:
            speak("I thought you'd never ask. So I've never thought about it.")

        elif 'python assistant' in query:
            speak("Are you joking. You're coming in loud and clear.")

        elif 'what language you use' in query:
            speak("I am written in Python and I generally speak english.")
   
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'xyz@gmail.com'
                sendEmail(to, content)
                speak("content")
            except Exception as e:
                print(e)
                speak("Unable to sent email")
                
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Mr. Sahil Lokhande")
        
        elif "who i am" in query:
            speak("If you talk then definately your human.")
    
        elif "jarvis why you came to this world" in query:
            speak("Thanks to Mr. Sahil Lokhande who created me.   further It's a secret and none of your business")
            
        elif 'what is love' in query:
            speak("It is 7th sense that destroy all other senses")
        
        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")
            
        elif "i love you" in query:
            speak("It's hard to understand")
            
        elif "Jarvis tell us about yourself" in query:
            speak("OK i am jarvis created by Mr. Sahil Lokahnde. i am virtual assistant.who can help you in your day today life.i can do virtually whatever you want.such as webbrowsing, opning applications,writing short notes.i can be your 24 by 7 assistant to help you sir.")
            
        elif 'open bluestack' in query:
            appli=r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
            os.startfile(appli)
            
        elif 'open notepad' in query:
            npad=r"C:\\Windows\\notepad.exe"
            os.startfile(npad)
            
        elif 'open visual studio code' in query:
            os.startfile(home_user_dir + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\"
                         "Programs\\Visual Studio Code\\Visual Studio Code")

        elif 'open eclipse' in query:
            os.startfile(home_user_dir + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\"
                         "Programs\\Eclipse\\Eclipse IDE for Java Developers - 2020-06")

        elif 'open notepad' in query:
            os.startfile("C:\\Windows\\notepad.exe")

        elif 'open pycharm' in query:
            os.startfile("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.1\\bin\\pycharm64.exe")

        elif 'open code blocks' in query:
            os.startfile(home_user_dir + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\"
                         "Programs\\CodeBlocks\\CodeBlocks")

        elif 'open mozilla firefox' in query:
            os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")

        elif 'open chrome' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif 'open whatsapp' in query:
            os.startfile(home_user_dir + "\\AppData\\Local\\WhatsApp\\WhatsApp.exe")

        elif 'open v l c' in query:
            os.startfile("C:\\Program Files\\VideoLAN\\VLC\\vlc.exe")
            
        #close the running application
        elif 'close notepad' in query.lower():
            speak("OK i am closing notepad")
            os.system("taskkill /f /im notepad.exe")
            
        elif 'close visual studio code' in query:
            os.system("TASKKILL /F /IM Code.exe")

        elif 'close eclipse' in query:
            os.system("TASKKILL /F /IM eclipse.exe")

        elif 'close notepad' in query:
            os.system("TASKKILL /F /IM notepad.exe")

        elif 'close pycharm' in query:
            os.system("TASKKILL /F /IM pycharm64.exe")

        elif 'close code blocks' in query:
            os.system("TASKKILL /F /IM codeblocks.exe")

        elif 'close chrome' in query:
            os.system("TASKKILL /F /IM chrome.exe")

        elif 'close whatsapp' in query:
            os.system("TASKKILL /F /IM WhatsApp.exe")

        elif 'close vlc' in query:
            os.system("TASKKILL /F /IM vlc.exe")

        elif 'close spotify' in query:
            os.system("TASKKILL /F /IM Spotify.exe")
            
        elif 'open cmd' in query or 'open command prompt'.lower() in query:
            os.system("start cmd")
            
        elif 'open camera' in query.lower(): #closed bt esc key
              cap = cv2.VideoCapture(0)
              while True:
                  ret, img = cap.read()
                  cv2.imshow('webcam', img)
                  k = cv2.waitKey(50)
                  if k==27:
                      break;
              cap.release()
              cv2.destroyAllWindows()  
              
        elif 'ip address' in query.lower():
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")
            
        elif 'where i am' in query.lower() or 'where we are' in query.lower():
            speak("wait, let me check")
            print("searching our location...")
            try:
                ipAdd = requests.gets('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                
                city = geo_data['city']
                country = geo_data['country']
                
                speak(f"Sir I am not sure, but i think we are in {city} city of {country} country")
            except Exception as e:
                speak("Sorry I am able to find location, please check your network comnection")
                pass
            
        elif 'send message' in query.lower():
            kit.sendwhatmsg("+918087977227", "this automatic generated message by Jarvis",2,24) #2,24 is time
                  
        elif 'switch window' in query.lower() or 'change window' in query.lower():
            speak("Okay sir, Switching the window")
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
            
        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation() 
            
        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call(["shutdown", "/s"]) 
            
        elif 'free recycle bin' in query or 'clear recycle bin' in query:
            try:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                print("Recycle Bin is cleaned successfully.")
                speak("Recycle Bin is cleaned successfully.")

            except Exception as e:
                print("Recycle bin is already Empty.")
                speak("Recycle bin is already Empty.") 
                
        elif 'quote' in query or 'quotes' in query:
            speak("Tell me the author or person name.")
            q_author = takeCommand()
            quotes = quote(q_author)
            quote_no = random.randint(1, len(quotes))
            # print(len(quotes))
            # print(quotes)
            print("Author: ", quotes[quote_no]['author'])
            print("-->", quotes[quote_no]['quote'])
            speak(f"Author: {quotes[quote_no]['author']}")
            speak(f"He said {quotes[quote_no]['quote']}")
            
        elif 'day' in query or 'day today' in query:
            def tell_day():
                day = datetime.datetime.now().strftime("%A")
                speak(day)
            tell_day()
            
        elif 'month' in query or 'month is going' in query:
            def tell_month():
                month = datetime.datetime.now().strftime("%B")
                speak(month)
            tell_month()
            
        elif 'volume up' in query:
            print("Increrasing Volume Up")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
    
        elif 'volume down' in query:
            print("decreasing  Volume Down")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
                  
        elif 'volume mute' in query:
            print("Muted")
            pyautogui.press("volumemute")
                   
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
        
        elif "write a note" in query or 'make a note' in query:
            speak("What should I write, sir??")
            note = takeCommand()
            file = open('note.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                speak("Point noted successfully.")
            else:
                file.write(note)
                speak("Point noted successfully.")
                
        elif "show note" in query or 'read notes' in query:
            speak("Showing Notes")
            file = open("note.txt", "r")
            print(file.read())
            speak(file.read(6))
            
            #speak("Reading Notes")
            #file = open("note.txt", "r")
            #data_note = file.readlines()
            ## for points in data_note:
            #print(data_note)
            #speak(data_note)
                
        elif "open chrome" in query:
            print("Opening chrome....")
            chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)
                
        elif 'search in chrome' in query:
            try:
                speak("what should I search?")
                print("What should I search?")
                chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
                search = takeCommand().lower()
                wb.get(chromepath).open_new_tab(search+'.com')
            except Exception as e:
                speak("Can't open now, please try again later.")
                print("Can't open now, please try again later.")
                
        elif 'clear browsing history' in query:
            pyautogui.hotkey('ctrl', 'shift', 'delete')
            
        elif 'close tab' in query:
            pyautogui.hotkey('ctrl', 'w')
            
        elif 'minimise this window' in query:
            pyautogui.hotkey('alt', 'space')
            time.sleep(1)
            pyautogui.press('n')
            
        elif 'open history' in query:
            pyautogui.hotkey('ctrl', 'h')
            
        elif 'open downloads' in query:
            pyautogui.hotkey('ctrl', 'j')

        elif 'open incognito window' in query:
            pyautogui.hotkey('ctrl', 'shift', 'n')
            
        elif "refresh" in query:
            pyautogui.moveTo(1551,551, 2)
            pyautogui.click(x=1551, y=551, clicks=1, interval=0, button='right')
            pyautogui.moveTo(1620,667, 1)
            pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left')
               
        elif 'logout' in query:
            os.system("shutdown -1")
            #print("Do you want to logout from your system?")
            #speak("Do you want to logout from your system?")
            #cmd = takeCommand()
            #if 'no' in cmd:
            #    continue
            #else:
            #    os.system("shutdown -l")
        
        elif 'shutdowm' in query:
            os.system("shutdown /s /t 1")
            #print("Do you want to shutdown you system?")
            #speak("Do you want to shutdown you system?")
            #cmd = takeCommand()
            #if 'no' in cmd:
            #    continue
            #else:
                
            #    os.system("shutdown /s /t 1")
            
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
            #print("Do you want to restart your system?")
            #speak("Do you want to restart your system?")
            #cmd = takeCommand()
            #if 'no' in cmd:
            #    continue
            #else:
              
            #    os.system("shutdown /r /t 1")
         
        elif 'play songs' in query:
            songs_dir = 'D:\\Songs'
            songs = os.listdir(songs_dir)
            print(songs)
            os.startfile(os.path.join(songs_dir, songs[0]))
            
        elif 'search google' in query:
            speak('What should I search?')
            search_term = takeCommand().lower()
            speak('Searching...')
            wb.open('https://www.google.com/search?q='+search_term)
        
        elif 'remember that' in query:
            speak("what should I remenber?")
            data = takeCommand()
            speak("you said me to remember that" + data)
            print("You said me to remember that " + str(data))
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
        
        elif 'where is' in query:
            query = query.replace('where is', '')
            location = query
            speak('User asked to locate'+location)
            wb.open_new_tab('https://www.google.com/maps/place/'+location)
        
        elif 'news' in query:
            try:
                jsonobj = urlopen("http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=3e8a98729b98442d978bfd17421187d5")        
                data = json.load(jsonobj)
                i = 1
                speak("Here are top 10 headlines")
                print("===========TOP HEADLINES==========="+"\n")
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i +=1
                
            except Exception as e:
                print(str(e))
                
            '''main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=3e8a98729b98442d978bfd17421187d5' #newsapi
            main_page = requests.get(main_url).json()
            articles = main_page["articles"]
            head=[]
            day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","ninth","tenth"]
            for ar in articles:
                head.append(ar["title"])
            for i in range (len(day)):
                print(f"Today's {day[i]} news is: {head[i]}")
                speak(f"Today's {day[i]} news is: {head[i]}")'''
                   
        elif 'stop listening' in query:
            speak('For how much time you want me to stop listening to your commands?')
            ans = int(takeCommand())
            time.sleep(ans)
            print(ans)
        
        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("You told me to remember that" + remember.read())
            print("You told me to remember that " + str(remember))
            
        elif 'take screenshot' in query:
            screenshot()
            speak("Done! I've taken screenshot, please check it")
            
        elif 'internet speed' in query or 'net speed' in query:
            print("Calculating downloading and uploading speed...")
            st = speedtest.Speedtest()
            print("Wait!! I am checking your Internet Speed...")
            speak("Wait!! I am checking your Internet Speed...")
            dw_speed = st.download()
            up_speed = st.upload()
            dw_speed = dw_speed / 1000000
            up_speed = up_speed / 1000000
            print('Your downloading speed is', round(dw_speed, 3), 'Mbps')
            print('Your uploading speed is', round(up_speed, 3), 'Mbps')
            speak(f'Your downloading speed is {round(dw_speed, 3)} Mbps')
            speak(f'Your uploading speed is {round(up_speed, 3)} Mbps')
            
            #st = speedtest.Speedtest()
            #dl =  st.download()
            #up = st.upload()
            #print(f"Sir we have {dl} bit per second downloading speed and {up} bit per seconds uploading speed")
            #speak(f"Sir we have {dl} bit per second downloading speed and {up} bit per seconds uploading speed")
                       
        elif 'cpu' in query:
            cpu()
            
        elif 'joke' in query:
            print(jokes)
            jokes()
            
        elif ("tell me your powers" in query or "help" in query or "features" in query):
            features = ''' i can help to do lot many things like..
            i can tell you the current time and date,
            i can tell you the current weather,
            i can tell you battery and cpu usage,
            i can create the reminder list,
            i can take screenshots,
            i can send email to your boss or family or your friend,
            i can shut down or logout or hibernate your system,
            i can tell you non funny jokes,
            i can open any website,
            i can search the thing on wikipedia,
            i can change my voice from male to female and vice-versa
            And yes one more thing, My boss is working on this system to add more features...,
            tell me what can i do for you??
            '''
            print(features)
            speak(features)
            
        elif 'using ai'.lower() in query.lower():
            ai(prompt = query)
        
        elif "go to sleep" in query:
            speak(' alright then, I am switching off')
            sys.exit()

        elif 'close movie' in query:
            os.system("taskkill /f /im vlc.exe")
            
        elif 'offline' in query:
            print("Bye !!! See you later")
            speak("Bye, See you later")
            quit()
        
        elif 'reset chat'.lower() in query.lower():
            chatStr = ""
        
        elif 'how to' in query:
            try:
                # query = query.replace('how to', '')
                max_results = 1
                data = search_wikihow(query, max_results)
                # assert len(data) == 1
                data[0].print()
                speak(data[0].summary)
            except Exception as e:
                speak('Sorry, I am unable to find the answer for your query.')
            
        elif 'do some calculation' in query.lower() or 'can you calculate' in query.lower():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("Say what you want to calculate...")
                print("Listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source) #source =  microphone
            my_string= r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return{
                    '+' : operator.add,
                    '-' : operator.sub,
                    'x' : operator.mul,
                    'divide' : operator.__truediv__,
                }[op]            
            def eval_binary_expr(op1, oper, op2):
                op1, op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            speak("your result is: ")
            speak(eval_binary_expr(*(my_string.split())))
            print("your result is: ",eval_binary_expr(*(my_string.split())))
            
        elif 'alarm' in query:
            speak(" Time please")
            time = input(": Enter the time :")
            
            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")
                
                if now == time:
                    speak("Time to Wake Up !!!")
                    playsound('air_horn.mp3')
                    speak("Alarm Closed!!!")
                    
                elif now>time:
                    break 
                
        elif 'send message on whatsapp' in query:
            phno_list = {
                'Umesh': '+911234567890',
                'Rishabh': '+919876543210',
                'Sahil': '+918087977227'
            }


            def send_whtmsg():
                speak('To whom you want to send message on WhatsApp')
                recepient = takeCommand()
                check_recep = phno_list[recepient]
                print(check_recep)
                speak('Tell me the text in your message')
                msg = takeCommand()
                speak('Do you want to send it immediately?')
                act_msg = takeCommand()
                if 'yes' in act_msg:
                    hr = datetime.datetime.now().time().hour
                    min = datetime.datetime.now().time().minute
                    pywhatkit.sendwhatmsg(check_recep, msg, hr, min + 2)
                    print('Hey lazy person. Your message is sent successfully.')
                else:
                    speak('At what time you want to send this message. For example, 11:21 PM')
                    msg_time = takeCommand()

                    hr = 12
                    min = 52
                    pywhatkit.sendwhatmsg(check_recep, msg, hr, min)
                    print('Hey lazy person. Your message is sent successfully.')
                speak('Do you want to send more WhatsApp messages?')
                more_msg = takeCommand()
                if 'yes' in more_msg:
                    send_whtmsg()


            send_whtmsg()
            
        elif 'distance' in query:
            geocoder = Nominatim(user_agent="Singh")
            speak("Tell me the first city name??")
            location1 = takeCommand()
            speak("Tell me the second city name??")
            location2 = takeCommand()

            coordinates1 = geocoder.geocode(location1)
            coordinates2 = geocoder.geocode(location2)

            lat1, long1 = coordinates1.latitude, coordinates1.longitude
            lat2, long2 = coordinates2.latitude, coordinates2.longitude

            place1 = (lat1, long1)
            place2 = (lat2, long2)

            distance_places = distance.distance(place1, place2)

            print(f"The distance between {location1} and {location2} is {distance_places}.")
            speak(f"The distance between {location1} and {location2} is {distance_places}")
        
        elif 'convert currency' in query:
            try:
                curr_list = {
                    'dollar': 'USD', 'taka': 'BDT', 'dinar': 'BHD',
                    'rupee': 'INR', 'afghani': 'AFN', 'real': 'BRL',
                    'yen': 'JPY', 'peso': 'ARS', 'pound': 'EGP', 'rial': 'OMR',
                    'lek': 'ALL', 'kwanza': 'AOA', 'manat': 'AZN', 'franc': 'CHF'
                }

                cur = CurrencyRates()
                # print(cur.get_rate('USD', 'INR'))
                speak('From which currency u want to convert?')
                from_cur = takeCommand()
                src_cur = curr_list[from_cur.lower()]
                speak('To which currency u want to convert?')
                to_cur = takeCommand()
                dest_cur = curr_list[to_cur.lower()]
                speak('Tell me the value of currency u want to convert.')
                val_cur = float(takeCommand())
                # print(val_cur)
                print(cur.convert(src_cur, dest_cur, val_cur))
                speak(cur.convert(src_cur, dest_cur, val_cur))
                        
            except Exception as e:
                print("Couldn't get what you have said, Can you say it again??")
                
        
        #elif 'translator' in query:
           # Tran()
                             
        else:
            chat(query)
            
    '''elif 'read pdf' in query.lower():
            pdf_reader()'''