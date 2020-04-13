import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia as wiki # we have to install this using pip


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
#fucntion for speak the content
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#fucntion for wish me with date & time 
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >=0 and  hour<12:
        speak('Good Morning Mahim !')
    elif hour>=12 and hour<18:
        speak('Good Afternoon Mahim !')
    else:
        speak('Good Evening Mahim !')
    speak('I am jarvis. Your virtual assistant. How may I help you sir? ')

#here is a fucntion for take our command using mic voice
def takeCommand():
    #it take microphone input and returns output as string
    sr.Microphone(device_index=11)
    r = sr.Recognizer()
    r.energy_threshold=5000

    with sr.Microphone() as source:
        print("Listening.....")
        audio = r.listen(source)
    
    
    try:
        print("Recognizing....")
        query = r.recognize_google(audio)
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
    #while True:
    text = takeCommand().lower()
    #Logic for the task base on input text
    if 'wikipedia' in text:
        speak('Searching Wikipedia....')
        text = text.replace("wikipedia","")
        out_data = wiki.summary(text,sentences=2)
        speak("According to Wikipedia")
        print(out_data)
        speak(out_data)


