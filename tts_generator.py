# tts_generator.py

from gtts import gTTS
import os
import uuid

def text_to_speech(text, language='en', output_dir='outputs'):
    """Metni sese çevirir ve MP3 dosyası olarak kaydeder."""
    try:
        # Ses dosyası için eşsiz bir isim oluştur
        filename = f"{uuid.uuid4().hex}.mp3"
        output_path = os.path.join(output_dir, filename)

        # Klasör yoksa oluştur
        os.makedirs(output_dir, exist_ok=True)

        # TTS işlemi
        tts = gTTS(text=text, lang=language)
        tts.save(output_path)

        print(f"Ses dosyası oluşturuldu: {output_path}")
        return output_path
    except Exception as e:
        print(f"Hata oluştu: {e}")
        return None
