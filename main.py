from content_generator import generate_content
from translator import translate_text
from tts_generator import text_to_speech
from video_creator import create_video

def run_pipeline(topic, target_language='en'):
    print("İçerik üretiliyor...")
    content = generate_content(topic)

    print("İçerik çevriliyor...")
    translated = translate_text(content, target_language)

    print("Ses dosyası oluşturuluyor...")
    audio_path = text_to_speech(translated, language=target_language)

    print("Video oluşturuluyor...")
    create_video(translated, audio_path)

    print("Tüm süreç başarıyla tamamlandı!")

if __name__ == "__main__":
    run_pipeline("Yapay zekanın geleceği", target_language='en')