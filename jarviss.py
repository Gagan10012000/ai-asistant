import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print('good morning')
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening!")  
    print('hi how may i help u')      
    speak("hi how may I help you") 
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

n=1

if __name__ == "__main__":
    wishMe()
    while True:
            query = takeCommand().lower()
            if 'wikipedia' in query:
                print('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
            
            elif 'open google' in query:
                webbrowser.open("google.com")  
            
            elif 'music' in query:
                music_dir = 'C:\\Users\\shamh\\Desktop\\music'
                songs = os.listdir(music_dir) 
                os.startfile(os.path.join(music_dir, songs[4]))
            
            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"the time is {strTime}")
                
            elif 'stop' in query:
                break

            elif 'how are you' in query:
                print("I am fine .What about you")
                speak('I am fine .What about you')

            elif "dance":
                print("i am dancing but you cannot see")
                speak("i am dancing but you cannot see")
