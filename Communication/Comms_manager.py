from Speech_to_text.ASR_with_wakeword import AudioTranscriber
from multiprocessing import Process, Queue


def run_input_comms():
    # Setup Queues
    audio_chunk_q = Queue()
    text_command_q = Queue()

    # Set wake-word model path
    keyword_path = "Speech_to_text/Hey-Jimbo_en_windows_v3_0_0.ppn"

    # Create and run audio_listener
    audio_listener = AudioTranscriber(audio_chunk_q, text_command_q, keyword_path)
    p1 = Process(audio_listener.audio_listener())

    p1.start()


def main():
    run_input_comms()


if __name__ == "__main__":
    main()
