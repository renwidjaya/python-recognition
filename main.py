import ai21
import pywhatkit
import playsound 
import pyttsx3 as pyt
import speech_recognition as sr
from gtts import gTTS
from time import sleep
ai21.api_key = 'UdnbG6SvstJFVOBYRe5SSiDJPLWQITVY'

engine = pyt.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def asistance():
    hallo = 'voices/hallo.mp3'
    playsound.playsound(hallo)
    sleep(5)

asistance()

def talking():
    hears = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        voice = hears.listen(source, phrase_time_limit=5)
        try:
            print("proccesing...")
            proccess = hears.recognize_google(voice, language='id-ID')
            print(proccess)

        except Exception:
            voice = gTTS(text='maaf tuan rendy kami tidak mendengar suara kamu?', lang='id', slow=False)
            voice.save('voice.mp3')
            playsound.playsound('voice.mp3')

        return proccess

def run_sherly():
    Talking = talking()

    if 'keluar' in Talking:
        signout = 'voices/out.mp3'
        playsound.playsound(signout)
        print('terimakasih, Sampai jumpa lagi')   
        sleep(4)
        exit()
    
    elif 'Open' in Talking:
        pywhatkit.playonyt(Talking)
        voice = gTTS(text='Baik tuan rendy kami akan segera tampilkan?', lang='id', slow=False)
        voice.save('voice.mp3')
        playsound.playsound('voice.mp3')

    else:
        response = ai21.Completion.execute(
            model='j2-ultra',
            prompt=Talking,
            maxTokens=200,
        )

        result = response.completions[0].data.text
        voice = gTTS(text=result, lang='id', slow=False)
        voice.save('voice.mp3')
        playsound.playsound('voice.mp3')
        print(result)

        voice = gTTS(text='apakah ada lagi tuan rendy yang bisa saya bantu', lang='id', slow=False)
        voice.save('voice.mp3')
        playsound.playsound('voice.mp3')

while True:
    run_sherly()