from moviepy.editor import TextClip, AudioFileClip, CompositeVideoClip
import os

def create_video(text, audio_path, output_filename="final_video.mp4"):
    os.makedirs("outputs", exist_ok=True)
    clip = TextClip(text, fontsize=50, color='white', bg_color='black', size=(720, 1280), method='caption').set_duration(AudioFileClip(audio_path).duration)
    audio = AudioFileClip(audio_path)
    video = clip.set_audio(audio)
    video_path = os.path.join("outputs", output_filename)
    video.write_videofile(video_path, fps=24)
    return video_path