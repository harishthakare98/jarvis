import speech_recognition as sr
import datetime
import pyttsx3
import webbrowser
import pywhatkit as kit
from googleapiclient.discovery import build
import keyboard
import time

listener = sr.Recognizer()
api_key = 'AIzaSyAOXBZeUaR6gd5Mwo5fe-b42X7vuAiXft4'
youtube = build('youtube', 'v3', developerKey=api_key)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',170)


def scroll_down():
    try:
        keyboard.press_and_release('pagedown')
        time.sleep(1)  # Adjust sleep duration if needed
    except Exception as e:
        print(f"Error scrolling down: {e}")

def play_video_by_voice():
    try:
        with sr.Microphone() as source:
            print('Please say the title of the video you want to play...')
            voice = listener.listen(source, timeout=10)
            video_title = listener.recognize_google(voice)
            print(f"You said: {video_title}")

            # Search for videos
            response = search_videos(video_title)

            if response:
                for item in response['items']:
                    if video_title.lower() in item['snippet']['title'].lower():
                        video_id = item['id']['videoId']
                        play_url = f"https://www.youtube.com/watch?v={video_id}"
                        webbrowser.open(play_url)
                        return
                print(f"No video found with title: {video_title}")
            else:
                print("Error searching videos.")
    except sr.WaitTimeoutError:
        print("Listening timed out.")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service; check your network connection.")
    except Exception as e:
        print(f"Error playing video: {e}")


def scroll_down():
    try:
        keyboard.press_and_release('pagedown')
        time.sleep(1)  # Adjust sleep duration if needed
    except Exception as e:
        print(f"Error scrolling down: {e}")

def search_videos(query):
    try:
        request = youtube.search().list(
            part='snippet',
            q=query
        )
        response = request.execute()
        for item in response['items']:
            print(item['snippet']['title'])
        return response
    except Exception as e:
        print(f"Error searching videos: {e}")
        return None

def show_search_results_in_browser(query):
    search_url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(search_url)

def scroll_down():
    try:
        keyboard.press_and_release('pagedown')
        time.sleep(1)  # Adjust sleep duration if needed
    except Exception as e:
        print(f"Error scrolling down: {e}")
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening!")  
    speak("I am your Assistant. Please tell me how can I help you")

def takecommand(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("          ")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Your Command :  {query}\n")

    except:   
        return "None"
        
    return query.lower()

if __name__ == "__main__":
    wish_me()
    while True:
        command = takecommand().lower()    

        if 'hello' in command:
            speak("Hello how can i help you")

        elif 'the time' in command:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'scroll' in command:
                scroll_down()

        elif ' play' in command.lower():
                video = command.lower().replace('play', '').strip()
                if 'results' in locals():
                    for item in results['items']:
                        if video in item['snippet']['title'].lower():
                            video_id = item['id']['videoId']
                            try:
                                play_url = f"https://www.youtube.com/watch?v={video_id}"
                                webbrowser.open(play_url)
                            except Exception as e:
                                print(f"Error playing video: {e}")
                            break


        elif 'open google' in command:
            webbrowser.open("google.com")

        elif 'open youtube' in command:
            webbrowser.open("youtube.com")

        
        elif 'stop' in command:
            exit()

