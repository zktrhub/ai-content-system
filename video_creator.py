# video_creator.py

from moviepy.editor import *
from gtts import gTTS
import os

def text_to_video(text, output_file='output_video.mp4', lang='en'):
    audio_file = 'temp_audio.mp3'
    tts = gTTS(text, lang=lang)
    tts.save(audio_file)

    clip = ColorClip(size=(1280, 720), color=(0, 0, 0), duration=10)
    txt_clip = TextClip(text, fontsize=48, color='white', size=clip.size, method='caption').set_position('center').set_duration(10)
    audio = AudioFileClip(audio_file)

    final_clip = CompositeVideoClip([clip, txt_clip]).set_audio(audio)
    final_clip.write_videofile(output_file, fps=24)

    os.remove(audio_file)
