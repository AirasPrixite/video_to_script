from moviepy.editor import VideoFileClip

def convert_video_to_audio(video_path, output_audio_path):
    try:
        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(output_audio_path)
        
        print(f"Audio successfully extracted to {output_audio_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Path to the video file
    video_path = "/path/to/your/video.mp4"
    
    # Path where the audio will be saved
    output_audio_path = "output_audio.wav"
    
    # Convert the video to audio
    convert_video_to_audio(video_path, output_audio_path)
