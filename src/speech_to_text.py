import sounddevice as sd
import numpy as np
import wave
import whisper
import os

# Load Whisper model
model = whisper.load_model("base")

def record_audio(filename="user_audio.wav", record_seconds=5, sample_rate=44100):
    """
    Records audio from the microphone and saves it as a WAV file.

    Parameters:
    - filename (str): Name of the output audio file
    - record_seconds (int): Duration of recording in seconds
    - sample_rate (int): Sample rate of the recording
    """
    print("🎙️ Recording...")
    
    try:
        # Record audio
        audio_data = sd.rec(int(record_seconds * sample_rate), samplerate=sample_rate, channels=1, dtype=np.int16)
        sd.wait()  # Wait for recording to finish

        # Save the audio file
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(np.dtype(np.int16).itemsize)
            wf.setframerate(sample_rate)
            wf.writeframes(audio_data.tobytes())

        print(f"✅ Recording finished. Saved as {filename}")

    except Exception as e:
        print(f"❌ Error during recording: {e}")

def transcribe_audio(filename="user_audio.wav"):
    """
    Transcribes the given audio file using Whisper.

    Parameters:
    - filename (str): Path to the audio file

    Returns:
    - (str): Transcribed text
    """
    if not os.path.exists(filename):
        print(f"❌ Error: File '{filename}' not found.")
        return None

    try:
        print("📝 Transcribing audio...")
        result = model.transcribe(filename)
        text = result["text"].strip()
        print(f"✅ Transcription: {text}")
        return text

    except Exception as e:
        print(f"❌ Error during transcription: {e}")
        return None

if __name__ == "__main__":
    record_audio()
    transcribe_audio()
