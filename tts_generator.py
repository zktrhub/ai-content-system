from gtts import gTTS
import os

def text_to_speech(text, language='en', filename='output_audio.mp3'):
    tts = gTTS(text=text, lang=language)
    path = os.path.join("outputs", filename)
    os.makedirs("outputs", exist_ok=True)
    tts.save(path)
    return path