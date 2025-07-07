speech_recognition_app.py

import speech_recognition as sr

def transcribe_with_google(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            print("Transcription (Google):", text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    transcribe_with_google("example.wav")
