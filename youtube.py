from googleapiclient.discovery import build
import speech_recognition as sr
import pyttsx3
import pywhatkit as kit
import keyboard
import webbrowser
import time

listener = sr.Recognizer()

api_key = 'AIzaSyAOXBZeUaR6gd5Mwo5fe-b42X7vuAiXft4'
youtube = build('youtube', 'v3', developerKey=api_key)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',170)


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

def YoutubeAuto():
        talk("Whats Your Command ?")
        comm = takecommand()

        if 'pause' in comm:
            keyboard.press('space bar')

        elif 'restart' in comm:
            keyboard.press('0')

        elif 'mute' in comm:
            keyboard.press('m')

        elif 'skip' in comm:
            keyboard.press('l')

        elif 'back' in comm:
            keyboard.press('j')

        elif 'full screen' in comm:
            keyboard.press('f')

        elif 'film mode' in comm:
            keyboard.press('t')

        talk("Done Sir")


def talk(audio):
    engine.say(audio)
    engine.runAndWait()

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




def run():
    video = ""
    while True:
        command = takecommand()

        if command:
            if 'search' in command:
                query = command.replace('search', '').strip()
                results = search_videos(query)
                if results:
                    show_search_results_in_browser(query)
                    talk('The results are displayed. Please choose a video by saying play and the video title.')

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
                        
            elif 'pause' in command:
             keyboard.press('space bar')

            elif 'restart' in command:
             keyboard.press('0')

            elif 'mute' in command:
             keyboard.press('m')

            elif 'skip' in command:
             keyboard.press('l')

            elif 'back' in command:
              keyboard.press('j')

            elif 'full screen' in command:
             keyboard.press('f')

            elif 'film mode' in command:
             keyboard.press('t')
  
            elif 'stop' in command:
             exit()
            

run()
