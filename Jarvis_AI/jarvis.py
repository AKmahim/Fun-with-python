import pyttsx3
import datetime
import speech_recognition as sr


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
#fucntion for speak the content
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#fucntion for wish me with date & time 
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >=0 and  hour<12:
        speak('Good Morning Mitu!')
    elif hour>=12 and hour<18:
        speak('Good Afternoon Mitu!')
    else:
        speak('Good Evening Mitu!')
    speak('I am jarvis. Your virtual assistant. How may I help you medam? ')

#here is a fucntion for take our command using mic voice
def takeCommand():
    #it take microphone input and returns output as string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 200
        audio = r.listen(source)
    
    
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language="en-IN")
        #print(query)
        print(f"User said:{query}\n")
        #st ="User said:{}"
        #print(st.format(query))
    
    except Exception as e:
        #print(e)
        print('Say that again please....')
        return "none"
    return query



#this is the main fucntion
if __name__ == '__main__':
    wishMe()
    takeCommand()


