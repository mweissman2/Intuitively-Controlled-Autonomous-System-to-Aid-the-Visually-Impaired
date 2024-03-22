from Speech_to_text.ASR import *


def run_input_comms():
    # Setup Queues
    audio_chunk_q = queue.Queue()
    text_command_q = queue.Queue()

    # Create and run audio_listener
    audio_listener = AudioTranscriber(audio_chunk_q, text_command_q)
    audio_listener.audio_listener()


def main():
    run_input_comms()


if __name__ == "__main__":
    main()
