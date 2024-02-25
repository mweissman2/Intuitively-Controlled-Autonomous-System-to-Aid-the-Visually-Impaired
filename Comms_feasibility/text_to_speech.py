import time
import json
import elevenlabs

# NOTE: ELEVEN LABS requires ffmpeg: https://ffmpeg.org/download.html
import os

os.environ['PATH'] += os.pathsep + 'C:/Users/Max/Documents/Misc/ffmpeg-master-latest-win64-gpl/bin'

# Get API KEY
config_path = 'C:/Users/Max/Desktop/api_keys.json'
with open(config_path) as f:
    ELEVENLABS_API_KEY = json.load(f)['ELEVENLABS_API_KEY']
elevenlabs.set_api_key(ELEVENLABS_API_KEY)

short = "What is the meaning of life?"
medium = "As a large language model, I have access to an immense amount of information. Can you tell me about a " \
         "specific topic you'd like a summary of?"
long = "Imagine you're on a journey through a vast, star-filled galaxy. You've landed on a strange new planet, " \
       "teeming with life unlike any you've ever seen. Describe the sights, sounds, and sensations of this alien " \
       "world. What creatures do you encounter? What mysteries await you as you explore? Let your imagination run " \
       "wild and tell me about your adventure in detail."

prompts = [short, medium, long]


# Eleven Labs workflow
def tts_play(text_to_play):
    start_time = time.time()
    audio = elevenlabs.generate(
        # api_key="YOUR_API_KEY", (Defaults to os.getenv(ELEVEN_API_KEY))
        text=text_to_play,
        voice="Bill",
        model="eleven_multilingual_v2"
    )
    end_play_time = time.time()
    play_time = end_play_time - start_time
    print(play_time)

    elevenlabs.play(audio)


def tts_stream(text_to_play):
    """
    Requires MPV(https://mpv.io/) for streaming
    """
    audio_stream = elevenlabs.generate(
        # api_key="YOUR_API_KEY", (Defaults to os.getenv(ELEVEN_API_KEY))
        text=text_to_play,
        voice="Bill",
        model="eleven_multilingual_v2"
    )
    elevenlabs.stream(audio_stream)


def tts_save(text_to_play, path_to_file):
    start_time = time.time()
    audio = elevenlabs.generate(
        # api_key="YOUR_API_KEY", (Defaults to os.getenv(ELEVEN_API_KEY))
        text=text_to_play,
        voice="Bill",
        model="eleven_multilingual_v2"
    )
    end_play_time = time.time()
    play_time = end_play_time - start_time
    print(play_time)

    elevenlabs.save(audio, path_to_file)


tts_play(prompts[0])
tts_save(prompts[0], 'audio_output/test.wav')
