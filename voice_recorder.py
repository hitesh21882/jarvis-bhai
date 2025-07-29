import pyaudio
import wave
from playsound import playsound

def record_audio(output_filename, duration=5, sample_rate=44100, channels=2, chunk_size=1024):
    """
    Record audio and save it to a file.
    :param output_filename: Name of the output WAV file
    :param duration: Duration of recording in seconds
    :param sample_rate: Sampling rate
    :param channels: Number of audio channels
    :param chunk_size: Chunk size for buffer
    """
    audio = pyaudio.PyAudio()

    # Start recording
    print("Recording...")
    stream = audio.open(format=pyaudio.paInt16,
                        channels=channels,
                        rate=sample_rate,
                        input=True,
                        frames_per_buffer=chunk_size)
    
    frames = []

    for _ in range(0, int(sample_rate / chunk_size * duration)):
        data = stream.read(chunk_size)
        frames.append(data)

    # Stop recording
    print("Recording finished.")
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save to a WAV file
    with wave.open(output_filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))

    print(f"Audio saved as {output_filename}")

def play_audio(file_path):
    
    print(f"Playing {file_path}...")
    playsound(file_path)

if __name__ == "__main__":
    output_file = "recorded_audio.wav"
    record_audio(output_file, duration=5)  # Record for 5 seconds
    play_audio(output_file)  # Play the recorded audio
