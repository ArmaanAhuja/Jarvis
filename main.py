import speech_recognition as sr
import pyttsx3 as audio
import qrcode
from PIL import Image
import datetime
# from selenium import webdriver
import webbrowser
import win32com.client
import openai
import subprocess
import os 


speaker = win32com.client.Dispatch("SAPI.SpVoice")
engine = audio.init()


# driver = webdriver.Chrome()
print("everything worked fine")

#function that prints the argument given

    



    



def say(text): 
    # engine.say(text)
    # engine.runAndWait()
    speaker.Speak(text)




def say2(text): 
    # speaker.Speak(text)
    engine.say(text)
    engine.runAndWait()

def takeCommand(): 
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        r.pause_threshhold = 1
        print("listening....")
        audio = r.listen(source)
        try: 
            query = r.recognize_google(audio, language = "en-in")
            print(f"User said: {query}")
            return query
        except Exception as e: 
            print("Some error occured. sorry from jarvis")
            return "Some error occured. sorry from jarvis"


# def chat(query):
#     openai.api_key = apikey
#     chat
    

if __name__ == '__main__': 
    say("JARVIS AI HERE")
    # say2("JARVIS AI HERE")
    sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.org"], ['google', 'https://www.google.com'], ["xvideos", 'https://www.xvideos53.com'], ['discord', 'https://www.discord.com'], ['instagram', 'https://www.instagram.com']]

    colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]


    while True: 
        text = takeCommand()
        if "jarvis shut down" in text.lower():
            print("shutting down")
            say("shutting down")
            break
        # elif "open" in text.lower():
        for site in sites: 
            if f"open {site[0]}".lower() in text.lower(): 
                print(f"opening {site[0]}")
                say(f"opening {site[0]}")
                webbrowser.open(site[1])


        if "open music" in text.lower():
            print("opening music")
            say("opening music")
            musicPath = 'C:/Users/ASUS/OneDrive/Documents/Coding/100DAYSOFPYTHON/venv/jarvis/music.mp3'
            # os.startfile(musicPath)
            # import subprocess, sys
            # opener = "open" if sys.platform == "darwin" else "xdg-open"
            # subprocess.call([opener, musicPath]
            # )
            os.system(musicPath)

        elif "open image" in text.lower(): 
            print("opening image")
            say("opening image")
            imgPath = 'C:\\Users\\ASUS\\OneDrive\\Desktop\\cheify.png'
            os.system(imgPath)
        
        elif "open discord in app" in text.lower(): 
            print("opening discord")
            say("opening discord")
            discordPath = "C:/Users\ASUS/AppData/Local/Discord/Update.exe --processStart Discord.exe"
            os.system(discordPath)

        elif "open processing" in text.lower(): 
            print("opening processing")
            say("opeing processing")
            processingPath = "C:\Program Files\processing-4.2\processing.exe"
            subprocess.call([processingPath])

        elif "the time" in text.lower(): 
            strfTime = datetime.datetime.now().strftime('%H:%M')
            print(f"The time is {strfTime}")
            say(f"The time is {strfTime}")

        elif "open downloads" in text.lower(): 
            downloadsPath = "D:\Games"
            print("opening downloads")
            say("opening downloads")
            # os.system(downloadsPath)
            # os.open(downloadsPath, os.O_RDWR, 0o666)
            os.startfile(downloadsPath)


        elif "qr code for" in text.lower(): 
            # print("true")
            if "normal" in text.lower(): 
                # print("true again")
                for site in sites: 
                    if site[0] in text.lower():
                        print(f"Generating a normal qr code for site {site[0]}") 
                        say(f"Generating a normal qr code for site {site[0]}")
                        img = qrcode.make(site[1])
                        img.save(f"jarvis/assets/qr/{site[0]}.png")
                    
            for color in colors: 
                if (f"background colour {color}") in text.lower(): 
                    print("true 2")
                    for color2 in colors: 
                        if(f"foreground colour {color2}") or (f"4 ground colour {color2}") in text.lower():
                            for site in sites: 
                                if site[0] in text.lower(): 
                                    qr = qrcode.QRCode(
                                            version = 1,  
                                            error_correction = qrcode.constants.ERROR_CORRECT_H, 
                                            box_size = 10, border = 4)
                                    
                                    qr.add_data(site[1])
                                    qr.make(fit = True)
                                    img = qr.make_image(fill_color = color2, back_color = color)
                                    img.save(f"jarvis/assets/qrColored/{site[0]}.png")
                                     

                                    


                     




            
            
        # else: 
        #     say(text)
          