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

wav2vec_app.py

from transformers import pipeline

def transcribe_with_wav2vec(audio_path):
    asr = pipeline("automatic-speech-recognition", model="facebook/wav2vec2-base-960h")
    result = asr(audio_path)
    print("Transcription (Wav2Vec2):", result['text'])

if __name__ == "__main__":
    transcribe_with_wav2vec("example.wav")
