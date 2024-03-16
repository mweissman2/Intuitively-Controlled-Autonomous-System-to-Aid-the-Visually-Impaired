import utils
import speech_recognition as sr
from openai import OpenAI
import queue
from time import sleep
import datetime
import io
import threading


class AudioTranscriber:
    def __init__(self):
        # Setup OpenAI
        self.KEY = utils.get_key("OPENAI_API_KEY")
        self.client = OpenAI(api_key=self.KEY)

        # Set up recorder and mic
        self.mic = sr.Microphone()
        self.recorder = sr.Recognizer()
        self.recorder.energy_threshold = 1000
        self.recorder.dynamic_energy_threshold = False
        with self.mic:
            self.recorder.adjust_for_ambient_noise(self.mic)

        self.chunk_time = 2
        self.phrase_time = None

        # Setup model and Queue
        self.audio_in_queue = queue.Queue()

        # Initialize transcription
        self.transcription = ['']

    def recorder_callback(self, _, audio):
        self.audio_in_queue.put(audio)
        print(f"Queue size: {self.audio_in_queue.qsize()}")
        if not self.audio_in_queue.empty():
            print(f"Newest Item: {self.audio_in_queue.queue[0]}")

    def audio_listener(self):
        print("Listening...")
        # Start new background thread for listener
        self.recorder.listen_in_background(self.mic, self.recorder_callback, phrase_time_limit=2)

        while True:
            try:
                self.transcriber()
            except KeyboardInterrupt:
                break
            except queue.Empty:
                print("TIME OUT: No input detected")
                break

        print("\n\nTranscription:")
        for line in self.transcription:
            print(line)

    def transcriber(self):
        # Pull audio from queue
        audio_data = self.audio_in_queue.get(block=True, timeout=5)

        now = datetime.datetime.utcnow()
        phrase_complete = False
        # If enough time has passed between recordings, consider the phrase complete.
        if self.phrase_time and now - self.phrase_time > datetime.timedelta(seconds=2):
            phrase_complete = True
        # This is the last time we received new audio data from the queue.
        self.phrase_time = now

        # Convert audio data to WAV format and name (this is important for openAI call to work)
        buffer = io.BytesIO(audio_data.get_wav_data())
        buffer.name = 'file.wav'

        # Read the transcription.
        print("Processing...")
        result = self.client.audio.transcriptions.create(
            model="whisper-1",
            file=buffer,
            response_format="text",
        )
        print("Processed!")

        # If we detected a pause between recordings, add a new item to our transcription.
        # Otherwise, edit the existing one.
        if phrase_complete:
            self.transcription.append(result)
        else:
            self.transcription[-1] = result

        print(result)

        # Consider including slight delay
        # sleep(0.25)


def main():
    audio_listener = AudioTranscriber()
    audio_listener.audio_listener()


if __name__ == "__main__":
    main()
