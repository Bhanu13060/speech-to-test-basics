from transformers import pipeline

def transcribe_with_wav2vec(audio_path): asr = pipeline("automatic-speech-recognition", model="facebook/wav2vec2-base-960h") result = asr(audio_path) print("Transcription (Wav2Vec2):", result['text'])

if name == "main": transcribe_with_wav2vec("example.wav")

requirement.txt

SpeechRecognition pydub transformers torchaudio soundfile
