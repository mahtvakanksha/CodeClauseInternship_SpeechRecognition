import speech_recognition as sr
import pyttsx3

# Initialize recognizer
r = sr.Recognizer()

def record_audio():
    try:
        with sr.Microphone() as src:
            print("Adjusting for ambient noise, please wait...")
            r.adjust_for_ambient_noise(src, duration=0.3)
            print("Listening...")
            aud = r.listen(src)
            txt = r.recognize_google(aud)
            return txt
    except sr.RequestError as e:
        print(f"Couldn't process your request; {e}")
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand the audio")
    except Exception as e:
        print(f"An unknown error occurred: {e}")
    return None

def show_text(text):
    if text:
        with open("output.txt", "a") as f:
            f.write(text + "\n")
        print(f"Text written to file: {text}")
    return

# Record a single instance of audio
text = record_audio()

# Process the captured audio
if text:
    show_text(text)
    print("Text written in file successfully")
else:
    print("No text to write")
