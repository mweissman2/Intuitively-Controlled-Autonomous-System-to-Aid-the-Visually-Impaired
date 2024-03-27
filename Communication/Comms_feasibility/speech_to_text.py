import time
import json
from openai import OpenAI

# Get API KEY
config_path = 'C:/Users/Max/Desktop/api_keys.json'
with open(config_path) as f:
    OPENAI_API_KEY = json.load(f)['OPENAI_API_KEY']
client = OpenAI(
    api_key=OPENAI_API_KEY
)


# Set audio file and transcribe
def OpenAI_transcribe(audio_file):
    start_time = time.time()
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        response_format="text"
    )
    end_play_time = time.time()
    play_time = end_play_time - start_time
    print(play_time)

    return transcript


file = open('audio_output/medium.wav', "rb")
print(OpenAI_transcribe(file))
